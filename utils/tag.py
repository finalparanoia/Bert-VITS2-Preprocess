from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from config.config import dataset_dir, modelscope_model
from utils.basic.file import ls, exist


def read_breakpoint(file_list_path: str) -> list:
    complete_list = []
    if not exist(file_list_path):
        return complete_list

    with open(file_list_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            pt, _, _ = line.strip().split('|')
            complete_list.append(pt)
    return complete_list


def tag(dataset_name: str):
    current_dataset_dir = f"{dataset_dir}/{dataset_name}"
    audio_dir = f"{current_dataset_dir}/audios/wavs"
    filelist = ls(f"{audio_dir}/*.wav")
    file_list_path = f"{current_dataset_dir}/filelists/{dataset_name}.list"

    complete_list = read_breakpoint(file_list_path)

    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model=modelscope_model
    )

    for file in filelist:
        if file[-3:] != 'wav':
            continue

        # todo 支持单数据集多角色

        if file in complete_list:
            continue

        rec_result = inference_pipeline(file)

        if 'text' not in rec_result:
            continue

        line = file + "|" + dataset_name + "|ZH|" + rec_result['text'] + "\n"

        with open(file_list_path, 'a', encoding='utf-8') as f:
            f.write(line)
