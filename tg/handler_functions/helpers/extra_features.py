"""
This module is uised to get the extra inputs and outputs for the signal where necessary. If an item doesn't exist in the lists, that means that image only requires the very basic
signal information and nothing else. Otherwise, "margin", "referral", "qr", "username", "date", etc. are included in the value of the key where required.
As
"""

extra_features = {
    "bitget_5": ["date"],
    "bingx_10": ["date"],
    "mexc_7": ["margin", "date", "input_date"],
    "mexc_8": ["date"],
    "binance_6": ["margin", "date"],
    "kcex_1": ["date"],
}


def get_extra_features(image_id: str) -> list[str]:
    """
    Returns the extra features for the given image id.
    Args:
        image_id (str): The image id.
    Returns:
        list[str]: The extra features for the given image id, including "margin", "date", "qr", "referral", etc.
    """
    return extra_features.get(image_id, [])


def is_extra_feature_missing(context, feature: str) -> bool:
    """
    Checks if the extra feature is missing.
    Args:
        context (ContextTypes.DEFAULT_TYPE): The context object.
        feature (str): The feature to check.
    Returns:
        bool: True if the extra feature is missing, False otherwise.
    """
    extra_features = get_extra_features(context.user_data["image_id"])
    if feature in extra_features and (
        context.user_data.get(feature, None) is None
        or context.user_data.get(feature, None) == ""
    ):
        return True
    return False
