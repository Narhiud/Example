# https://en.wikipedia.org/wiki/Nim

import random
import itertools


#nr_games = input('Number of games to play: ')
#nr_games = int(nr_games)

nr_games = 1000000


NIM=[1,
     3,
     5,
     7]
acoes=sum(NIM)
NIM1=(1,
     3,
     5,
     7)

#Possible moves:
#L=(row,nº of pieces removed)
L=[]

for a in range(len(NIM)):
    b=list(range(1,NIM[a]+1))
    l=[NIM[a]]
    c=[l,b]
    combination = [p for p in itertools.product(*c)]
    L.extend(combination)




Pieces=[]
for a in range(0,NIM[0]+1):
    for b in range(0,NIM[1]+1):
        for c in range(0,NIM[2]+1):
            for d in range(0,NIM[3]+1):
                Pieces.append([a,b,c,d])
                
Pieces.reverse()  
Pieces.pop(-1)

    

Dic={}
for a in range(len(Pieces)):
    z=Pieces[a]
    Stat={}
    for l in range(len(z)):
        d=z[l]
        for i in range(1,d+1):
            for j in range(1,min(i,d)+1):
                Stat[(l,j)] = 0
            Dic[tuple(Pieces[a])]=Stat

for g in range(nr_games):
  # moves[player][pos]:
  #   for player 1 and 2:
  #     for each position this player went through:
  #        number of peaces taken at position
  moves = {}
  moves[1] = {}
  moves[2] = {}
  # Player 1 is starting
  pos = NIM1
  player = 0
  # One game:
  while sum(pos):
    # switch players
    player = 2 if player == 1 else 1

    #random move
    #move = max(Dic[pos], key=Dic[pos].get)   #other possible solution but self fulfilling and possibly decreases effectiveness
    move = random.choice(list(Dic[pos].keys()))
    moves[player][pos] = move
    pos=list(pos)
    pos[move[0]] -= move[1]
    pos=tuple(pos)

  # last player wins, collect statistics:  
  for pos in moves[player]:
    Dic[pos][moves[player][pos]]+= 1
  # switch to other player that lost:
  player = 2 if player == 1 else 1
  for pos in moves[player]:
    Dic[pos][moves[player][pos]] -= 1

# Detect best move for all positions and write statistics to text file:
f = open('nim.txt', 'w')
f.write("") 
for a in range(len(Pieces)):
    z=Pieces[a]
    z=tuple(z)
    best = max(Dic[z], key=Dic[z].get)
    v = Dic[z][best]
    if v<0:
        best = '-'
        v = ''
    f = open('nim.txt', 'a') 
    f.write (f"{z}: best:{best} v:{v:>5}    {Dic[z]}\n")
    f.close()

