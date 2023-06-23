#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 00:20:00 2023

@author: salman
"""

import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv


path = os.path.expanduser('~/Desktop/123/')

# a = "this is a test"
# b= "this is a test!"

# GT = ["ANU, Located in, Canberra Australia","ANU, Location, Canberra"]
# T = ["ANU, Located in, Canberra Australia", "ANU, is in, Australia"]

# x = fuzz.ratio(GT,T)

# print("Ratio Measure: ",x)

# y = fuzz.partial_ratio(GT,T)
# print("Partial Ratio Measure: ",y)


# c=0
# for x in T:   
#     cs=0
#     for y in GT:
#         fr = fuzz.partial_ratio(x,y)
#         print(fr)
#         if fr>cs:
#             cs=fr
            
#     c+=cs

# k = len(T)
# l= len(GT)
# print(k,"vs",l)
# n = max(k,l)

# print("Total Fuzzy Partial Similarity:",c/n)

P=50
A=80
tcos=0
tjac=0
tcosa=0
tjaca=0
tcosp=0
tjacp=0
totalCos=0
totalJac=0
totalSS=0
ttt=0
with open(path+"CC.csv","r") as f:
    #data = f.readlines()
    csv_readerx = csv.reader(f, delimiter=',')
    num=0
    for n in csv_readerx:    
        #trips.append(n)
        #print(n)
        i=0
        x=n[1]
        y=n[4]
        c=0
        j=0
        s=0
        i=1
        if y:
            GT=x.split(',')
            T=y.split(',')
            #print(T)
            
            for a in T:   
                cs=0
                js=0
                ss=0
                ttt+=1
                for b in GT:
                    Csim = fuzz.ratio(a,b)
                    if Csim>cs:
                        cs=Csim
                    # else:
                    #     cs=cs
                
                    Jsim = fuzz.partial_ratio(a,b)
                    if Jsim>js:
                        js=Jsim
                    # else:
                    #     js=js
                    
                    Ssim = fuzz.token_sort_ratio(a,b)
                    if Ssim>ss:
                        ss=Ssim
                    # else:
                    #     ss=ss
            
                # AMNESTY        
                if (js<P):
                    js=0    
                # elif (js < P):
                #     js=0
                # else:
                #     js=js
           
                  
                # # AMNESTY    
                if (cs<P):
                    cs=0   
                # elif (cs < P):
                #     cs=0
                # else:
                #     cs=cs
                
                # # AMNESTY    
                if (ss<P):
                    ss=0  
                # elif (ss < P):
                #     ss=0
                # else:
                #     ss=ss
                
                c+=cs
                j+=js
                s+=ss
            #print(c,j,s)
        k = len(GT)
        l= len(T)
        #print(k,"vs",l)
        n = max(k,l)
            
        c = c/n
        j = j/n
        s = s/n
        #print(c,j,s) 
        # AMNESTY
        # if (c>A):
        #     c=100
        # # PENALTY
        # if (c<P):
        #       c=0
       
        # # AMNESTY    
        # if (j>A):
        #     j=100  
        # # PENALTY
        # if (j<P):
        #     j=0
        
        
        # if (s>A):
        #     s=100  
        # # PENALTY
        # if (s<P):
        #     s=0

            
        output=c,j,s    
        totalCos+=c
        totalJac+=j
        totalSS+=s
        
        with open(path + 'threshf/GPTS.csv', 'a') as file:
                  writer = csv.writer(file, delimiter=',')
                  writer.writerow(output)
                  
    print(totalCos,totalJac,totalSS)
    num+=1
        # print("Fuzzy Ratio Similarity For Paragraph ",num,":",cos)
        # print("Fuzzy Partial Ratio Similarity For Paragraph ",num,":",jac)
     
        
        
print("Total Triples By Model:", ttt) 
# print("Total Fuzzy Ratio Similarity:",totalCos)
# print("Total Fuzzy Partial Ratio Similarity:",totalJac)
# print("Total Fuzzy Sorted Ratio Similarity:",totalSS)
print("Total Fuzzy Ratio  Similarity:",(totalCos/80),"%")
print("Total Fuzzy Partial Ratio Similarity",":",(totalJac/80),"%")
print("Total Fuzzy Sorted Ratio Similarity",":",(totalSS/80),"%")