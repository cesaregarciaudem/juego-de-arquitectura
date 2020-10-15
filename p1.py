# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:33:56 2020

@author: cesar
"""


#aaaaaaaaaaaaaaaaa
#qqqqqqqqqqqqqqqqqqqqq
#111111111111111111111
#zzzzzzzzzzzzzzzzzzzz
#!!!!!!!!!!!!!!!!

x = input("")
x = x.split()
c,v = int(x[0]),int(x[1])
voc = ['a','e','i','o','u']
op = ['o','s','x']
op2 = ['ch','sh']
resp = []
aux = []
aux2 = []

for i in range(c):
    lin = input("")
    lin = lin.split()
    aux.append(lin[0])
    aux2.append(lin[1])
for i in range(v):
    lin = input("")
    if lin in aux:
        for j in range(len(aux)):
            if lin==aux[j]:
                resp.append(aux2[j])
    elif lin[-2] not in voc and lin[-1]=="y":
        lin = lin[:-1]
        lin = lin+"ies"
        resp.append(lin)
    elif lin[-1] in op or lin[-2:] in op2:
        lin = lin+"es"
        resp.append(lin)
    else:
        lin = lin+"s"
        resp.append(lin)
for palabra in resp:
    print(palabra)

        
