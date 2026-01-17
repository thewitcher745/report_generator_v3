"""
This is the conversation handler staget  confirm the user inputs and ask if the user needs to customize them.
"""

from tg.handler_functions.helpers.confirm_helpers import (
    apply_multiple_mode_leverage_override,
    build_multiple_snapshot,
    build_report_inputs,
    get_mass_sending_destination,
    get_requester_chat_id,
    maybe_adjust_targets_inplace,
    reset_user_data_for_next_multiple_report,
)
from telegram import InputMediaPhoto

from tg.handler_functions.helpers.prompts import (
    prompt_get_exchange,
)
from tg.handler_functions.helpers.conversation_stages import (
    END,
    GET_EXCHANGE,
)
from tg.handler_functions.helpers.utilities import send_media_group, send_message
from tg.handler_functions.helpers import strings


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

    requester_chat_id = get_requester_chat_id(update)

    if context.user_data.get("multiple_mode"):
        queue: list[dict] = context.user_data.setdefault("multiple_queue", [])
        n_reports = int(context.user_data.get("multiple_n_reports") or 0)
        current_index = int(context.user_data.get("multiple_current_index") or 0)

        leverage_counters: dict[str, int] = context.user_data.setdefault(
            "multiple_leverage_counters", {}
        )

        queue.append(build_multiple_snapshot(context.user_data))

        current_index += 1
        context.user_data["multiple_current_index"] = current_index

        if n_reports and current_index < n_reports:
            reset_user_data_for_next_multiple_report(context.user_data)

            await send_message(
                context,
                update,
                strings.MULTIPLE_REPORT_PROGRESS(current_index + 1, n_reports),
            )
            await prompt_get_exchange(update, context)
            return GET_EXCHANGE

        for queued in list(queue):
            image_id = str(queued.get("image_id") or "")
            destination_chat_id, rule = get_mass_sending_destination(
                queued=queued, requester_chat_id=requester_chat_id
            )

            try:
                maybe_adjust_targets_inplace(queued=queued)
                apply_multiple_mode_leverage_override(
                    queued=queued,
                    counters=leverage_counters,
                )
                report_data_array, extra_features, ReportClassCurrent = (
                    build_report_inputs(queued)
                )

                if rule.message_body:
                    await context.bot.send_message(
                        chat_id=destination_chat_id,
                        text=rule.message_body,
                    )

                for counter, report_data in enumerate(report_data_array):
                    driver = None
                    try:
                        report = ReportClassCurrent(
                            report_data, extra_features=extra_features
                        )
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

            except Exception as exc:
                await context.bot.send_message(
                    chat_id=requester_chat_id,
                    text=f"❌ Failed processing queued report ({image_id}): {exc}",
                )

        context.user_data.clear()
        return END

    report_data_array, extra_features, ReportClass = build_report_inputs(
        context.user_data
    )

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
