# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:59:11 2019

@author: Kamran
"""

#Write a program to enter a number and print sum of all its digits.
num=int(input(""))
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+r
print(sum)