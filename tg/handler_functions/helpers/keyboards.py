"""
This file will contain the keyboards put under each message or prompt.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tg.handler_functions.helpers import keyboards_statics
from tg.handler_functions.helpers.templates import TEMPLATES


def compose_keyboard_markup(
    buttons_list: list[dict[str, str]], max_buttons_per_row: int = 2
) -> InlineKeyboardMarkup:
    """
    Composes a keyboard markup from a list of buttons, with a max number of columns.

    Args:
        buttons_list (list[dict[str, str]]): A list of buttons where the key is the button text and the value is the callback data.
        max_buttons_per_row (int, optional): The maximum number of buttons per row. Defaults to 2.

    Returns:
        InlineKeyboardMarkup: The composed keyboard markup.
    """
    keyboard = []
    for i in range(0, len(buttons_list), max_buttons_per_row):
        try:
            keyboard.append(
                [
                    InlineKeyboardButton(
                        button_item["label"],
                        callback_data=button_item["callback_query"],
                    )
                    for button_item in buttons_list[i : i + max_buttons_per_row]
                ]
            )

        # In case of an IndexError, it means that the last row has less than max_buttons_per_row buttons
        except (IndexError, KeyError):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        button_item["label"],
                        callback_data=button_item["callback_query"],
                    )
                    for button_item in buttons_list[i:]
                ]
            )

    return InlineKeyboardMarkup(keyboard)


# Get exchange keyboard
GET_EXCHANGE = compose_keyboard_markup(keyboards_statics.EXCHANGE_LIST)


# Get image selection keyboard for a selected exchange
def GET_IMAGE(exchange: str):
    return compose_keyboard_markup(keyboards_statics.IMAGE_LIST[exchange])


# Get template selection keyboard for a selected exchange
def GET_TEMPLATE(exchange: str):
    template_buttons = [
        {"label": template_label, "callback_query": template_label}
        for template_label in TEMPLATES[exchange].keys()
    ]
    return compose_keyboard_markup(template_buttons)


CONFIRM = compose_keyboard_markup(
    keyboards_statics.CONFIRM_DIALOG, max_buttons_per_row=1
)
