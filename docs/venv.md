# Venv

virtualenv在不同的操作系统下，使用不同的命令激活：
```shell
// Linux 
source venv/bin/activaate

// windows
venv/scripts/activate
```
在这种情况下，当命令提示符前出现`(venv)`前缀时，即为激活成功。

退出venv环境的命令是一致的：
```shell
deactivate
```

当命令提示符前`(venv)`前缀消失，即为成功退出。
