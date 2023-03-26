import os
import shutil


try:
    if not os.path.exists('img_frame'):
        os.makedirs('img_frame')
    if not os.path.exists('label_txt'):
        os.makedirs('label_txt')
except OSError:
    print("Error: Creating directory of data")


def separat_img_txt(folder_name):
    for f in os.listdir(folder_name):
        name, extention = os.path.splitext(f)
        if extention in ".jpg":
            src = os.path.join(folder_name,name+".jpg")
            dst = os.path.join('img_frame',name+".jpg")
            shutil.copy(src, dst)
        
        if extention in ".png":
            src = os.path.join(folder_name,name+".png")
            dst = os.path.join('img_frame',name+".png")
            shutil.copy(src, dst)

        elif extention in ".txt":
            src = os.path.join(folder_name,name+".txt")
            dst = os.path.join('label_txt',name+".txt")
            shutil.copy(src, dst)
        else:
            continue

folder_name= 'all_annotations/datasets/kg_d_dataset_png_jpg'
separat_img_txt(folder_name)