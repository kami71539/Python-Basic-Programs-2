# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:01:52 2019

@author: Kamran
"""

#Wap to enter 3 digits number and print if the number is armostrong or not.
num=int(input(""))
num2=num
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+(r*r*r)
if sum==num2:
    print("The number is armostrong.")
else:
    print("The number is not an armostrong.")