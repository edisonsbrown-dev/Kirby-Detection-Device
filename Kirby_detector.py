import os
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

root_dir = r"C:\Users\ediso\Downloads\Python Projects\Kirby project\kirby_images" # Raw string
target_extension = ".png"



def Image_folder_processing():
    file_templates = []
    for root, dirs, files in os.walk(root_dir): # os.walk will go into subfolders to find every target within the directory
        for file in files:
            if file.endswith(target_extension): # Only pulling png images

                image = cv2.imread(os.path.join(root_dir, file), 1) # 1 allows them to load in color

                file_templates.append(image)

    return file_templates

def Image_pattern_scoring():
    print("")


rval = True

if vc.isOpened(): # try to get the first frame of camera
    rval, frame = vc.read()

    for file in Image_folder_processing():
        cv2.imshow(f"file:{file}", file)

    while rval:

        
       



        cv2.imshow("preview", frame)
        rval, frame = vc.read()



        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

else:
    rval = False
