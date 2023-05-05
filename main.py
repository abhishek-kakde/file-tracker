# importing os and shutil module
import os, shutil
path = r'C:/Users/computer world/Desktop/New folder/'
filename = os.listdir(path)
folder_names = ['text','zip','doc']
for i in range(0,3):
    if not os.path.exists(path + folder_names[i]):
        os.makedirs(path+folder_names[i])
for file in filename:
    if '.txt' in file and not os.path.exists(path + 'text' + file):
        shutil.move(path+ file,path + 'text/'+ file)
    elif '.rar' in file and not os.path.exists(path + 'zip' + file):
        shutil.move(path+ file,path + 'zip/'+ file)
    elif '.docx' in file and not os.path.exists(path + 'doc'+file):
        shutil.move(path+ file,path + 'doc/'+ file)

