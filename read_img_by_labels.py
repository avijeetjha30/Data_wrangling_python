import os
import shutil

try:
      
    # creating a folder named label_txt
    if not os.path.exists('img_frame1'):
        os.makedirs('img_frame1')
        print("file creates")
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
                

def get_frame_name():
    # os.chdir('data')
    frame_folder_name = 'datasets/images/0cccoco'
    label_folder_name = 'datasets/images/label_txt12'
    for label in os.listdir(label_folder_name):
        label_name, label_extention = os.path.splitext(label)
        # print(type(label_name))
        for frame in os.listdir(frame_folder_name):
            if label_name in frame:
                frame_name, frame_extention = os.path.splitext(frame)
                if frame_extention in '.jpg':
                    src = os.path.join(frame_folder_name,label_name+".jpg")
                    dst = os.path.join('img_frame1',label_name+".jpg")
                    shutil.copy(src, dst)
                elif frame_extention in '.png':
                    src = os.path.join(frame_folder_name,label_name+".png")
                    dst = os.path.join('img_frame1',label_name+".png")
                    shutil.copy(src, dst)
                else:
                    continue
            else:
                continue


get_frame_name()