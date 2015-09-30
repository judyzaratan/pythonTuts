import os
#os module
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/prank")
    print(saved_path)

    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #translate removes numbers in a string

    os.chdir(saved_path)

rename_files()
