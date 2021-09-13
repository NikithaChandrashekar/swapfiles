import os
import shutil 
def swapFiles():
    source=input("enter name of the first file")
    destination=input("enter name of the second file")
    file1=open(source,"r")
    data_a=file1.read()
    file2=open(destination,"r")
    data_b=file2.read()
    file1.close()
    file2.close()
    FILE1=open(source,"w")
    FILE2=open(destination,"w")
    FILE1.write(data_b)
    FILE2.write(data_a)
    print("file data swapped sucessfully!")
    file1.close()
    file2.close()

swapFiles()
