import os
import cv2
import numpy as np
import pandas as pd
import csv
import re

# provide video path here
# ex: '/Users/erica/Desktop/Daffodil_1.mov'
video_path = '../videos/'

# provide path to save video frames here
# ex: '/Users/erica/Desktop/images'
frame_path = '../images/'

fv_path = '../fv_CSVs/'
norm_path = '../fv_norm_CSVs/'

for directory in [video_path, frame_path, fv_path, norm_path]:
    if not os.path.exists(directory):
        os.makedirs(directory)

for video in os.scandir(video_path):
    print(video.name)
    cap = cv2.VideoCapture(video_path + video.name)

    if (cap.isOpened() == False) :
     print ("Error opening video stream or file")

    success, frame = cap.read()
    count = 0

    img_dir = frame_path + video.name[0:-4] + '_images'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    while success:
        count += 1
         # 1 frame per second
        cap.set(cv2.CAP_PROP_POS_MSEC,(count * 1000))
        success, frame = cap.read()
         # only save nonempty frames
        if np.shape(frame) != ():
         				# "../images/Daffodil_1_images/"  # "Daffodil_1_%d.jpg"
            cv2.imwrite(os.path.join(img_dir + '/', (video.name[0:-4] + '_%d.jpg') %(count * 1000)), frame)
            # status = cv2.imwrite(os.path.join(img_dir + '/', (video.name[0:-4] + '_%d.jpg') %(count * 1000)), frame)
            # print(status)
        # keyboard exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

    cap.release()
    cv2.destroyAllWindows()

    # fps = cap.get(cv2.CAP_PROP_FPS)
    # print(fps)

def imgs_to_csv(img_path, img_dir, csv_path):
    '''creates a feature vector csv from a directory of images'''
    # csv_file = path + '_fv.csv'
    print('creating feature vector csv for ', img_path)
    images = os.listdir(img_path)
    img_fv = np.array(list(map(lambda x: img_to_feat_vec(img_path + '/' + x), images)))
    save_path = img_path.replace(img_dir, csv_path)
    # print(save_path)
    save_path = save_path[0:-6]
    # print(save_path)
    (pd.DataFrame(data = img_fv, index = images)).to_csv(save_path + 'fv.csv', header = False)

def img_to_feat_vec(img_name):
    '''converts an image to a feature vector'''
    img = cv2.imread(img_name) # STORED Blue | Green | Red
    # next two lines are standard deviation and variance, can comment one of them when needed
    (means, stds) = cv2.meanStdDev(img)
    stats = np.concatenate([means, stds, np.square(stds)]).flatten()
    return stats

def normalize(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)


# get list of all image directories from each video
img_dirs = list(filter(lambda x: x.endswith('images'), [x[0] for x in os.walk(frame_path)]))
for x in img_dirs:
    imgs_to_csv(x, frame_path, fv_path)

for inputCSV in os.scandir(fv_path):

    with open(inputCSV, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        matrix = []
        for row in reader:
            row = np.array(list(row))
            matrix.append(row)
        matrix = np.vstack(matrix)  # multidimensional nparray
        matrix = matrix.T
        data_categories = matrix.shape[0]

        img_names = np.array(matrix[0])
        i = 1 # iteration over rows
        for row in matrix[1:]: # skip first row of matrix are the names of images
            row = row.astype(np.float)
            max_val = np.max(row)
            min_val = np.min(row)
            if max_val != min_val:
                for j in range(len(row)):
                    x = row[j]
                    row[j] = normalize(x, min_val, max_val)
                    j += 1
            else:
                row[:] = 0.5
            matrix[i] = row # overwrite matrix elems with normalized values
            i += 1 

        # matrix = matrix.T
        (pd.DataFrame(data = matrix[1:].T, index = img_names)).to_csv(norm_path + inputCSV.name[0:-4] + '_norm.csv', header = False)
        # np.savetxt(path + '/' + inputCSV.name[0:-4] + '_norm.csv', matrix, delimiter = ',', fmt = '%s')
