# Write Python code here 
# import the necessary packages 
import cv2 
import argparse
import pandas as pd
  
def shape_selection(event, x, y, flags, param): 
    # grab references to the global variables 
    global ref_point, crop 
  
    # if the left mouse button was clicked, record the starting 
    # (x, y) coordinates and indicate that cropping is being performed 
    if event == cv2.EVENT_LBUTTONDOWN: 
        ref_point = [(x, y)] 
  
    # check to see if the left mouse button was released 
    elif event == cv2.EVENT_LBUTTONUP: 
        # record the ending (x, y) coordinates and indicate that 
        # the cropping operation is finished 
        ref_point.append((x, y)) 
  
        # draw a rectangle around the region of interest 
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2) 
        cv2.imshow("image", image) 

def convert_ref_points_to_box_FastRCNN(ref_point, width, height):
    x_min = min(ref_point[0][0], ref_point[1][0])
    y_min = min(ref_point[0][1], ref_point[1][1])
    x_max = max(ref_point[0][0], ref_point[1][0])
    y_max = max(ref_point[0][1], ref_point[1][1])

    # ensure box is within image
    x_min = max(x_min, 0)
    x_max = min(x_max, width-1)
    y_min = max(y_min, 0)
    y_max = min(y_max, height-1)
    
    return x_min, x_max, y_min, y_max

def save_box_to_file(box_data, image_name, outputfile):
    f = open(outputfile, "a")
    x_min, x_max, y_min, y_max, width, height = box_data
    line = "{}, {}, {}, {}, {}, {}, {}\n".format(image_name, x_min, x_max, y_min, y_max, width, height)
    f.write(line)
    f.close()

if __name__ == "__main__":
    # now let's initialize the list of reference point 
    ref_point = [] 
    crop = False

    # construct the argument parser and parse the arguments 
    ap = argparse.ArgumentParser() 
    ap.add_argument("-out", "--outputfile", required = True, help ="Path to output file")
    ap.add_argument("-i", "--image", required = True, help ="Path to the image")
    args = vars(ap.parse_args())

    # load the image, clone it, and setup the mouse callback function
    image_name = args["image"]
    image = cv2.imread(args["image"]) 
    clone = image.copy() 
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", shape_selection)

    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    outputfile = args["outputfile"]

    # keep looping until the 'q' key is pressed 
    while True: 
        # display the image and wait for a keypress 
        cv2.imshow("image", image) 
        key = cv2.waitKey(1) & 0xFF

        # press 'r' to reset the window 
        if key == ord("r"): 
            image = clone.copy() 

        # if the 'q' key is pressed, break from the loop 
        elif key == ord("q"): 
            break

    if len(ref_point) == 2:
        x_min, x_max, y_min, y_max = convert_ref_points_to_box_FastRCNN(ref_point, width, height)
        box_data = [x_min, x_max, y_min, y_max, width, height]
        save_box_to_file(box_data, image_name, outputfile)
        
    # close all open windows 
    cv2.destroyAllWindows()

    # df = pd.read_csv(outputfile, index_col=0)
    # print(df.loc["Desktop/panda.jpg"])
    # print(df)
