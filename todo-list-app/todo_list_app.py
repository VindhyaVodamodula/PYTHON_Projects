#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:18:18 2024

@author: vindhya
"""
from datetime import datetime

#Displaying welcome message
print('\n')
print('Welcome to "TO-DO LIST APP"😊')
print('\n')

#displaying MENU OPTIONS
menu=[
    "1. Add Task",
    "2. View by creation date",
    "3. View by priority",
    "4. Update tasks",
    "5. Delete task",
    "6. Exit App"
] 
tasks=[]

#Defining each function:
def add_task():#creation date,name of task,dead line,priority,discreption

    #Displaying current date
    task_creation_on=datetime.now().date()
    print("task created on: ",task_creation_on)
    
    #Asking task input from user
    name=(input("Please enter task name: "))
    
    while True:
        #asking deadline input
        deadline=input('please enter deadline[yyyy-mm-dd]: ')
        #date formatting
        def date_format(deadline):
            Date_format= '%Y-%m-%d'
            try:
              datetime.strptime(deadline, Date_format )
              return True
            except ValueError:
              return False
        #checking thr deadline date format and making sure its on or before creation date
        task_creation_on=datetime.now().date()
        if date_format(deadline):
            deadline_date=datetime.strptime(deadline, '%Y-%m-%d').date()
            if deadline_date>=task_creation_on:
               break
            else:
               print("Invalid, please check formatting date or input date should be on or after today's date:")
    print('Dead line date noted: ',deadline_date) 
      
    #Getting priority input from the user:
    while True:
        try:
            input_priority=(input("please enter priority from 1-10: "))
            priority=int(input_priority)
         # 1 being the higest priority and 10 being the lowest
            if 1<=priority<=10:
              break
            else : 
               print('Invalid,please select priority of task from 1-10: ')
        except ValueError:
           print('Invalid input,(please select priority number between 1-10.')
    print('Priority noted: ',priority)        
    # description of task       
    Discreption=(input("enter notes for the task: "))     
         
    #Adding current task to the list: 
    task={
          "task_creation_on":task_creation_on,
          "name":name,
          "dead line":deadline_date,
          "priority":priority,
          'Discreption':Discreption        
         }
    tasks.append(task)
    # numbering each task in my list of tasks
    for i ,task in enumerate(tasks, start=1):  
        print(f"Task {i}:")
        print("Name:", task["name"])
        print("Deadline:", task["dead line"])
        print("Priority:", task["priority"])
        print("Created on:", task["task_creation_on"])
        print("Description:", task["Discreption"])
        print()    

    #Conformation to the user     
    print(name,'added to your "TO-DO List."')
    
    
    

        
    
    



