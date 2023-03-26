import os


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
                    if lst_data[0] != '2' and lst_data[0] != '1':
                        # lst_data[0] = '2'
                        str_data = ' '.join(lst_data)
                        f.writelines(str_data)
                    # print(lst_data[0])
                
            f.close()

folder_name = "data"
change_class(folder_name)
