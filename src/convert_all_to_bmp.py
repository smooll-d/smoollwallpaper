from PIL import Image

from config_file import config_file

def convert_all_to_bmp():
    convert_all_to_bmp.img = Image.open(config_file.path_img)
    convert_all_to_bmp.img.save(f"{config_file.path_img}.bmp")

    convert_all_to_bmp.converted_image_path = f"{config_file.path_img}.bmp"
