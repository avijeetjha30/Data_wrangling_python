import os
import shutil
import glob

try:
    if not os.path.exists('img_frame1'):
        os.makedirs('img_frame1')
except OSError:
    print("Error: Creating directory of data")

total_img = glob.glob('img_frame/*.jpg')
for frames in total_img:
    indx = total_img.index(frames)
    if (indx == 0):
        continue
    elif (indx%6 == 0):
        frame = frames.split('/')
        src = os.path.join('img_frame',frame[-1])
        dst = os.path.join('img_frame1',frame[-1])
        shutil.move(src, dst)
    else:
        continue

