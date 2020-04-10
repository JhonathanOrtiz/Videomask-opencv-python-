import numpy as np
import cv2


#Define some varible, will need it

point1=()
point2=()
drawing = False

#mouse_track function will help to read de mouse click into the video screen
def mouse_track(event, x, y, flags, params):
    
    global point1, point2, drawing

#if the left button is clicked over de screen store un point1 the coordinates     
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if drawing is False:

            drawing = True
            point1 =(x,y)
            print(point1)
        else:
            drawing = False      
# if the mouse is move it over the screen and we are drawing store the coordinates
    elif event == cv2.EVENT_MOUSEMOVE:
         if drawing is True:
            point2 = (x,y)
            print(point2)
    
#Initialize the video
cap = cv2.VideoCapture(0)
cv2.namedWindow('Frame')

#Capture the mouse event
cv2.setMouseCallback("Frame", mouse_track)
while True:

#Initialize the video    
    _, frame = cap.read()
#Create de mask
    mask = np.zeros(frame.shape[:-1], dtype = np.uint8)

    if point1 and point2:
        
#Create the rectangle over the select area
        cv2.rectangle(mask, point1, point2, (255,255,255), -1)

#Apply and operation with the frames 
    new_video = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("new_video", new_video)
    
    if cv2.waitKey(1) and 0xFF == ord('s'):
        break
    
cap.release()
cv2.destroyAllWindows()
