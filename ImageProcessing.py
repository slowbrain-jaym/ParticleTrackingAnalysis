
import cv2
import pandas as pd 
import numpy as np 

target_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\GlassTest4\\"
image_name = "GlassTest"
first_frame = 4000001
final_frame = 4000003

particle_ID = 0
frame_rate = 1500
focus_jet = 3
save_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\RawTrackResults\\"
file_name = "GlassTest4"

particle_ID = 0

frame_nums = []
x_coords = []
y_coords = []
refPt = []
mouse_release = False

def click_and_crop(event, x, y, flags, param):
    '''Function records location of left mouse click and reports when left mouse is released'''
    # grab references to the global variables
    global refPt, mouse_release
    mouse_release = False

    if event == cv2.EVENT_LBUTTONDOWN:
	    refPt = [x, y]

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_release = True


for i in np.arange(first_frame,final_frame,1):
    filename = target_folder + image_name + str(i) + ".tif"
    image = cv2.imread(filename)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    # keep looping until the 'q' key is pressed
    while True:
       # global mouse_release, refPt
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        if mouse_release:
            frame_nums.append(i)
            x_coords.append(refPt[0])
            y_coords.append(refPt[1])
            break

        if key == ord("n"):
            break
    cv2.destroyAllWindows()


df = pd.DataFrame({"Frame Number":frame_nums,"x position":x_coords,"y position":y_coords})
df["particle ID"] = particle_ID
df["frame rate"] = frame_rate
df["jet in focus"] = focus_jet
df.to_csv(save_folder+file_name+".csv")
