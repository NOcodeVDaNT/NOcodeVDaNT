# # Open the file in read and write mode ('r+')
# file = open('sample.txt', 'r+')
# file.write("dahake")
# # Move the file pointer to the beginning to read the content
# file.seek(0)
# content = file.read()
# print(content)
# file.close()


import os

def create_file(filename):
    try:
        # Create a new file
        open(filename, 'x').close()
        print("file created succesfully")
    except FileExistsError:
        print("file already exists")
    except Exception as e:
        print("An error occurred: ", str(e))
        
        
        
def view_all_files():
    files=os.listdir() #os.listdir(path='directory_path') || Defaults to the current working directory ('.') if not provided.

    if not files:
        print("No files found")
    else:
        for file in files:
            print(file)
            
            

def delete_file(filename):
    try:
        os.remove(filename)
        print("file deleted succesfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured")
        
        
        
def update_file(filename):
    try:
        with open(filename, 'r+') as file: #The with open() statement in Python is a convenient and preferred way to work with files. It ensures that files are properly closed after their operations dont have to be manually closed.


            content = file.read()
            file.seek(0)
            new_content = input("Enter new content: ")
            file.write(new_content)
            file.truncate() #The file.truncate() method in Python is used to resize the file to a specified size. If no size is specified, it truncates the file to the current position of the file pointer.
            print("file updated succesfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("error occurred: ", str(e))
        


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("error")
            
            
def write_file(filename):
    try:
        with open(filename, 'a') as file:  #a+ is to append in the file
            content = input("Enter content: ")
            file.write(content)
            print("file created succesfully")
    except Exception as e:
        print("error occurred: ", str(e))
            
            
def mian():
    while True:
        print("--------------------------------------GHOST FILE MANAGER APPLICATION--------------------------------------")
        print("1. create file")
        print("2. view all file")
        print("3. delete file")
        print("4. write file")
        print("5. update file")
        print("6. read file")
        print("7. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            file_name=input("enter file name:")
            create_file(file_name)
            
            
        elif choice == "2":
            view_all_files()
            
        elif choice == "3":
            file_name=input("enter file name:")
            delete_file(file_name)
            
            
        elif choice == "4":
            file_name=input("enter file name:")
            write_file(file_name)
            
        elif choice == "5":
            file_name=input("enter file name:")
            update_file(file_name)
            
        elif choice == "6":
            file_name=input("enter file name:")
            read_file(file_name)
            
        elif choice=="7":
            break
        else:
            print("invalid choice")
            
        print("\n\n\n\n\n\n")
            
            
            
mian()