import cv2
import os
import numpy as np


global Standard_grid_size
Standard_grid_size = (100,100)
# Load and process templates
templates = []
for file in os.listdir("Kirby_images"):
    if file.endswith(".png"):
        img = cv2.imread(os.path.join("Kirby_images", file))
        
        templates.append(img)


cap = cv2.VideoCapture(0)

if cap.isOpened():
    rval, frame = cap.read()
else:
    print("Error! First frame could not be retrieved")

class template:
    def __init__(self, gray, blur, edge, thresh):
        self.gray = gray
        self.blur = blur
        self.edge = edge
        self.thresh = thresh



def frame_equalizer(image):
    '''
    This function takes the current recorded frame and grayscales/edgeblurs it for easier detection.
    Not directly called in main but used in other key functions.
    '''
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # First step is grayscaling the frame
    blur = cv2.GaussianBlur(grayscale, (5, 5), 0)       # Then we apply gaussian blur...
    edge = cv2.Canny(blur, 50, 150)                   # Next is blur
    threshold = cv2.adaptiveThreshold(
        blur,
        255,    # Max color value
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2,
    )
    return grayscale, blur, edge, threshold


rows = []
for i,t in enumerate(templates):
    
    gray, blur, edge, threshold = frame_equalizer(t)
    threshold = cv2.resize(threshold, Standard_grid_size)
    t = template(gray, blur, edge, threshold)



    
    rows.append(threshold)   # This is for debugging your TEMPLATE images


while rval:

    grid = np.hstack(rows)
    cv2.imshow("all thresholds", grid)          # Threshold template image viewing


    cv2.imshow("preview", frame)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break


if cv2.waitKey(1) & 0xFF == 27:
    pass

cap.release()
cv2.destroyAllWindows()