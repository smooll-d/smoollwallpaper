import os

from convert_all_to_bmp import convert_all_to_bmp

def start_img_wallpaper():
    os.system(f"xsetroot -bitmap {convert_all_to_bmp.converted_image_path}")
