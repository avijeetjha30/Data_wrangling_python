import os

os.chdir('dataset/images/train')

count = count2 =  0
for frame in os.listdir():
    frame_name, frame_ext = os.path.splitext(frame)
    if(frame_ext == '.jpg'):
        count += 1
    if(frame_name == '.png'):
        count2 += 1
    else:
        continue

print(count,count2)