import os

def recursive_ls(path):
    print(path)             #print path 
    if os.path.isdir(path):  ##check pth exist or not 
        for item in os.listdir(path):     ##This function returns a list of names of the entries in the given directory.
            recursive_ls(path + "/" + item)  

recursive_ls(input())     ##user need to give input

