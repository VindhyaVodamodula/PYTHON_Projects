#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 02:15:18 2025

@author: vindhya vodamodula

"""
#Defining each function
def area_square():
    while True:
        try:
            side= float(input("enter the length of square's side: "))
            Squarearea=side*side
            print(f"The area of square is {Squarearea}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
def area_rectangle():
    while True:
        try:
            length=float(input("please enter length of rectangle: "))
            width=float(input("please enter the width of the rectangle: "))
            Area_rectangle=length*width
            print(f"Area of rectangle is {Area_rectangle}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
def Area_circle():
    while True:
        try:
            radius=float(input("Enter radius of circle: "))
            Circle_area=3.14*radius**2
            print(f"Area of circle is {Circle_area}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
def Perimeter_square():
    while True:
        try:
            Side=float(input("please enter the length of the square's side: "))
            square_perimeter=4*Side
            print(f"Perimeter of Square is {square_perimeter}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
def Preimeter_rectangle():
    while True:
        try:
            Length=float(input("Please enter length of the rectangle: "))
            Width=float(input("Please enter width of the rectangle: "))
            rectangle_perimeter=2*Length*Width
            print(f"Perimeter of rectangle is {rectangle_perimeter}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
def Perimeter_circle():
    while True:
        try:
            Radius=float(input("Please enter radius of circle: "))
            Circle_perimeter=2*3.14*Radius
            print(f"Perimeter of circle is {Circle_perimeter}.")
            break
        except ValueError:
            print("Error! please enter a valid number(not letters,symbols.")
            #Taking input from users choice
print(" ")
while True:
    try:
      print("Choose from the following menu: ")
      print(" ")
      print("1)Area of square.")
      print(" ")
      print("2)Area of rectangle.")
      print(" ")
      print("3)Area of circle.")
      print(" ")
      print("4)Perimeter of square.")
      print(" ")
      print("5)Perimeter of rectangle.")
      print(" ")
      print("6)Perimeter of circle.")
      print(" ")
      print("7)Exit")  
      menu=int(input("please enter your choice: "))
      #perfoming functions and validating users input
      if menu in [1,2,3,4,5,6,7]:
          if menu==1:
             area_square()
             continue
          elif menu==2:
             area_rectangle()
             continue
          elif menu==3:
              Area_circle()
              continue
          elif menu==4:
              Perimeter_square()
              continue
          elif menu==5:
              Preimeter_rectangle()
              continue
          elif menu==6:
              Perimeter_circle()
              continue
          elif menu==7:
              print("Thankyou! You are now exiting the program :) ")
          break
      else :
          print(" ")
          print("error!please choose between 1 to 7 options.")
    except ValueError :
        print(" ")
        print("error!please choose between 1 to 7 options.")
            
             
    
    
       
        
        
            
            
