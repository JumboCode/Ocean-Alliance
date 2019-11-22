import csv
import re
import numpy as np

"""
This script takes in a path to a feature vector csv, and goes through each
columns of data (mean of Blue, mean of Green, mean of Red, std of Blue, std of
Green, std of red) and normalize the data, then output the normalized csv of
feature vectors
"""

inputCSV = '/Users/erica/Desktop/Daffodil_1_images_fv.csv'
def normalize(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)

with open(inputCSV, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader) #skip useless repetitive header data, fv to csv script could be
                # improved to avoid this issue
    matrix = []
    for row in reader:
        row = np.array(list(row))
        matrix.append(row)
    matrix = np.vstack(matrix)  # multidimensional nparray
    matrix = matrix.T
    data_categories = matrix.shape[0]

    i = 1 #iteration over rows
    for row in matrix[1:]: #skip first row of matrix are the names of images
        row = row.astype(np.float)
        max_val = np.max(row)
        min_val = np.min(row)
        if max_val != min_val:
            for j in range(len(row)):
                x = row[j]
                row[j] = normalize(x, min_val, max_val)
                j += 1
        matrix[i] = row #overwrite data
        i += 1

    matrix = matrix.T
    np.savetxt("/Users/erica/Desktop/Daffodil_1_images_fv_normalized.csv", matrix, delimiter=",", fmt='%s')

""" Potentially helpful test dummy csv_file
,1,2,3,4,5,6
a.jpg,1,2,3,4,5,6
b.jpg,7,8,9,10,11,12
c.jpg,13,14,15,16,17,18 """

"""  Potentially helpful test csv_file that resembles our test data
,157.84800720968366,121.32011477623458,96.8574274209105,40.75185778790517,47.73890739814047,59.59056649454756
Daffodil_1_00001000.jpg,157.84800720968366,121.32011477623458,96.8574274209105,40.75185778790517,47.73890739814047,59.59056649454756
Daffodil_1_00002000.jpg,83.893466796875,60.702920404128086,44.52061824845679,46.19905170686465,44.235795036998546,47.76748445213679
Daffodil_1_00003000.jpg,80.76267445505401,56.75182014371142,40.79349922839506,38.31016529851732,35.63443205159199,40.158716038930415
Daffodil_1_00004000.jpg,151.17220413773148,112.23720896026235,85.93518759645062,37.486679365855636,38.59213289451398,52.96467161516431
Daffodil_1_00005000.jpg,135.80757908950616,97.92763237847223,71.0721437355324,34.03592695281478,35.34852312470605,46.21803435694151"""
