import cv2
import os
import numpy as np

# provide local video path here
video_path = '../Pinball/'
frame_path = '../images/'
label_path = '../labels/'

for directory in [frame_path, label_path]:
    if not os.path.exists(directory):
        os.makedirs(directory)

for video in os.scandir(video_path):
    cap = cv2.VideoCapture(video_path + video.name)

    if (cap.isOpened() == False) :
        print ("Error opening video stream or file")

    success, frame = cap.read()
    count = 0
    csvtext = ''

    img_dir = frame_path + video.name[0:-4] + '_images'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    while success:
        count += 1
         # 1 frame per second
        cap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        success, frame = cap.read()
         # only save nonempty frames
        if np.shape(frame) != ():
            wname = img_dir + '/' + video.name[0:-4] + "_%d.jpg" %(count * 1000)
            cv2.imwrite(wname, frame)
            csvtext += wname + ', '
            csvtext += '\n'
         # keyboard exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    f = open(label_path + video.name[0:-4] + '_labels.csv', 'w+')
    f.write(csvtext)

    cap.release()
    cv2.destroyAllWindows()

#fps = cap.get(cv2.CAP_PROP_FPS)
#print (fps)
