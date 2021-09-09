import json
import os

data_path = "/data01/appleternity/workspace/OpenNMT-py/data/scicap-small"

def load_data(rule:str, normalization:str, collection:str, phase=str):
    base_folder = "/data01/tingyao/figure_caption/data/output"
    data_path = os.path.join(
        base_folder, rule, normalization, 
        collection, f"{phase.upper()}_IMG_CAPTIONS_LIST.json"
    )
    with open(data_path, 'r', encoding='utf-8') as infile:
        ori_data = json.load(infile)
        data = [
            {
                "img": img_path,
                "text": caption_info["ori_cap"]
            }
            for img_path, caption_info in ori_data.items() 
        ]
    return data[:1000]

def build_data(phase:str="train"):
    print(f"Processing {phase} data")
    data = load_data(
        rule="rule_based+separator",
        normalization="advance_norm",
        collection="sent_max_1",
        phase=phase
    )

    # (1) build src-train.txt - image path
    with open(os.path.join(data_path, f"src-{phase}.txt"), 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join([d["img"] for d in data]))

    # (2) build tgt-train.txt - captions (separated by space)
    with open(os.path.join(data_path, f"tgt-{phase}.txt"), 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join([d["text"] for d in data]))

def main():
    build_data(phase="train")
    build_data(phase="val")
    build_data(phase="test")

if __name__ == "__main__":
    main()
