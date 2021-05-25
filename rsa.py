# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:08:05 2021

@author: picha
"""
import random 
def is_prime(n, k = 32):
    if n <= 3:
        return True
    
    else:
        d = (n-1)/2
        r = 0
        res = 2**r
        
        while pow(d,1,2) != 1:
            d /= 2
        print(d)
        
        while res != ((n-1)/d):
            res = 2**r
            r += 1
        print(f'r={r}')
        
        for i in range(k):
            a = random.randint(1,n-2)
            x = pow(a,d,n)
            #print(f'a={a}',f'x={x}')
            
            if x == 1 or x == n-1:
                continue
            
            else:
                for j in range(r-1):
                    x = pow(x,2,n)
                    
                    if x == 1:
                        return False
                    
                    if x == n-1:
                        break
                    continue
        return True
