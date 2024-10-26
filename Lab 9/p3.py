import os
path=input("Enter path")


for item in os.listdir(path) :
       print(path+item)