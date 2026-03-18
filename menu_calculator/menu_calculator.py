#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 01:51:39 2025

@author: vindhya

"""
#Displaying program name
print("math functions")

while True:
    #display menu
    print("choose from following menu:")
    print("Addition(A)")
    print("Multiply(M)")
    print("Subtraction(S)")
    print("Division(D)")
    print("Exponent(E)")
    print("Remainder(R)")
    # getting input from user to choose
    choice=input("Enter A, M, S, D, E or R: ").upper()
    #validating user choice
    if choice not in ["A","S","M","D","E","R"]:
       print("invalid entry,Try again")
       continue
       #performing addition operation
    if choice=="A":
        #getting numbers from user and validating
      while True: 
          try:
             x=float(input("enter first number:"))
             y=float(input("enter second number:"))
             print(f"Answer= {x+y}")
             break
          except ValueError:
              print("ERROR!enter valied number.")
         #performing multiplication operation
    if choice=="M":
        #getting numbers from user and validating
        while True: 
            try:
               x=float(input("enter first number:"))
               y=float(input("enter second number:"))
               print(f"Answer = {x*y}")
               break
            except ValueError:
                print("ERROR!enter valied number.")
                #performing subtraction operation

    if choice=="S":
         #getting numbers from user and validating
         while True: 
             try:
                x=float(input("enter first number:"))
                y=float(input("enter second number:"))
                print(f"Answer = {x-y}")
                break
             except ValueError:
                 print("ERROR!enter valied number.")
                 #performing division operation

    if choice=="D":
        #getting numbers from user and validating
        while True: 
            try:
               x=float(input("enter first number:"))
               y=float(input("enter second number:"))
               print(f"Answer = {x/y}")
               break
            except ValueError:
                print("ERROR!enter valied number.")
                #performing exponent operation

    if choice=="E":
         #getting numbers from user and validating
         while True: 
             try:
                x=float(input("enter first number:"))
                y=float(input("enter second number:"))
                print(f"Answer = {x**y}")
                break
             except ValueError:
                 print("ERROR!enter valied number.") 
                 #performing remainder operation

    if choice=="R":
         #getting numbers from user and validating
         while True: 
             try:
                x=float(input("enter first number:"))
                y=float(input("enter second number:"))
                print(f"Answer = {x%y}")
                break
             except ValueError:
                 print("ERROR!enter valied number.")            
                
#looping back to the main menu                
    continue                

    
    

   

   
    

    
