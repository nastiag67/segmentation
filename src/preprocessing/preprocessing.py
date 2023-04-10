import pandas as pd
import glob
import os
from src import config

def read_folders():
    # Raw data
    data_map = []
    for sub_dir_path in glob.glob(config.DATA_PATH+"*"):
        print(sub_dir_path)
        if os.path.isdir(sub_dir_path):
            dirname = sub_dir_path.split("/")[-1]
            for filename in os.listdir(sub_dir_path):
                image_path = sub_dir_path + "/" + filename
                data_map.extend([dirname, image_path])
        else:
            print("This is not a dir:", sub_dir_path)
            
            
    df = pd.DataFrame({"dirname" : data_map[::2],
                    "path" : data_map[1::2]})
    return df