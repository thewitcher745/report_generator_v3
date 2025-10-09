"""
This module contains the base class for all reports, including the __init__ method.
"""


class BaseReport:
    def __init__(self, user_data: dict):
        """
        Initializes the BaseReport class.

        Args:
            user_data (dict): The user data, taken from the context.user_data object of the bot.
        """

        self.user_data = user_data

        # These properties always exist, taken from the signal text.
        self.symbol: str = user_data["symbol"]
        self.signal_type: str = user_data["signal_type"]
        self.leverage: str = user_data["leverage"]
        self.entry: str = user_data["entry"]
        self.targets: str = user_data["targets"]
        self.stop: str = user_data["stop"]

        # These properties always exist, taken from the user's inputs.
        self.exchange: str = user_data["exchange"]
        self.template: str = user_data["template"]
        self.image_id: str = user_data["image_id"]
        self.qr: str = user_data["qr"]
        self.referral: str = user_data["referral"]

        # The following properties may or may not exist in the user_data dictionary.
        if "username" in user_data:
            self.username: str = user_data["username"]
        if "tz" in user_data:
            self.tz: str = user_data["tz"]

    def print_info(self):
        """
        Prints all the properties of the BaseReport class.
        """
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def draw_roi(self):
        """
        Draws the ROI on the image.
        """
        pass
