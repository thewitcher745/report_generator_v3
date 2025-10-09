from tg.handler_functions.helpers.keyboards_statics import IMAGE_LIST


def get_unique_images_by_exchange(exchange: str) -> list[str]:
    """
    This functions gets the image_id's for all the images that have a unique image_list_label in the list of images. These images are then composed
    into a collage and sent to the user to choose from.

    Args:
        exchange (str): The exchange to get the images for.

    Returns:
        list[str]: The image_id's for all the images that have a unique image_list_label in the list of images.
    """
    exchange_image_list = IMAGE_LIST[exchange]

    unique_images = []
    for image in exchange_image_list:
        if image["image_list_label"] not in [
            image["image_list_label"] for image in unique_images
        ]:
            unique_images.append(image)

    return [image["callback_query"] for image in unique_images]


def get_image_list_label_by_id(image_id: str) -> int | None:
    exchange = image_id.split("_")[0]
    exchange_image_list = IMAGE_LIST[exchange]
    for image in exchange_image_list:
        if image["callback_query"] == image_id:
            return image["image_list_label"]

    return None
