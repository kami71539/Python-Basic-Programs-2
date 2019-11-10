# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:16:59 2019

@author: Kamran
"""

#Wap to enter a number and print if the number is prime or not prime.
a=int(input(""))
if a>1:
    prime=True
    for i in range(2,a//2):
        if a%i==0:
            prime=False
            break
    if prime==True:
        print("The number is prime.")
    else:
        print("The number is not prime.")