import numpy as np
import csv

# reads in a csv with feature vectors to normalize
# creates a new csv file with the normalized feature vectors
# normalization fcn so far is (x - min_val) / (max_val - min_val)

fname = 'path/test.csv'

def open_csv(filename):
	lst = []
	with open(filename, 'r') as f:
		readCSV = csv.reader(f, delimiter = ',')
		for row in readCSV:
			lst.append(row) # row[-1:] ignores file path, the first element for testing purposes
		return lst

def normalize(x, min_val, max_val):
	return ((x - min_val) / (max_val - min_val))

features_lst = np.array(open_csv(fname))
features_lst = features_lst.astype(np.float)
# num_cols = features_lst.shape[1]
i = 0
# print(features_lst)

for column in features_lst.T:
	# stats: max, min; (x - min) / (max - min)

	# column = [int(c) for c in column]
	max_val = np.max(column)
	# print(max_val)

	min_val = np.min(column)
	# print(min_val)

	# currently leaves a column be if it has the same value
	if max_val != min_val:
	# print(features_lst[:, i])
		features_lst[:, i] = [normalize(x, min_val, max_val) for x in column]
	# print(features_lst[:, i])
	i = i + 1

# csvwriter = csv.writer(open(fname[0:-4] + '_norm.csv', 'w'))
# csvwriter.writerow(features_lst)

# potential shortcut to avoid csvwriter
np.savetxt(fname[0:-4] + '_norm.csv', features_lst, delimiter = ',')