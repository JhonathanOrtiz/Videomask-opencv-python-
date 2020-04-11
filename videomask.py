import numpy as np
import cv2


#Define some varible, will need it

pts=[]

drawing = True
counts = 0

#mouse_track function will help to read de mouse click into the video screen
def mouse_track(event, x, y, flags, params):
    
    global pts, drawing, counts

#When de user click append to a list the coordinates    
    if event == cv2.EVENT_LBUTTONDOWN and drawing == True:
        counts +=1
        pts.append((x,y))
        print(pts)
        
cap = cv2.VideoCapture(0)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse_track)       



while True:

#Initialize the video
    
     _, frame = cap.read()
    
#Create de mask
     mask = np.zeros(frame.shape[:-1], dtype = np.uint8)

     if (len(pts)) > 0:
        
#Create a polygone over the select area
        cv2.fillPoly(mask, np.array([pts]), (255,255,255))

#Apply and operation with the frames 
     new_video = cv2.bitwise_and(frame, frame, mask=mask)
     cv2.imshow("Frame", frame)
     cv2.imshow("mask", mask)
     cv2.imshow("new_video", new_video)
    
     if cv2.waitKey(1) and 0xFF == ord('s'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
  
           
        
  
        
    
            
        
        





    
