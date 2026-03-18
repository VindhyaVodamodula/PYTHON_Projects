#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 02:48:19 2025

@author: vindhya

"""

while True:
    #getting input from thr user
    password=input("Enter password: ")
    if password=="hello":
          print("Welcome to the second half of the pregram!")
          name=input("please enter your name: ")
          if name=="vindhya":
                print("What a great name!")
                break
          elif name=="Madonna" or name=="Cher":
                 print("May I have your autograph, please?")
                 break
          else:
                 print(name, ", that's a nice name.") 
                 break
    else:
          print('Error!please enter valid password')
          Ask=input("Do you want to try again?(yes/no): ")
          if Ask=="yes":
           continue
          elif Ask=="no":
            break
