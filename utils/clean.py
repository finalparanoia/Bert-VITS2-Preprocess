from config.config import dataset_dir
from utils.basic.file import ls, rm


def clean(dataset_name: str):

    for raw_wav in ls(f"{dataset_dir}/{dataset_name}/audios/raw/*.wav"):
        rm(raw_wav)
