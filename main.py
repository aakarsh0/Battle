import pandas as pd
import numpy as np
from random import random
from subprocess import call
from time import sleep

def play():
    sleep(sleeptime)
    call('clear')
    # print('Team A moves')
    #print(teamA)
    move(teamA,army1,army2)
    # print(teamA)
    showGround()
    sleep(sleeptime)
    call('clear')
    # print('team B moves')
    # print(teamB)
    move(teamB,army2,army1)
    # print(teamB)
    showGround()

def move(army,t,O):
    X = len(ground)-1 #down
    Y = len(ground[0])-1 #right
    global teamA
    global teamB
    for i in range(len(army)):
        man,position=army[i]
        x = position//10
        y = position%10
        r = random()
        #Right for r<0.5 else down
        # print(x,X,y,Y)
        if movement == 'random' or movement == 'adjacentKill':
            if movement == 'adjacentKill': #then movement will not be random
                if y<Y and ground[x][y+1]==O:
                    r = 0.1
                elif x<X and ground[x+1][y]==O:
                    r = 0.3
                elif y>0 and ground[x][y-1]==O:
                    r = 0.5
                elif x>0 and ground[x-1][y]==O:
                    r = 0.7
                
            if r<0.2 and y<Y and ground[x][y+1]!=t:
                #remove player of other team
                if ground[x][y+1]==O:
                    if O==army1:
                        teamA = list(filter(lambda p:p[1]!=x*10+y+1,teamA))
                    elif O==army2:
                        teamB = list(filter(lambda p:p[1]!=x*10+y+1,teamB))
                #change position of player
                ground[x][y+1]=t
                ground[x][y]=empty
                #update in teamList
                if t==army1:
                    teamA[i][1]=teamA[i][1]+1
                elif t==army2:
                    teamB[i][1]=teamB[i][1]+1
            elif r<0.4 and x<X and ground[x+1][y]!=t:
                if ground[x+1][y]==O:
                    if O==army1:
                        teamA = list(filter(lambda p:p[1]!=x*10+y+10,teamA))
                    elif O==army2:
                        teamB = list(filter(lambda p:p[1]!=x*10+y+10,teamB))
                #change position of player
                ground[x+1][y]=t
                ground[x][y]=empty
                #update in teamList
                if t==army1:
                    teamA[i][1]=teamA[i][1]+10
                elif t==army2:
                    teamB[i][1]=teamB[i][1]+10
            elif r<0.6 and y>0 and ground[x][y-1]!=t:
                #remove player of other team
                if ground[x][y-1]==O:
                    if O==army1:
                        teamA = list(filter(lambda p:p[1]!=x*10+y-1,teamA))
                    elif O==army2:
                        teamB = list(filter(lambda p:p[1]!=x*10+y-1,teamB))
                #change position of player
                ground[x][y-1]=t
                ground[x][y]=empty
                #update in teamList
                if t==army1:
                    teamA[i][1]=teamA[i][1]-1
                elif t==army2:
                    teamB[i][1]=teamB[i][1]-1
            elif r<0.8 and x>0 and ground[x-1][y]!=t:
                if ground[x-1][y]==O:
                    if O==army1:
                        teamA = list(filter(lambda p:p[1]!=x*10+y-10,teamA))
                    elif O==army2:
                        teamB = list(filter(lambda p:p[1]!=x*10+y-10,teamB))
                #change position of player
                ground[x-1][y]=t
                ground[x][y]=empty
                #update in teamList
                if t==army1:
                    teamA[i][1]=teamA[i][1]-10
                elif t==army2:
                    teamB[i][1]=teamB[i][1]-10

def showGround():
    print('Team A - {} '.format(len(teamA)), teamA)
    print('Team B - {} '.format(len(teamB)),teamB)
    print('AWin - {}'.format(Gwin))
    print('BWin - {}'.format(Xwin))
    print('\nTime: {} min'.format(iteration))
    print('\n\nThe Ground')
    print(pd.DataFrame(ground))

#Initial Variables
L = 10
B = 10
iteration = 0
sleeptime = 0
army1 = 'G'
army2 = 'X'
empty = ' '
Gwin = 0
Xwin = 0
movement = 'adjacentKill' #choose from random,adjacentKill

#Creating the play Arena
ground = [[empty for i in range(L)]for j in range(B)]

#fill the position of teams, need to create a function
# print('Place team A')
# nA = input("Enter positions of Team A")
nA = '0 10 20 30 40 50 60 70 80 90'
teamA = [[1,int(x)] for x in nA.split(' ')]
print('Team A: ',teamA)
for p in teamA:
    ground[int(p[1]//10)][p[1]%10] = army1

# print('Place team B')
# nB = input("Enter positions of Team B")
nB = '9 18 27 36 45 55 66 77 88 99'
teamB = [[2,int(x)] for x in nB.split(' ')]
print('Team B: ',teamB)
for p in teamB:
    ground[int(p[1]//10)][p[1]%10] = army2

#Initial Ground
showGround()
#making copy
originalground = ground[:]
originalTeamA = teamA[:]
originalTeamB = teamB[:]
sleep(5)


for i in range(100):
    iteration=0
    ground = originalground[:]
    teamA = originalTeamA[:]
    teamB = originalTeamB[:]
    while iteration<200 and len(teamA) > 0 and len(teamB) > 0:
        iteration += 1
        play()
    if len(teamA)==0:
        Xwin+=1
    elif len(teamB)==0:
        Gwin+=1
    sleep(1)
print('Gwin: {} XWin: {}'.format(Gwin,Xwin))


#ideas
##movement:
##1. if neighbor is opponent, just kill it. DONE - adjacentKill
##2. more probability to move towards center of cluster of opponents
##3. Each soldier has the info of position at a movement, and then everyone moves accordingly.