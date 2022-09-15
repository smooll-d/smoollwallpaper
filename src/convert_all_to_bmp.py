from PIL import Image
from pathlib import Path 

from config_file import config_file

def convert_all_to_bmp():
    filename = Path(config_file.path_img)
    img = Image.open(filename)

    img_convert = img.save(filename.with_suffix(".png"))

    print(img_convert)
