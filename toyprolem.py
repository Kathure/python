#!/usr/bin/python

listy = [1,4,45,6,10,-8]
n  = 16
arr_size = len(listy)

#checking for n difference in array

def arrayFunc(listy,arr_size,n):
    #sort the array
    listy = listy.sort()
    l = 0
    r = arr_size-1
    
    #traverse the array for the two elements
    for i in range(0,len(listy)):
        if (listy[r] - listy[l] == n ):
            n = listy[r]- listy[l]
            return n     
        else:
            r -= 1
    return n

arrayFunc(listy,arr_size,n)
