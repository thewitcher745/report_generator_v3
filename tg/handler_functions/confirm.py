"""
This is the conversation handler staget  confirm the user inputs and ask if the user needs to customize them.
"""

from image.report_generator.report_classes.BaseReport import BaseReport
from static.report_class_mapping import MAPPING
from tg.handler_functions.helpers.calc_report_numbers import calc_report_numbers
from tg.handler_functions.helpers.conversation_stages import (
    END,
    CUSTOMIZE_QR,
    CUSTOMIZE_REFERRAL,
    CUSTOMIZE_USERNAME,
)
from tg.handler_functions.helpers.extra_features import get_extra_features
from tg.handler_functions.helpers.utilities import send_media_group


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

    # An array made up of different reports for each target
    report_data_array = calc_report_numbers(
        context.user_data,
    )
    extra_features = get_extra_features(context.user_data["image_id"])
    ReportClass: type[BaseReport] | None = MAPPING.get(
        context.user_data["image_id"], None
    )

    if ReportClass is None:
        raise ValueError("Report class not found.")

    driver = None

    for counter, report_data in enumerate(report_data_array):
        report = ReportClass(report_data, extra_features=extra_features)
        image_path, driver = report.save_image(counter=counter)
        await send_media_group(context, update, file_address=image_path)

    if driver:
        driver.quit()

        context.user_data.clear()

    return END
