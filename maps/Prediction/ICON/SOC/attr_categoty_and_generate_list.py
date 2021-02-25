#!/usr/bin/env python3
# coding=utf-8
import os
import numpy as np
from PIL import Image
import cv2
from shutil import copyfile

dir = './SOC-1200' # only mask

txt_ac = './Attribute/AC.txt'
txt_bo = './Attribute/BO.txt'
txt_cl = './Attribute/CL.txt'
txt_ho = './Attribute/HO.txt'
txt_mb = './Attribute/MB.txt'
txt_oc = './Attribute/OC.txt'
txt_ov = './Attribute/SC.txt'
txt_sc = './Attribute/SV.txt'
txt_so = './Attribute/SO.txt'

ATTR = ['AC', 'BO', 'CL', 'HO', 'MB', 'OC', 'OV', 'SC', 'SO']

for i in range(len(ATTR)):

    if not os.path.exists('SOC-'+ATTR[i]+'/mask'):
        os.makedirs('SOC-'+ATTR[i]+'/mask')

for i in range(len(ATTR)):
    f_attr = open('./Attribute/'+ATTR[i]+'.txt')
    line = f_attr.read().splitlines()
    count = 0
    for j in range(len(line)):
        
        pred_  = cv2.imread('SOC-1200/' +line[j]+'.png')

        cv2.imwrite('SOC-'+ATTR[i]+'/' +line[j]+'.png', pred_)
        count += 1

    f_attr.close()
    copyfile('./Attribute/'+ATTR[i]+'.txt', 'SOC-'+ATTR[i]+'/test.txt')
    print(ATTR[i]+': '+str(count))  


