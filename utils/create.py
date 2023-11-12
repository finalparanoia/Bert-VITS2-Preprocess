from utils.basic.file import ls, mv, exist, mkdir
from config.config import raw_dir, dataset_dir, tmp_dir
from pydub import AudioSegment
from pydub.silence import detect_nonsilent


def mk_dataset_dir(current_dataset_path: str):
    dir_tree = [
        current_dataset_path,
        current_dataset_path + "/audios",
        current_dataset_path + "/audios/Raw",
        current_dataset_path + "/audios/wavs",
        current_dataset_path + "/filelists",
    ]
    for dirs in dir_tree:
        mkdir(dirs)


def cut_long_silences(character, input_path, i):
    sound = AudioSegment.from_wav(input_path)
    duration_ms = len(sound)
    block = 2 * 60 * 1000
    start = 0
    end = block
    count = 0
    while end < duration_ms:
        cut_point = len(detect_nonsilent(sound[end:min(end + block, duration_ms)], min_silence_len=500))
        output_path = f"{tmp_dir}/{character}_{i}_{count}.wav"
        print(output_path)
        sound[start:end+cut_point].export(output_path, format="wav")
        count += 1
        start = end + cut_point
        end = start + block

    output_path = f"{tmp_dir}/{character}_{i}_{count}.wav"
    print(output_path)
    sound[start:duration_ms].export(output_path, format="wav")
    print("finish", input_path)


def create(dataset_name: str):
    raw_files = ls(f"{raw_dir}/*.wav")
    current_dataset_path = f"{dataset_dir}/{dataset_name}"
    i = 0

    if exist(current_dataset_path):
        mv(current_dataset_path, current_dataset_path+".old")

    mk_dataset_dir(current_dataset_path)

    for raw_file in raw_files:
        cut_long_silences(dataset_name, raw_file, i)
        i += 1

    for tmp in ls(f"{tmp_dir}/*.wav"):
        mv(tmp, f"{current_dataset_path}/audios/Raw")
