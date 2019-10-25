# 10/14/19 Mon
# Erica Zhang
import cv2
import os
import numpy as np

#provide local video path here
cap = cv2.VideoCapture('/Users/erica/Desktop/Daffodil_1.mov')

if (cap.isOpened() == False) :
 print ("Error opening video stream or file")

success, frame = cap.read()
count = 0
#provide path to save video frames here
path = '/Users/erica/Desktop/images'
while success:
     count += 1
     # 1 frame per second
     cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
     success, frame = cap.read()
     # only save nonempty frames
     if np.shape(frame) != ():
         cv2.imwrite(os.path.join(path, "Daffodil_1_%d_ms.jpg" % (count * 1000)), frame)
     # keyboard exit
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()

#fps = cap.get(cv2.CAP_PROP_FPS)
#print (fps)
