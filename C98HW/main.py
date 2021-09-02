import os
import shutil

path1 = input("Enter the first file you would like to switch: ")
path2 = input("Enter the second file you would like to switch: ")

with open(path1, "r") as a:
    data_1 = a.read()
    
with open(path2, "r") as b:
    data_2 = b.read()
    
with open(path1, "w") as a:
    a.write(data_2)    

with open(path2, "w") as b:
    b.write(data_1)    