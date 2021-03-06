import os
import numpy as np
import pandas as pd
import cv2

def img_dir_to_csv(path):
    '''creates a feature vector csv from a directory of images'''
    # csv_file = path + '_fv.csv'
    print('creating feature vector csv for ', path)
    images = os.listdir(path)
    img_fv = np.array(list(map(lambda x: img_to_feat_vec(path + '/' + x), images)))
    (pd.DataFrame(data = img_fv, index = images)).to_csv(path + '_fv.csv', header = False)

def img_to_feat_vec(img_name):
    '''converts an image to a feature vector'''
    img = cv2.imread(img_name) # STORED Blue | Green | Red
    (means, stds) = cv2.meanStdDev(img)
    stats = np.concatenate([means, stds, np.square(stds)]).flatten()
    return stats

# get list of all image directories
img_dir = list(filter(lambda x: x.endswith('images'), [x[0] for x in os.walk('.')]))

for x in img_dir:
    img_dir_to_csv(x)
