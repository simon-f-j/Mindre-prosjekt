# -*- coding: utf-8 -*-
"""
The monty hall problem

Created on Sun Oct 25 20:36:46 2020

@author: simon
"""

import random as rd


# Create list of three doors, fill with 'empty'
def  keepdoor():
    doors=['empty','empty','empty']
    # Replace a random door with prize, and save the location of the prize as a variable
    prize = rd.randint(1,3)
    #print(prize)
    doors[prize-1]='prize'
    #print(doors)

    # Choose a door
    choice_p = rd.randint(1,3)-1

    # create a list of doors without prizes        
    cnt=0
    doors_noprize=[]
    for item in doors:
        if item != 'prize':
            doors_noprize.append(cnt)
        cnt+=1

    # Host opens a random door, not containing the prize
    if choice_p in doors_noprize:
        doors_noprize.remove(choice_p)
    choice_h = rd.choice(doors_noprize)

    # keep door:
    if doors[choice_p] == 'prize':
        print('congrats!')
        cnt=1
        return cnt
    else:
        print('you lost...')
        cnt=0
        return cnt


def switchdoor():
    doors=['empty','empty','empty']
    # Replace a random door with prize, and save the location of the prize as a variable
    prize = rd.randint(1,3)-1
    #print(prize)
    doors[prize]='prize'
    #print(doors)
    print(f"prize is behind door: {prize}")
    choices = [0,1,2]

    # create a list of doors without prizes        
    cnt=0
    doors_noprize=[]
    for item in doors:
        if item != 'prize':
            doors_noprize.append(cnt)
        cnt+=1

    # Player chooses a door
    choice_p = rd.randint(1,3)-1
    print(f"player chooses door: {choice_p}")

    # Host opens a random door, not containing the prize
    if choice_p in doors_noprize:
        doors_noprize.remove(choice_p)
    choice_h = rd.choice(doors_noprize)
    
    choices.remove(choice_p)
    choices.remove(choice_h)
    
    if doors[choices[0]] == 'prize':
        print('you won')
        return 1
    else:
        print('you lost')
        return 0


    # choose the remaining door:
    for choice in choices:
        if choice != choice_p and choice!=choice_h:
            final_choice = choice
            #print(f"player switches door to: {final_choice}")

    if doors[final_choice] == 'prize':
        print('congrats!')
        cnt=1
        return cnt
    else:
        print('you lost...')
        cnt=0
        return cnt

 
if __name__ =="__main__":
    results=[]
    for n in range(2000):
        results.append(switchdoor())
    print(sum(results)/len(results))

