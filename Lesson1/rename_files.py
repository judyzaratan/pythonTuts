import os
#os module
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/prank")
    print(file_list)

    #gets current working directory
    saved_path = os.getcwd()
    print(saved_path)

    #changes directory
    os.chdir("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #translate removes numbers in a string

    os.chdir(saved_path)

rename_files()

#Exceptions
#if it tries to rename a file that does not exist or rename a file that already has the same name
# it will throw an exception
