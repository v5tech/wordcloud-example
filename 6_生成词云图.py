# -*- coding:utf-8 -*-
# @File : 6_生成词云图.py

import collections
import re

import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# 读取数据
with open('bullet.txt') as f:
    data = f.read()

# 文本预处理  去除一些无用的字符只提取出中文出来
new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
new_data = "/".join(new_data)

# 文本分词
seg_list_exact = jieba.cut(new_data, cut_all=True)

result_list = []
with open('stop_words.txt', encoding='utf-8') as f:
    con = f.read().split('\n')
    stop_words = set()
    for i in con:
        stop_words.add(i)

for word in seg_list_exact:
    # 设置停用词并去除单个词
    if word not in stop_words and len(word) > 1:
        result_list.append(word)

# 筛选后统计词频
word_counts = collections.Counter(result_list)
path = './wordcloud/'

for num in range(88, 888):
    img = f'./mask_img/mask_{num}.png'
    # 获取蒙版图片
    mask_ = 255 - np.array(Image.open(img))
    # 绘制词云
    plt.figure(figsize=(8, 5), dpi=200)
    my_cloud = WordCloud(
        background_color='black',  # 设置背景颜色  默认是black
        mask=mask_,  # 自定义蒙版
        mode='RGBA',
        max_words=500,
        font_path='simhei.ttf',  # 设置字体  显示中文
    ).generate_from_frequencies(word_counts)

    # 显示生成的词云图片
    plt.imshow(my_cloud)
    # 显示设置词云图中无坐标轴
    plt.axis('off')
    word_cloud_name = path + 'wordcloud_{}.png'.format(num)
    my_cloud.to_file(word_cloud_name)  # 保存词云图片
    print(f'======== 第{num}张词云图生成 ========')
