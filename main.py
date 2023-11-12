from utils.create import create
from utils.tag import tag
from utils.resample import resample


if __name__ == "__main__":
    pass
    dataset_name = input("请为数据集命名：")
    create(dataset_name)
    resample(dataset_name)
    tag(dataset_name)
