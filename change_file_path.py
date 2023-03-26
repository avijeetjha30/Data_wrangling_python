import uuid
import os

os.chdir('img_frame')

for f in os.listdir():
    x = str(uuid.uuid4().hex)
    file_name, file_ext = os.path.splitext(f)
    # print(file_name,"##", file_ext)

    new_name = '{}{}'.format(x,file_ext)
    # print(new_name)
    
    os.rename(f, new_name)
