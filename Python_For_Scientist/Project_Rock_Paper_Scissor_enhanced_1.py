# -*- coding: utf-8 -*-
"""

@author: Gregory Krulin
Added variable HumanCount to store count of rock paper or scissor choice as 
naively counting is too costly when amount of rounds increases
Added function fequency to assign probability list
"""
import numpy as np
from random import randint

def UpdateGameRecord(GameRecord,ChoiceOfComputerPlayer,ChoiceOfHumanPlayer,Outcome, HumanCount):
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
    HumanCount[ChoiceOfHumanPlayer] +=1
    outcome_list = {0:"It is a tie", 1:"Computer wins", 2: "Human wins"}
    print()
    print('-'*5 + 'Outcome' + '-'*5)
    print("%s: Computer chose %s; Human chose %s" %(outcome_list[Outcome],\
                                                   ChoiceOfComputerPlayer,\
                                                   ChoiceOfHumanPlayer))
    print('-'*20)
    
    
    
def HumanPlayer(GameRecord):
    end = ['r','s','p','q','rock', 'scissors', 'paper', 'quit']
    valid = ['r','s','p','q','g','game','rock', 'scissors', 'paper', 'quit']
    word = {'r':'rock', 's':'scissors', 'p':'paper', 'q':'quit'}
    ChoiceOfHumanPlayer = ' '
    print("\nLets play.....")
    while not(ChoiceOfHumanPlayer in end):
        print("Choose (r)rock, (s)scissors, or (p)paper\n \
or choose (g)game to see game results so far\n \
or choose (q)quit to quit the game.")
        ChoiceOfHumanPlayer = input("Please input a valid choice:  ")
        if not(ChoiceOfHumanPlayer in valid):
            print("Not valid choice.")
            print()
        if ChoiceOfHumanPlayer == 'g' or ChoiceOfHumanPlayer =='game':
            if len(GameRecord[2]) != 0:
                 print('-'*5 + 'Record Of the Game' + '-'*5)
                 print('Number of rounds so far: %d' %(len(GameRecord[2])))
                 print('Number of draws: %d' %(GameRecord[2].count(0)))
                 print('Number of computer wins: %d' %(GameRecord[2].count(1)))
                 print('Number of human wins: %d' % (GameRecord[2].count(2)))
                 print('Human; Computer')
                 for x in range(0, len(GameRecord[2])):
                     print('%d: %s; %s' %(x + 1, GameRecord[0][x], GameRecord[1][x]))
                 print('-'*25)
            else: 
                 print("No rounds have been played so far")
        
    if ChoiceOfHumanPlayer == 'q' or ChoiceOfHumanPlayer =='p'or ChoiceOfHumanPlayer == 'r' or ChoiceOfHumanPlayer == 's':
        ChoiceOfHumanPlayer = word[ChoiceOfHumanPlayer]
    return ChoiceOfHumanPlayer
        
    
def ComputerPlayer(GameRecord,HumanCount):
    if len(GameRecord[2]) == 0:
        dice = (randint(0,8)%3)
        dice_result = {0:'paper', 1:'rock', 2:'scissors'}
        return dice_result[dice]
    else:
        return  np.random.choice(['rock', 'paper', 'scissors'], 1, p = Frequency(HumanCount))[0] 

def Frequency(HumanCount):
    R = HumanCount['rock']
    S = HumanCount['scissors']
    P = HumanCount['paper']
    Rfreq = R/(R+S+P)
    Sfreq = S/(R+S+P)
    Pfreq = P/(R+S+P)
    p = [Sfreq, Rfreq, Pfreq]
    return p
    

def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    Outcome = -1
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        Outcome = 0
    elif ChoiceOfComputerPlayer =='rock':
        if ChoiceOfHumanPlayer == 'paper':
            Outcome = 2
        else:
            Outcome = 1
        
    elif ChoiceOfComputerPlayer =='paper':
        if ChoiceOfHumanPlayer == 'scissors':
            Outcome = 2
        else:
            Outcome =1
        
    elif ChoiceOfComputerPlayer =='scissors':
        if ChoiceOfHumanPlayer == 'rock':
            Outcome = 2
        else:
            Outcome =1
    return Outcome
def Tester(n):
    GameRecord = [[],[],[]]
    HumanCount = { 'rock': 0, 'paper': 0,'scissors': 0}
    ChoiceOfHumanPlayer = 'scissors'
    ChoiceOfComputerPlayer = ''
    i = 0
    while i < n:
        ChoiceOfComputerPlayer = ComputerPlayer(GameRecord, HumanCount)
        Outcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        UpdateGameRecord(GameRecord,ChoiceOfComputerPlayer,ChoiceOfHumanPlayer,Outcome,HumanCount)
        i+=1
        
    print('Number of rounds so far: %d' %(len(GameRecord[2])))
    print('Number of draws: %d' %(GameRecord[2].count(0)))
    print('Number of computer wins: %d' %(GameRecord[2].count(1)))
    print('Number of human wins: %d' % (GameRecord[2].count(2)))
    print(HumanCount)
    print(Frequency(HumanCount))
def PlayGame():
    GameRecord = [[],[],[]] 
    HumanCount = {'rock':0, 'paper':0,'scissors':0}
    ChoiceOfHumanPlayer = ' '
    print("Welcome to Rock-Paper-Scissors!")
    while ChoiceOfHumanPlayer != 'quit':
        ChoiceOfHumanPlayer = HumanPlayer(GameRecord)
        
        if ChoiceOfHumanPlayer == 'quit':
            print("Goodbye")
            return
        ChoiceOfComputerPlayer = ComputerPlayer(GameRecord, HumanCount)
        Outcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        UpdateGameRecord(GameRecord,ChoiceOfComputerPlayer,ChoiceOfHumanPlayer,Outcome, HumanCount)