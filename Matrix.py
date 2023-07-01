# -*- coding: utf-8 -*-
"""
Solving a simple linear equation through Gauss method for a square matrix and calculating its inverse matrix.

L*(x1,x2,x3,x3)=W

@author: Narhiud
"""

#Solving equation

L0=[2,2,1,4]
L1=[1,-3,2,3]
L2=[-1,1,-1,-1]
L3=[1,-1,1,2]
I0=[1,0,0,0]
I1=[0,1,0,0]
I2=[0,0,1,0]
I3=[0,0,0,1]
Ide=[I0,I1,I2,I3]
W=[5,2,-1,2]
Wusable=W.copy()
Lists=[L0,L1,L2,L3]
lines=len(Lists)
colum=len(L0)
dif=lines-colum
X=Wusable.copy()
Usable=[L0.copy(),L1.copy(),L2.copy(),L3.copy()]

if colum>lines:
    print("Nope")


for n in range (colum):
    if dif>=n:
        for i in range (1,lines):
            const=(Usable[i][n]/Usable[n][n])
            for k in range(colum):
                Usable[i][k]=Usable[i][k]-const*Usable[0][k]
            Wusable[i]-=const*Wusable[0]
    else:
        for i in range (n-dif+1, lines):
            const=(Usable[i][n]/Usable[n][n])
            for k in range(colum):
                Usable[i][k]=Usable[i][k]-const*Usable[n-dif][k]
            Wusable[i]-=const*Wusable[n-dif]



if lines==colum:
    for i in range (0,lines):
        for k in range(0,colum):
            if k!=i:
                Wusable[-i-1]-=Usable[-i-1][-k-1]*X[-k-1]
            if i==k:
                X[-i-1]=Wusable[-i-1]/Usable[-i-1][-k-1]
                break
        
    for i in range (lines):
        print('x'+str(i+1),'=',X[i])
        
#Calculating inverse matrix
Usable=[L0.copy(),L1.copy(),L2.copy(),L3.copy()]



for n in range (colum):
    for i in range (n-dif+1, lines):
        const=(Usable[i][n]/Usable[n][n])
        for k in range(colum):
            Usable[i][k]=Usable[i][k]-const*Usable[n-dif][k]
            Ide[i][k]-=const*Ide[n-dif][k]
        



for i in range(lines):
    const=Usable[i][i]
    for k in range (colum):
        Usable[i][k]/=const
        Ide[i][k]/=const

        
for n in range (-1,-colum-1,-1):
    for i in range (n-1, -lines-1,-1):
        const=(Usable[i][n]/Usable[n][n])
        for k in range(-1,-colum-1,-1):
            Usable[i][k]=Usable[i][k]-const*Usable[n-dif][k]
            Ide[i][k]-=const*Ide[n-dif][k]




for i in range (lines):
    print('|',f'{Ide[i][0]:.2f}',f'{(Ide[i][1]):.3f}',f'{(Ide[i][2]):.3f}',f'{(Ide[i][3]):.3f}','|')
    
