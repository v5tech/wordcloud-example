# -*- coding:utf-8 -*-
# @File : 5_解析弹幕.py

from xml.dom import minidom


def main():
    with open('./beauty.cmt.xml', 'r', encoding='utf-8') as f:
        dom = minidom.parse(f)
        # 获取根节点
        root = dom.documentElement
        with open('bullet.txt', 'w', encoding='utf-8') as fp:
            try:
                for i in range(1000):
                    name = root.getElementsByTagName('d')[i]
                    name_text_node = name.childNodes[0]
                    danmu = name_text_node.data
                    type(danmu)
                    fp.write(danmu)
                    fp.write('\n')
            except:
                print('over!')


if __name__ == '__main__':
    main()
