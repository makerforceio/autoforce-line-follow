# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:31:30 2018

@author: h1410
"""

from six.moves import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 6):
    f = open('C:\Users\h1410\OneDrive\Documents\GitHub\cifar10\data_batch_'+str(i), 'rb')
    tupled_data= pickle.load(f)
    f.close()
    img = tupled_data[b'data']
    count = 0
    for j in range(10000):
        single_img = np.array(img[j])
        single_img_reshaped = np.transpose(np.reshape(single_img,(3, 32,32)), (1,2,0))
        plt.imshow(single_img_reshaped)
        dir = 'C:\Users\h1410\OneDrive\Documents\GitHub\cifar10\\'+str(j)
        plt.savefig(dir)