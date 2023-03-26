import uuid
import os

frame_folder_name = 'all_annotations/stanford/images'
label_folder_name = 'all_annotations/stanford/labels'

l = []

for frame in os.listdir(frame_folder_name):
    x = str(uuid.uuid4().hex)
    frame_name, frame_ext = os.path.splitext(frame)
    for label in os.listdir(label_folder_name):
        label_name, label_ext = os.path.splitext(label)
        if frame_name == label_name:
            frame_rename = f'{frame_folder_name}/{x}{frame_ext}'
            label_rename = f'{label_folder_name}/{x}{label_ext}'
            os.rename(f'{frame_folder_name}/{frame}', frame_rename)
            os.rename(f'{label_folder_name}/{label}', label_rename)
            # print(label)
            # print(frame)
        else:
            continue