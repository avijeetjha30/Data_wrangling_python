import os


def change_class(folder_name):
    count = 0
    for file in os.listdir(folder_name):
        if file.endswith('.txt'):
            
            file_path = f"{folder_name}/{file}"

            with open(file_path, 'r+') as f:
                # print(f.read())
                content_lst = f.readlines()
                # if not content_lst:
                # #     # os.remove(file_path)
                # #     # count += 1
                # #     print(file_path)
                #         continue
                # else:
                #     print(file_path)
                
                # f.seek(0)
                # f.truncate(0)
                for data in content_lst:
                    if data.startswith('0 '):
                        # f.write(data)
                        continue
                    elif data.startswith('2 '):
                        # data1 = data.replace('1 ', '0 ')
                        # f.write(data1)
                        continue
                    elif data.startswith('1 '):
                        # data1 = data.replace('3 ', '1 ')
                        # f.write(data1)
                        continue
                        # print(file_path)
                    else:
                        # continue
                        print(file_path)
                #     # if not data:
                #     #     count += 1
                #     # str_data = ' '.join(lst_data)
                #     # f.writelines(str_data)
                
            f.close()
    print(count)
folder_name = "VisDrone_1000img/train/labels"
change_class(folder_name)