#!/usr/bin/env python3
# coding=utf-8
import os
import numpy as np
from PIL import Image
import cv2

dir1 = './mask'
dir2 = './image'

txt = './train.txt'
f = open(txt,'a')
area = 0
count = 0
flag = 1

for filename in os.listdir(dir1):

    fn = filename.split('.')[0]
    if not os.path.exists(dir2+ '/'+fn+'.jpg'):
        print(filename.split('.')[0])

    image = Image.open(dir1+'/'+filename)
    
    
    
    image = np.array(image)
    try:
        width, height = image.shape
        #print(width, height)
    except:
        #print(filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        width, height = image.shape
        #print(width, height)
    

    
    for h in range(height):
        for w in range(width):
            if image[w, h] == 255:
                f.write(filename.split('.')[0])
                f.write("\n")
                flag = 0
                print(count)
                count += 1
                break
        if flag ==0:
            flag = 1
            break

f.close()


