# -*- coding: utf-8 -*-

from PIL import Image

from pythonds.trees import OctTree


# 简单图片量化算法
def simple_quant(img_path):
    img: Image.Image = Image.open(img_path)
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = r // (t := 255 // 7) * t
            g = g // (t := 255 // 6) * t
            b = b // (t := 255 // 6) * t
            img.putpixel((x, y), (r, g, b))
    img.show()
    img.save('img/simpleQuant.jpg')


# 基于八叉树的图片量化算法
def oct_tree_quant(img_path):
    img: Image.Image = Image.open(img_path)
    width, height = img.size
    ot = OctTree()

    # 遍历所有像素，构建八叉树
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            ot.insert(r, g, b)

    ot.reduce(256)  # 缩减为256种颜色

    # 遍历所有像素，用量化后的新值替换旧值
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            nr, ng, nb = ot.find(r, g, b)
            img.putpixel((x, y), (nr, ng, nb))

    img.show()
    img.save('img/octTreeQuant.jpg')


if __name__ == '__main__':
    img_path = 'img/bubbles.jpg'
    simple_quant(img_path)
    oct_tree_quant(img_path)
