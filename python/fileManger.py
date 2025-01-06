import os
import shutil #use for transfeering file from one place to another


path=input("enter your path")
files=os.listdir(path)
for i in files:
    #print(i)
    filename,extenstion=os.path.splitext(i)
    #print(filename)
    #print(extenstion)
    
    #removing . from extention for creating folder for each type of extenstion .mp4 ke liye mp4 naam ka folder
    extenstion_1=extenstion[1:]
    
    folder_path=path+"\\"+extenstion_1
    #checking is folder already exixt or not
    if os.path.exists(folder_path):
        #if folder exixt then move file to that folder
        shutil.move(path+"\\"+i,folder_path)  #folder_path = os.path.join(path, extension_1) ||we can also use this to concat path
        
    else:
        #if folder not exixt then create folder and move file to that folder
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i,folder_path)
        
            
        
        
    
    
    

    