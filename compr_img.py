import os
import sys
from PIL import Image

def compressMe(file):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	
	#Set quality equal to the % preferred quality. 85 is pretty good.
	picture.save("Compressed_"+file,"JPEG",optimize=True,quality=85) 
	
	newsize = os.stat(os.path.join(os.getcwd(),"Compressed_"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	return percent

def main():
	#finds present working dir
	pwd = os.getcwd()

	tot = 0
	num = 0
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			tot += compressMe(file)
	print "Average Compression: %d" % (float(tot)/num)
	print "Done"

if __name__ == "__main__":
	main()