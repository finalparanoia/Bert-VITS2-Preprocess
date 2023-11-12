# 快速开始

### 在开始前，你可能还需要阅读一下：[开始之前](./before.md)

## 1. git clone 本项目

在一个你看着顺眼的目录打开终端，并输入命令：

```shell
git clone https://github.com/finalparanoia/Bert-VITS2-Preprocess
```
## 2. 安装依赖库

关于venv的使用，可参照[venv](./venv.md)

启用venv环境后，使用下方命令安装依赖项:

```shell
pip install -r requirements.txt
```

你还可以通过`-i 镜像链接`来加速下载，这里以清华PyPI源为例：

```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 运行
将需要处理的`wav`文件放入 Raw 目录中，然后运行命令：

```shell
python main.py
```

然后根据提示输入数据集的名称，等待程序执行完毕。

## 训练

接下来，你就可以将 Data 目录下的数据集拷贝至 Bert-VITS2 的 Data 目录下，并开始训练了。

~~说不定我哪天把Bert和preprocess也缝合进来~~

```shell
python preprocess_text.py
python bert_gen.py
torchrun --standalone train_ms.py -c Data/{数据集名称}/config.json -m Data/{数据集名称}
```
