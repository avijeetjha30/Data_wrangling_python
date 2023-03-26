import os

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# file1 = open("frame.txt",'r+')
# content = file1.readlines()
# # print(content)
# file1.seek(0)
# file1.truncate(0)
# for i in content:
#     # lst = i.split(' ')
#     # print("##############",lst)
#     # if lst[0] == '1':
#     #     lst[0] = '3'
#     # print(lst)
#     if '1 ' in i:
#         i = i.replace('1 ', '3 ')
#     print(i)
#     file1.write(i)
# file1.close()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def change_class(folder_name):

    for file in os.listdir(folder_name):
        if file.endswith('.txt'):
            file_path = f"{folder_name}/{file}"

            with open(file_path, 'r+') as f:
                # print(f.read())
                content_lst = f.readlines()
                f.seek(0)
                f.truncate(0)
                for data in content_lst:
                    lst_data = data.split(' ')
                    if lst_data[0] == '0':
                        lst_data[0] = '2'
                    str_data = ' '.join(lst_data)
                    f.writelines(str_data)
                
            f.close()

folder_name = "all_annotations/datasets/data123/train_txt"
change_class(folder_name)
