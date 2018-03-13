# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 16:37:54 2018

@author: h1410
"""

from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

count = 0

for w in range(20, 50, 10):
    for x in range(80, 120, 10):
        for t in range(20, 50, 10):
            im = Image.new('RGB', (320,180), (255,255,255))
            draw = ImageDraw.Draw(im)
            
            draw.line((x, 0, x, im.size[1]), fill=128, width=w)
            draw.line((im.size[0]-x, 0, im.size[0]-x, im.size[1]), fill=128, width=w)
            draw.line((x, im.size[1]/2, im.size[0]-x, im.size[1]/2), fill=128, width=t)
            
            count += 1
            im.save(str(count)+".png")