# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:20:45 2020

@author: simon
"""
# enkelt skript som ber om å velge en mappe, og lager/flytter filer til mappene: dokument, tekst og andre filer


import os
import shutil
from os import listdir
from tkinter import *
from tkinter import filedialog 
import glob



root = Tk()
root.withdraw() #use to hide tkinter window
def browseFiles(): 
    directory = filedialog.askdirectory()
    # Change label contents 
    return directory



def chooseFiles(directory,ending): 
    all_files=glob.glob(directory + "/*"+str(ending).lower())
    cnt=0
    for files in all_files:
        print(f"{cnt}  {files}")
        cnt+=1
    a = list(map(int,input("\nChoose files by numbers separated by space(ex: 0 1 2): ").strip().split())) 
    new=[]
 
    for elem in a:
        try:
            new.append(all_files[elem])
            print(new)
        except:
            print("number out of range")
    return new
    


# define file format endings
doc_files = (".docx",".dotx",".txt",".odt",".doc")
pdf_files=(".pdf")
exe_files = (".exe",".py",".bat")
img_files = (".png",".PNG",".jpeg",".jpg",".eps",".img")
kmp_files = (".zip",".tar",".rar",".gz")
cell_files = (".xlsx",".xls",".csv")
ppt_files = (".ppt",".pptx")
photoshop_files=(".psd",".PSD",".PSB")
# open fileexplorer to get the target folder
directory = browseFiles()

# define desired folders to sort files into
folders=[directory+r"/dokument",\
         directory+r"/dokument/powerpoint",\
         directory+r"/dokument/pdf",\
         directory+r"/dokument/excel_filer",\
         directory+r"/dokument/word",\
         directory+r"/bilder",\
         directory+r"/bilder/photoshop_filer",\
         directory+r"/andre_filer",\
         directory+r"/andre_filer/komprimerte_filer",\
         directory+r"/andre_filer/exe_filer",\
         ]

# create folders if they do not exist
for items in folders:
    if not os.path.exists(items):
        os.makedirs(items)


def give_files(path):
    given_files=[]
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and not file.endswith(".lnk") and not file.endswith(".cls") and not file.endswith(".ini"):
            #print(file)
            given_files.append(file)
    #print(given_files)        
    return given_files




# go trough each file in the directory, check the ending and move to appropriate folder.
for file in give_files(directory):
    if file.endswith(doc_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[4], file)))
    if file.endswith(ppt_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[1], file)))
    if file.endswith(pdf_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[2], file)))
    if file.endswith(cell_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[3], file)))
    if file.endswith(img_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[5], file)))
    if file.endswith(photoshop_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[6], file)))
    if file.endswith(kmp_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[8], file)))
    if file.endswith(exe_files):
        shutil.move(os.path.join(directory, file),(os.path.join(folders[9], file)))  
    else:
        try:
            shutil.move(os.path.join(directory, file),(os.path.join(folders[7], file)))
        except:
            pass

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
