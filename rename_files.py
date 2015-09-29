import os
#os module
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/Judy/Documents/Coding/Tutorials/Udacity/Programming Foundations w Python/prank")
    print(file_list)
rename_files()
