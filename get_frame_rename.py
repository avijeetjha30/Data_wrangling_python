import cv2
import os
import uuid
  
# Read the video from specified path
cam = cv2.VideoCapture("ds1.mp4")
  
try:
      
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
    print(frame)
    if ret:
        file_ext = '.jpg'

        # create uuid
        x = str(uuid.uuid4().hex)
        name = './data/' + x + '.jpg'

        # writing the extracted images
        cv2.imwrite(name, frame)

    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()