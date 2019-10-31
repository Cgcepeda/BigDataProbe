#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:20:29 2019

@author: cristiancepeda
"""

import numpy as np
import random


print("Ingrese tamaño del tablero de ajedrez:")
table=int(input())
#table=8
chesstable=np.zeros((table,table))
xub=random.randint(0,table-1)
yub=random.randint(0,table-1)
decition = ""
while decition != "Reina" and decition != "Caballo":
    print("Ingrese Reina o Caballo para ingresar su movimiento:")
    decition=str(input())
#decition="Caballo"
if decition == "Reina":
    chesstable[xub,:]=1
    chesstable[:,yub]=1
    print("Posicion Ficha",(xub,yub))
    i=xub
    j=yub
    while i<table and j<table:
        print((i,j))
        chesstable[i][j]=1
        i+=1
        j+=1
    i=xub
    j=yub    
    while i<table and j>=0:
        print((i,j))
        chesstable[i][j]=1
        i+=1
        j-=1
    i=xub
    j=yub       
    while i>=0 and j>=0:
        print((i,j))
        chesstable[i][j]=1
        i-=1
        j-=1
    i=xub
    j=yub    
    while i>=0 and j<table:
        print((i,j))
        chesstable[i][j]=1
        i-=1
        j+=1
elif decition == "Caballo":
    desdown=xub+2
    desup=xub-2
    desleft=yub-2
    desright=yub+2
    if desdown<table:
        chesstable[desdown][yub+1]=1
        chesstable[desdown][yub-1]=1
    if desup>=0:
        chesstable[desup][yub+1]=1
        chesstable[desup][yub-1]=1
    if desleft>=0:
        chesstable[xub+1][desleft]=1
        chesstable[xub-1][desleft]=1
    if desright>=0:
        chesstable[xub+1][desright]=1
        chesstable[xub-1][desright]=1
chesstable[xub][yub]=8
print(chesstable)
