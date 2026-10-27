from pathlib import Path
import shutil

def create_folder():
    try:
        name=input("please tell your folder name : -")
        p=Path(name)
        p.mkdir()
        print("folder ceated successfully")
    except Exception as err:
        print(f"sorry as error occuredd as {err}")

def read_file_folder(): 
    p=Path("")
    items=list(p.rglob('*'))
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")

def update_folder():
    try:
        read_file_folder()
        old_name=input("please tell which folder you you want to update : - ")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("please tell your new folder name : - ")
            new_p=Path(new_name)
            p.rename(new_p)
            print("your folder name is updated successfully")
        else:
            print("sorry no such folder exist")
    except Exception as err:
        print(f"An error occured as {err}")

import shutil
import os
from pathlib import Path

def delete_folder():
    try:
        read_file_folder()

        name = input("Please tell which folder you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_dir():

            def handle_error(func, path, exc_info):
                os.chmod(path, 0o777)
                func(path)

            shutil.rmtree(p, onerror=handle_error)

            print("Folder deleted successfully")

        else:
            print("No such folder exists")

    except PermissionError as err:
        print(f"Access denied: {err}")
        print("Check folder permissions or close programs using this folder.")

    except Exception as err:
        print(f"An error occurred: {err}")

def create_file():
    read_file_folder()
    try:
            name=input("please tell your file name : -")
            p=Path(name)
            if not p.exists():
                with open(name,"w") as fs:
                    data=input("write what you want in this file : - ")
                    fs.write(data)
                print("file ceated successfully")
            else:
                print("sorry this name file already exist")
    except Exception as err:
        print(f"An error occuredd as {err}")
    
def read_file():
    try: 
        read_file_folder()
        name=input("please tell your file name : -")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(name,"r") as fs:
                content=fs.read()
                print("your file content is : - ")
                print(content)
        else:
            print("sorry no such file exist")
    except Exception as err:
            print(f"An error occuredd as {err}")

def update_file():
    try:
        read_file_folder()
        name=input("please tell which file you you want to update : - ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Options")
            print("1. For renaming the file")
            print("2. For appending something in the file")
            print("3. For overwriting the file content")

            choice=int(input("tell your choice : - "))

            if choice==1:
                new_name=int(input("tell your new name with extension : - "))
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("your file name is changed successfully")
                else:
                    print("sorry this name aleady exist")

            if choice==2:
                with open(name,'a') as fs:
                    data=input("what you want to append : ")
                    fs.write(" "+ data)
                print("Data appended successfully")
            
            if choice==3:
                with open(name,'a') as fs:
                    data=input("what you want to overwrite : ")
                    fs.write(data)
                print("Data overwrite successfully")
    except Exception as err:
        print(f"An error occured as {err}")

def delete_file():
    try:
        read_file_folder()
        name=input("please tell which file you you want to delete : - ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deletedd successfully")
        else:
            print("no such file exist")
    except Exception as err:
             print(f"There was an error occured as {err}")
    
while True:
    print("Options : - ")

    print("1. Create a folder")
    print("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete the folder")
    print("5. Create a file")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. Exit the program")

    choice=int(input("please choose your option"))

    if choice==1:
        create_folder()

    if choice==2:
        read_file_folder()

    if choice==3:
        update_folder()

    if choice==4:
        delete_folder()

    if choice==5:
        create_file()

    if choice==6:
        read_file()

    if choice==7:
        update_file()

    if choice==8:
        delete_file()
