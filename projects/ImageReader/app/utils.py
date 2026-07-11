def get_images(folder: Path) -> list[Path]:

    img_list = []
    img_suffix = [".jpg", ".jpeg", ".png", ".webp"]

    for item in folder.iterdir():
        if item.suffix.lower() in img_suffix:
            img_list.append(item)

    img_list.sort()

    return img_list
   