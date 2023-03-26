from base64 import encode
import glob
import os

#os.chdir(r'..//dataset/labels/val')
#my_files = glob.glob('*.txt')
classes = ['0','1','2']

all_files_path = glob.glob(r'val2017 (copy)/*.txt')
#print(all_files_path)
c=0

for txt_file in all_files_path:
    #print(txt_file)

    with open(txt_file,'r+',encoding='utf-8') as file:
        # f2 = open('val2017 (copy)/new_file.txt','w+', encoding='utf-8')
        data = file.readlines()
        if not data:
            os.remove(txt_file)

        # for s_line in data:
        #     if len(data) == 0:

            # if s_line[0] in classes:
            #     f2.write(s_line)
            # else:
            #     continue
                # if s_line[0]=='3':

                #     mydata = s_line.split(' ')
                #     mydata[0] = '1'
                #     mydata = " ".join(str(item) for item in mydata)
                #     f2.write(mydata)
                #     print(mydata)

                # elif s_line[0]=='10':
                #     mydata = s_line.split(' ')
                #     mydata[0] = '2'
                #     mydata = " ".join(str(item) for item in mydata)
                #     f2.write(mydata)
                #     print(mydata)
                # elif s_line[0] == '0':
                #     mydata = s_line
                #     f2.write(mydata)
                #     print(mydata)
            

                #print(s_line[0] , end = ' ')
               
                
                
        c = c+1
        print(c ,end = '    ')
        # print('##########################')



    
            #mydata = s_line.split(' ')
            #mydata[0] = 10
            

            #mydata = " ".join(str(item) for item in mydata)
        # os.remove(txt_file)
        # os.rename('val2017 (copy)/new_file.txt',txt_file)    
        #     #file.write(mydata)
            #print(s_line)
        #f2 = open('..//dataset/labels/vald/new_file.txt','w+', encoding='utf-8')
        #f2.write(mydata)
        
        
        # f2.close()
    file.close()

    




