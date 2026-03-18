import os
import shutil
from pathlib import Path
from PIL import Image, ImageDraw
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()
IMAGE_DIR = BASE_DIR / "images"
RESULT_DIR = BASE_DIR / "results"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

def save_uploaded_file(uploaded_file):
    file_path = IMAGE_DIR / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(file_path)

def create_zip_file(path_folder_to_zip, zip_name):
    shutil.make_archive(zip_name, "zip", path_folder_to_zip)

def load_image_pil(file_path):
    img = Image.open(file_path)
    draw = ImageDraw.Draw(img)
    w, h = img.size
    return img, w, h, draw

def save_df_result(df, path):
    df.to_csv(path, sep=";", index=True)