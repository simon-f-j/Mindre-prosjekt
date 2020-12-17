# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:23:35 2020
En enkel implementering av hangman i kommandolinja
@author: simon
"""

word =input('enter word: ').lower()
def split(word):
    return [char for char in word]

#print(split(word))

lives = 5
points =0
cnt=0
ch=split(word)

tmp=['-']*len(word)
pos=[]
tmp1=[]
guess = True



def quest(test):
    global cnt,lives,guess,ch,points
    if test in ch and points<len(ch):
        for item in ch:
            if item == test:
                tmp[cnt]=test
                points +=1
            cnt+=1
        cnt=0
    else:
        lives-=1
           
        

while guess == True:
    
    guess1 = input("guess a character: ").lower()
    
    quest(guess1)
    print(tmp)
    
    if lives == 0:
        print('you died!')
        guess = False
    elif points == len(ch):
        print('congrats!')
        guess = False
    

        



