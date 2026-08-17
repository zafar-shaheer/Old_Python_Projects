"""
Camera Video Recording Program

This Python program was created in 2019 using OpenCV (cv2) to access
a selected camera device, capture video frames, display the live
camera feed, and save the recorded footage as a video file.

The program takes user input for the camera device, the location
where the video should be saved, and the name of the output file.
It then records the camera feed and saves the footage in AVI format.

Built with:
- Python
- OpenCV (cv2)
"""

import cv2
import time

#Enter the number of the camera to be accessed
cam_num = int(input("Enter the Camera number to be accessed: "))
cap = cv2.VideoCapture(cam_num)

#Enter the address where the file musst be saved
file_address_initial = input('Insert the Address to store the file: ')
file_address_final = file_address_initial.replace("\\","/") #this changes the bck slash to forward slash

#Enters the name of the file
file_name = input('Enter the file name: ')
complete_address = file_address_final + "/" + file_name + ".avi" #Final adderess of the file and the name of the file and the format

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(complete_address,fourcc, 20.0, (640,480))

print("Opening camera..\nPlease wait..")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

print("Camera Closed..\nThankyou..")

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

time.sleep(5)
