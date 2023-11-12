from glob import glob
from shutil import move
from os.path import exists
from os import mkdir, remove


def rm(path: str):
    remove(path)


def ls(path: str) -> list[str]:
    resp = []
    for item in glob(path):
        resp.append(item.replace("\\", "/"))
    return resp


def mv(__old__: str, __new__: str):
    move(__old__, __new__)


def exist(path: str):
    return exists(path)
