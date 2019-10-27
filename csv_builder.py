import cv2
import os
import numpy as np

#provide local video path here

vidname = 'Grommet_1'
path = '../whale_videos/' + vidname + '_images'

cap = cv2.VideoCapture('../whale_videos/' + vidname + '.mov')

if (cap.isOpened() == False) :
    print ("Error opening video stream or file")

success, frame = cap.read()
count = 0
csvtext = ''

while success:
    count += 1
     # 1 frame per second
    cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
    success, frame = cap.read()
     # only save nonempty frames
    if np.shape(frame) != ():
        wname = path + '/' + vidname + "_%08d.jpg" % (count * 1000)
        cv2.imwrite(wname, frame)
        csvtext += wname + ', '
        csvtext += '\n'
     # keyboard exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

f = open('../whale_videos/' + vidname + '.csv', 'w+')
f.write(csvtext)




cap.release()
cv2.destroyAllWindows()

#fps = cap.get(cv2.CAP_PROP_FPS)
#print (fps)
