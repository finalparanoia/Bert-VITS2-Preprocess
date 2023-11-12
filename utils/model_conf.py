from json import loads, dumps
from config.config import dataset_dir


def gen_config(dataset_name: str):
    with open("./config/config.json", "r") as f:
        conf = loads(f.read())
        conf["data"]["spk2id"][dataset_name] = 0
    with open(f"{dataset_dir}/{dataset_name}/config.json", "w") as f:
        f.write(dumps(conf))
