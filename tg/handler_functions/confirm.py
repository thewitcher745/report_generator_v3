"""
This is the conversation handler staget  confirm the user inputs and ask if the user needs to customize them.
"""

import copy
from telegram import InputMediaPhoto

from image.report_generator.report_classes.BaseReport import BaseReport
from static.report_class_mapping import MAPPING
from tg.handler_functions.helpers.calc_report_numbers import calc_report_numbers
from tg.handler_functions.helpers.conversation_stages import (
    END,
    CUSTOMIZE_QR,
    CUSTOMIZE_REFERRAL,
    CUSTOMIZE_USERNAME,
    GET_CHANNEL,
)
from tg.handler_functions.helpers.extra_features import get_extra_features
from tg.handler_functions.helpers.mass_sending import resolve_mass_sending_rule
from tg.handler_functions.helpers.utilities import send_media_group, send_message
from tg.handler_functions.helpers import strings, keyboards


async def confirm(update, context):
    if update.callback_query:
        await update.callback_query.answer()

    if update.callback_query:
        confirmation_dialog_answer = update.callback_query.data

        if confirmation_dialog_answer == "confirm":
            print("Data acquired successfully!")
        elif confirmation_dialog_answer == "customize_qr":
            print("Customize QR")
        elif confirmation_dialog_answer == "customize_referral":
            print("Customize Referral")
        elif confirmation_dialog_answer == "customize_username":
            print("Customize Username")

    requester_chat_id = (
        update.callback_query.message.chat_id
        if update.callback_query
        else update.message.chat_id
    )

    if context.user_data.get("multiple_mode"):
        queue: list[dict] = context.user_data.setdefault("multiple_queue", [])
        n_reports = int(context.user_data.get("multiple_n_reports") or 0)
        current_index = int(context.user_data.get("multiple_current_index") or 0)

        snapshot = copy.deepcopy(context.user_data)
        snapshot.pop("multiple_queue", None)
        snapshot.pop("multiple_current_index", None)
        snapshot.pop("multiple_n_reports", None)
        snapshot.pop("multiple_mode", None)
        snapshot.pop("current_feature", None)
        queue.append(snapshot)

        current_index += 1
        context.user_data["multiple_current_index"] = current_index

        if n_reports and current_index < n_reports:
            for key in [
                "channel",
                "exchange",
                "image_id",
                "template",
                "precision",
                "qr",
                "referral",
                "username",
                "avatar",
                "date",
                "input_date",
                "period_start",
                "period_end",
                "pnl_usd",
                "pnl_percent",
                "input_symbol",
                "input_signal_type",
                "leverage_type",
                "input_leverage",
                "risk_percent",
                "input_entry_price",
                "input_target_price",
                "liq_price",
                "position_size",
                "margin",
            ]:
                context.user_data.pop(key, None)
            context.user_data.pop("current_feature", None)

            await send_message(
                context,
                update,
                strings.MULTIPLE_GET_CHANNEL(current_index + 1, n_reports),
                keyboard=keyboards.GET_CHANNELS(),
            )
            return GET_CHANNEL

        for queued in list(queue):
            channel = str(queued.get("channel") or "")
            exchange = str(queued.get("exchange") or "")
            image_id = str(queued.get("image_id") or "")
            template = str(queued.get("template") or "")

            rule = resolve_mass_sending_rule(
                channel=channel,
                exchange=exchange,
                image_id=image_id,
                template=template,
            )
            destination_chat_id = rule.user_id or requester_chat_id

            try:
                report_data_array = calc_report_numbers(queued)
                extra_features = get_extra_features(image_id)
                ReportClass: type[BaseReport] | None = MAPPING.get(image_id, None)
                if ReportClass is None:
                    raise ValueError("Report class not found.")

                for counter, report_data in enumerate(report_data_array):
                    driver = None
                    try:
                        report = ReportClass(report_data, extra_features=extra_features)
                        image_path, driver = report.save_image(counter=counter)
                        await context.bot.send_media_group(
                            chat_id=destination_chat_id,
                            media=[InputMediaPhoto(open(image_path, "rb"))],
                        )
                    except Exception as exc:
                        await context.bot.send_message(
                            chat_id=requester_chat_id,
                            text=f"❌ Failed generating {image_id} image #{counter + 1}: {exc}",
                        )
                    finally:
                        if driver:
                            driver.quit()

                if rule.message_body:
                    await context.bot.send_message(
                        chat_id=destination_chat_id,
                        text=rule.message_body,
                    )
            except Exception as exc:
                await context.bot.send_message(
                    chat_id=requester_chat_id,
                    text=f"❌ Failed processing queued report ({image_id}): {exc}",
                )

        context.user_data.clear()
        return END

    report_data_array = calc_report_numbers(
        context.user_data,
    )
    extra_features = get_extra_features(context.user_data["image_id"])
    ReportClass: type[BaseReport] | None = MAPPING.get(
        context.user_data["image_id"], None
    )

    if ReportClass is None:
        print("Invalid report class definition for ", context.user_data["image_id"])
        raise ValueError("Report class not found.")

    for counter, report_data in enumerate(report_data_array):
        driver = None
        try:
            report = ReportClass(report_data, extra_features=extra_features)
            image_path, driver = report.save_image(counter=counter)
            await send_media_group(context, update, file_address=image_path)
        finally:
            if driver:
                driver.quit()

    context.user_data.clear()

    return END
