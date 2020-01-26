import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# replace path, rerun fv_csv_builder.py to get variance in feature vector
df = pd.read_csv('path/Gom_1_images_fv_norm.csv', header = None)
df = df.rename(columns = {df.columns[0]: 'img name', df.columns[1]: 'B mean', df.columns[2]: 'G mean', df.columns[3]: 'R mean', df.columns[4]: 'B sd', df.columns[5]: 'G sd', df.columns[6]: 'R sd', df.columns[7]: 'B var', df.columns[8]: 'G var', df.columns[9]: 'R var', df.columns[10]: 'label'})
df['label'] = df['label'].astype('category')
cdict = {'N' : 'xkcd:ocean blue', 'W' : 'xkcd:seaweed'}
''' Graph in 2D '''
fig, ax = plt.subplots()
for category in pd.unique(df['label']):
	i = np.where(df.label == category)
	ax.scatter(df['B var'].iloc[i], df['G var'].iloc[i], c = cdict[category], label = category)
	# ax.scatter(i, df['B var'].iloc[i], c = cdict[category], label = category)
plt.xlabel('Blue Pixel Variance')
# plt.xlabel('Time')
plt.ylabel('Green Pixel Variance')
ax.legend()
plt.show()

''' Example of Graph in 3D '''
# UNCOMMENT TO PLOT
# fig = plt.figure()
# ax = plt.axes(projection = '3d')
# for category in pd.unique(df['label']):
# 	i = np.where(df.label == category)
# 	ax.scatter3D(i, df['B sd'].iloc[i], df['G sd'].iloc[i], c = cdict[category], label = category)
# ax.set_xlabel('Time')
# ax.set_ylabel('Blue Pixel Standard Deviation')
# ax.set_zlabel('Green Pixel Standard Deviation')
# ax.legend()
# plt.show()
