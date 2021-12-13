# -*- coding:utf-8 -*-
# @File : 1_安装依赖.py
import os

libs = {"lxml", "requests", "pandas", "numpy", "you-get", "opencv-python", "pandas", "fake_useragent", "matplotlib",
        "moviepy", "wordcloud", "jieba", "baidu-aip"}


def install():
    try:
        for lib in libs:
            os.system(f"pip3 install -i https://pypi.doubanio.com/simple/ {lib}")
            print(lib + "安装成功")
    except:
        print("安装失败")


if __name__ == '__main__':
    install()
