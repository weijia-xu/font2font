# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

import argparse
import sys
import numpy as np
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
import collections

reload(sys)
sys.setdefaultencoding("utf-8")

def splice_images(root_dir, img_list, canvas_size, num_img):
    cls_names = img_list.split(',')
    num_cls = len(cls_names)
    example_img = Image.new("RGB", (canvas_size * num_img, canvas_size * num_cls), (255, 255, 255))

    column = 0
    for cls_name in cls_names:
        row = 0
        column += 1
        filepath = os.path.join(root_dir, cls_name)
        img_names = os.listdir(filepath)
        for name in img_names:
            img = Image.open(os.path.join(filepath, name)).resize((canvas_size, canvas_size), Image.ANTIALIAS)
            example_img.paste(img, (row * canvas_size, (column - 1) * canvas_size))
            row += 1

    return example_img

parser = argparse.ArgumentParser(description='Splice images together')
parser.add_argument('--root_dir', dest='root_dir', required=True, help='root path of images')
parser.add_argument('--img_list', dest='img_list', required=True, help='list of images')
parser.add_argument('--dst_path', dest='dst_path', required=True, help='path of result image')
parser.add_argument('--canvas_size', dest='canvas_size', type=int, default=256, help='canvas size')
parser.add_argument('--num_images', dest='num_images', type=int, default=10, help='number of images displayed for each class')

args = parser.parse_args()

if __name__ == "__main__":
    example_img = splice_images(args.root_dir, args.img_list, args.canvas_size, args.num_images)
    example_img.save(args.dst_path)
