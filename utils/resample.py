import os
import librosa
from multiprocessing import Pool, cpu_count

import soundfile
from tqdm import tqdm
from model_conf.config import dataset_dir


def process(item: set[str, str, str, str]):
    spk_dir, wav_name, in_dir, out_dir = item
    wav_path = os.path.join(in_dir, spk_dir, wav_name)
    if os.path.exists(wav_path) and ".wav" in wav_path:
        wav, sr = librosa.load(wav_path, sr=44100)
        soundfile.write(os.path.join(out_dir, spk_dir, wav_name), wav, int(sr))


def resample(dataset_name: str):
    current_dataset_dir = f"{dataset_dir}/{dataset_name}"
    processes = cpu_count() - 2 if cpu_count() > 4 else 1

    pool = Pool(processes=processes)

    tasks = []

    in_dir = f"{current_dataset_dir}/audios/raw"
    out_dir = f"{current_dataset_dir}/audios/wavs"
    for dir_path, _, filenames in os.walk(in_dir):
        # 子级目录
        spk_dir = os.path.relpath(dir_path, in_dir)
        spk_dir_out = os.path.join(out_dir, spk_dir)
        if not os.path.isdir(spk_dir_out):
            os.makedirs(spk_dir_out, exist_ok=True)
        for filename in filenames:
            if filename.endswith(".wav"):
                tasks.append((spk_dir, filename, in_dir, out_dir))

    for _ in tqdm(
        pool.imap_unordered(process, tasks),
    ):
        pass

    pool.close()
    pool.join()

    print("音频重采样完毕!")


if __name__ == "__main__":
    pass
