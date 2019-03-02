#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:30:27 2019

@author: Ashley
"""
# =============================================================================
#                               Ashley Scurlock
#                           DSCI 401 Assignment 1
# =============================================================================
#%%
# =============================================================================
# I.Flatten
# =============================================================================

def flatten(*lists):
    #convert int variables into lists
    lists = list(map(lambda x: [x] if isinstance(x ,int) else x, lists))
    #converts flatten a list of lists into a list
    lists = list(map(lambda x: sum(x,[]) if isinstance(x[0] ,list) else x, lists))
    lists = sum(lists,[])
    for i in range(len(lists)):
        if isinstance(lists[i] ,list):
            lists = flatten([x for x in lists if lists.index(x) != i],lists[i])
    return lists


flatten([1,2,3], [[4],[5]], 6,7,8,[[9,[10]]])


#%%
# =============================================================================
# II.Power Set
# =============================================================================
def power_set(powerset):
    return [gen_combs(powerset, x+1) for x in reversed(range(len(powerset)))] + [[]]

def gen_combs(lists, k):
    #Trivial Case
    if k == len(lists): 
        return [lists]
    #Base Case
    if k == 1: 
        return [[x] for x in lists]
    else:
        return[[lists[0]] + i for i in gen_combs(lists[1:], k-1)] + gen_combs(lists[1:],k)


power_set([1,2,3])
#%%
# =============================================================================
# III.All Permutations
# =============================================================================
def all_perms(List):
    #Trivial Case
    if len(List) == 1: 
        return [List]
    #Base Case
    if len(List) == 2: 
        return [List] + [list(reversed(List))]
    else:
        return sum([[[List[mm]] + i for i in all_perms(List[:mm]+List[mm+1:])] for mm in range(len(List))],[])
        
all_perms([1,2,3])


#%%
# =============================================================================
# IV.Number Spiral
# =============================================================================
def spiral(n, end_corner):
    matrix = np.zeros((n,n))
    N = len(matrix)
    number = N**2 -1
    if end_corner == 1:
        for RR in range(0, int((N)/2)):  
            #Starting Top left --> Bottom left
            for n in range(RR,N-RR):
                matrix[n][0+RR] = number
                number = number - 1 
            #Starting Bottom left --> Bottom right
            for n in range(RR,N-1-RR): 
                matrix[N-1-RR][n+1] = number 
                number = number - 1
            #Starting Bottom right --> Top right
            for n in reversed(range(RR,N-1-RR)):
                matrix[n][N-1-RR] = number
                number = number - 1
            #Starting Top right --> Top left (5)
            for n in reversed(range(1+RR, N-1-RR)):
                matrix[0+RR][n] = number
                number = number - 1  
                
    if end_corner == 2:
        for RR in range(0, int((N)/2)):
            #Starting Top right --> Top left
            for n in reversed(range(RR,N-RR)):
                matrix[0+RR][n] = number     
                number = number - 1    
            #Starting Top left --> Bottom left    
            for n in range(RR,N-1-RR):     
                matrix[n+1][0+RR] = number     
                number = number - 1 
            #Starting Bottom left --> Bottom right     
            for n in range(RR,N-1-RR):  
                matrix[N-1-RR][n+1] = number  
                number = number - 1
            #Starting Bottom right --> Top right 
            for n in reversed(range(1+RR, N-1-RR)):  
                matrix[n][N-1-RR] = number 
                number = number - 1
    
    if end_corner == 3:
        for RR in range(0, int((N)/2)):
            #Starting Bottom left --> Bottom right  
            for n in range(RR, N-RR): 
                matrix[N-1-RR][n] = number  
                number = number - 1
            #Starting Bottom right --> Top right 
            for n in reversed(range(RR,N-1-RR)):  
                matrix[n][N-1-RR] = number 
                number = number - 1
            #Starting Top right --> Top left 
            for n in reversed(range(RR,N-1-RR)): 
                matrix[0+RR][n] = number 
                number = number - 1    
            #Starting Top left --> Bottom left 
            for n in range(1+RR, N-1-RR): 
                matrix[n][0+RR] = number 
                number = number - 1 
    if end_corner == 4:
        for RR in range(0, int((N)/2)):
            #Starting Bottom right --> Top right 
            for n in reversed(range(RR, N-RR)): 
                matrix[n][N-1-RR] = number  
                number = number - 1
            #Starting Top right --> Top left 
            for n in reversed(range(RR,N-1-RR)): 
                matrix[0+RR][n] = number 
                number = number - 1    
            #Starting Top left --> Bottom left 
            for n in range(RR,N-1-RR):  
                matrix[n+1][0+RR] = number 
                number = number - 1     
            #Starting Bottom left --> Bottom right  
            for n in range(1+RR, N-1-RR):  
                matrix[N-1-RR][n] = number 
                number = number - 1
    return matrix
