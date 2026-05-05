import cv2
import os

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False



def Image_folder_processing():
    file_templates = []
    for file in os.listdir("Kirby_images"):
        if file.endswith(".png"): # Only pulling png images

            image = cv2.imread(os.path.join("Kirby_images", file), 0)

            file_templates.append(image)

    return file_templates

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break











cv2.destroyWindow("preview")
vc.release()