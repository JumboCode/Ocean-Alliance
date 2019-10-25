import cv2
import os
import numpy as np

'''
this script takes a jpg image and converts it into a feature vector
encoding the following information: pixel red channel value average for 
the full image, blue average, green average, then red standard devation
and the same for blue and green.
'''


fname = 'frame52.jpg'

img = cv2.imread(fname)
(means, stds) = cv2.meanStdDev(img)
stats = np.concatenate([means, stds]).flatten()
print(means)
print(stds)
print(stats)
