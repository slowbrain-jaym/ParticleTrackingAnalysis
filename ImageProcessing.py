
import cv2
import pandas as pd 
import numpy as np 

target_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\GlassTest8\\"
image_name = "GlassTest"
first_frame = 8000001
final_frame = 8000430

particle_ID = 2
file_name = "GlassTest8" + str(particle_ID)


frame_rate = 1000
focus_jet = 6
save_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\RawTrackResults\\"


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
        mouse_release = True

    #if event == cv2.EVENT_LBUTTONUP:
        

frames = np.arange(first_frame,final_frame,1)
#frames = np.nditer(frames, flags=['f_index'])
tracking = True
i=0
while tracking:
    try:
        i = i+1
        frame = frames[i]
    except StopIteration:
        tracking = False
        break
    filename = target_folder + image_name + str(frame) + ".tif"
    image = cv2.imread(filename)
    try:
        clone = image.copy()
    except AttributeError:
        continue
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    # keep looping until the 'q' key is pressed
    while True:
       # global mouse_release, refPt
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        if mouse_release:
            frame_nums.append(frame)
            x_coords.append(refPt[0])
            y_coords.append(refPt[1])
            break

        if key == ord("n"):
            break

        if key == ord("b"):
            i = i-2
            break

        if key == ord("q"):
            tracking = False
            break

    cv2.destroyAllWindows()


df = pd.DataFrame({"Frame Number":frame_nums,"x position":x_coords,"y position":y_coords})
df["particle ID"] = particle_ID
df["frame rate"] = frame_rate
df["jet in focus"] = focus_jet
df.to_csv(save_folder+file_name+".csv")
