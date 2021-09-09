from PIL import Image
from tqdm import tqdm
import os
import json

image_folder = "/data01/tingyao/figure_caption/data/images"
data_folder = "/data01/appleternity/workspace/OpenNMT-py/data/scicap/image"

def load_image_list(rule:str, normalization:str, collection:str, phase=str):
    base_folder = "/data01/tingyao/figure_caption/data/output"
    data_path = os.path.join(
        base_folder, rule, normalization, 
        collection, f"{phase.upper()}_IMG_CAPTIONS_LIST.json"
    )
    with open(data_path, 'r', encoding='utf-8') as infile:
        ori_data = json.load(infile)
        data = [img_path for img_path, caption_info in ori_data.items()]
    return data

def build_image_data(phase:str="train"):
    image_list = load_image_list(
        rule="rule_based+separator",
        normalization="advance_norm",
        collection="sent_max_1",
        phase=phase
    )
    for filename in tqdm(image_list):
        with open(os.path.join(image_folder, filename), 'rb') as infile:
            with Image.open(infile) as img:
                resized_img = img.resize((256, 256), Image.ANTIALIAS)
                resized_img.save(os.path.join(data_folder, filename), resized_img.format)

def main():
    build_image_data(phase="val")
    build_image_data(phase="test")
    build_image_data(phase="train")

if __name__ == "__main__":
    main()
