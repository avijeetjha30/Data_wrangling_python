from pathlib import Path
import os
import shutil
import glob

# folder1 = glob.glob('data/*.jpg')
# folder2 = glob.glob('labels/*.txt')

# print(folder1)

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

# path1 = os.path.join('labels')
# path2 = os.path.join(BASE_DIR,'labels')
# print(path2)

# for j in os.listdir('labels'):
#     print(j)
# for i in os.listdir(path2):
#     print(i)


try:
      
    # creating a folder named label_txt
    if not os.path.exists('label_txt1'):
        os.makedirs('label_txt1')
        print("file creates")
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
                

def get_frame_name():
    # os.chdir('data')
    frame_folder_name = 'datasets/images/0cccoco'
    label_folder_name = 'datasets/labels/train'
    for frame in os.listdir(frame_folder_name):
        img_name, img_extention = os.path.splitext(frame)
        # print(type(img_name))
        for label in os.listdir(label_folder_name):
            # print(label)
            # label_name, label_extention = os.path.splittext(label)
            if img_name in label:
                src = os.path.join(label_folder_name,img_name+".txt")
                dst = os.path.join('label_txt1',img_name+".txt")
                shutil.move(src, dst)
            else:
                continue


get_frame_name()

