"""
Video Frame Extraction Program

This Python program was created in 2020 to extract individual frames
from a video file.

The program uses OpenCV to read a video frame by frame, resize each
frame to 1280x720, and save the frames as sequential JPEG images.
The user can specify the input video and the location where the
extracted frames should be saved.

Built with:
- Python
- OpenCV (cv2)
"""

import cv2

file_name = input("Enter the file name(with extension): ")
file_name = file_name.replace("\\","/") #this changes the bck slash to forward slash

file_path = input("Enter thee path of the file: ")
file_path = file_path.replace("\\","/") #this changes the bck slash to forward slash

path = file_path + file_name

vidcap = cv2.VideoCapture(path)
success, image = vidcap.read()

saving_path = input("Enter the path of the place to enter the data set: ")
saving_path = saving_path.replace("\\","/") #this changes the bck slash to forward slash

i = 1
while (success):
    save_Path = saving_path + str(i) + ".jpg"
    image = cv2.resize(image, (1280, 720))
    cv2.imwrite(save_Path, image)
    success, image = vidcap.read()
    print("Read a new frame:", success)
    if success:
        print("saving " + " image= ", i)
    else:
        break
    i += 1

vidcap.release()
cv2.destroyAllWindows()



