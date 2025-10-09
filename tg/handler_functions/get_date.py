"""
This file contains the handler that returns the current date.
"""

import datetime
from tg.handler_functions import check_missing


async def get_date(update, context):
    

    await check_missing(update, context)
