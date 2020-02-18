import os

video_path = '../Pinball'
count = 1
for video in os.scandir(video_path):
	os.rename(os.path.join(video_path, video), 
			  os.path.join(video_path, video_path[3:] + '_%d.mov' %(count)))
	count += 1