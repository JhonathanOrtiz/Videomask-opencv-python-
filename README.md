# Videomask-opencv-python-
That's my firts computer vision project, i accept suggestions


This is a little project obout computer vision and python whith open-cv librarie.

The project consist in with a webcam video in realtime create a mask and only view the selected screen zone. For this i define a function to do actions in consecuences of event mouse in the screen video for example "A click" or a mouse.


To visualize only de the selected area i create a black image with the numpy function zeros with a video frame shape so, when i push left click and move the the mouse i create a white shape in a mask image, with this image and the video frames i use a bitwise operator AND, black is 0 and white 255 if we apply AND operation to the both images, When we apply and operation if we have a zero the result is zero

true table:

    A     B    TARGET  
    0     0      0
    0     1      0
    1     0      0
    1     1      1
    
    
If the pixel is black the value is 0, as you can see if one of the pixel values is 0 (BLACK) the result will 0 (BLACK) so, we draw a white shape en some scree zone (255) if we apply the and we only will see the screen zone where the white shape are. 255 and Xvalue != 0 is equal to XValue != 0
