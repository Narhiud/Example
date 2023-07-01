# Simulation of NIM game with one heap of maxpos peaces
# Rule: at each position, take 1, 2 or 3 pieces.
# Winner: the player that takes the last piece.
#
# https://en.wikipedia.org/wiki/Nim
#
# Machine learning:
#   Play nr_games times against yourself and collect
#   statistics for winning and loosing positions,
#   in order to obtain best move for any position.
#

import random
import sys
import itertools

# if present, use arguments in call: python nim.py {maxpos} {nr_games} 
# if len(sys.argv) > 1:
#   maxpos   = sys.argv[1]
#   nr_games = sys.argv[2]
# else:
#   nr_games = input('Number of games to play: ')
# nr_games = int(nr_games)

nr_games = 1000000

#Disposição do jogo:
NIM=[1,
     3,
     5,
     7]
acoes=sum(NIM)
NIM1=(1,
     3,
     5,
     7)

#Jogadas que são possíveis de fazer:
#L=(coluna,nº de peças retiradas)
L=[]

for a in range(len(NIM)):
    b=list(range(1,NIM[a]+1))
    l=[NIM[a]]
    c=[l,b]
    combination = [p for p in itertools.product(*c)]
    L.extend(combination)




Pecas=[]
for a in range(0,NIM[0]+1):
    for b in range(0,NIM[1]+1):
        for c in range(0,NIM[2]+1):
            for d in range(0,NIM[3]+1):
                Pecas.append([a,b,c,d])
                
Pecas.reverse()  
Pecas.pop(-1)

    

Dic={}
for a in range(len(Pecas)):
    z=Pecas[a]
    Stat={}
    for l in range(len(z)):
        d=z[l]
        for i in range(1,d+1):
            for j in range(1,min(i,d)+1):
                Stat[(l,j)] = 0
            Dic[tuple(Pecas[a])]=Stat

for g in range(nr_games):
  # moves[player][pos]:
  #   for player 1 and 2:
  #     for each position this player went through:
  #        number of peaces taken at position
  moves = {}
  moves[1] = {}
  moves[2] = {}
  # start position, player 1 is starting
  pos = NIM1
  player = 0
  # perform one game:
  while sum(pos):
    # switch to other player
    player = 2 if player == 1 else 1

    # get best move for this position so far:
    #   key of highest value in Stat[pos])
    #move = max(Dic[pos], key=Dic[pos].get)
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

# Detect best move for all positions and print statistics:
f = open('nim.txt', 'w')
f.write("") 
for a in range(len(Pecas)):
    z=Pecas[a]
    z=tuple(z)
    best = max(Dic[z], key=Dic[z].get)
    v = Dic[z][best]
    if v<0:
        best = '-'
        v = ''
    f = open('nim.txt', 'a') 
    f.write (f"{z}: best:{best} v:{v:>5}    {Dic[z]}\n")
    f.close()
  #print ("%3d: %s %5s     %s" % (i, str(best), str(v), str(Stat[i])))

"""
Forma uma estratégia melhor consoante o estado em que está.
"""