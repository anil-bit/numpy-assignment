#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:19:32 2022

@author: anil
"""


k = 3
n = 13
pp = n-k+1
#moving average sequence 
#print(pp)



data = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
w = 3

hh =[]
count = 0
for i in range(len(data)):
    o =0
    for j in range(i,i+w):
        #print(data[j])
        o = o+data[j]
    uu=o/w
    uu = int(uu)
    hh.append(uu)        
    count=count+1
    #print(count)
    if count == pp:
        break
        
    
print(hh)    
        
   
        
    


