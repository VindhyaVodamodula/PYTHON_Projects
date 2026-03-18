import random


# first dice roll is an int
first_dice_roll = random.randint(1,6)

#second dice roll is an int
second_dice_roll = random.randint(1,6)

# display welcome message
print("Welcome to the Dice Game, if you win you win double!")

#Getting input from user to play game.
ready = "yes" or "no"

ready = input("Would you like to play? (yes/no) ")

if ready == "no":
    print("Thanks, see you soon")
            
elif ready == "yes":
    wager = int(input("How much would you like to wager? (enter an integer less than or equal 100): "))
    guess = int(input("What is your guess number guess? (1-6): "))
    possible_winning = 2*wager
    First_winning = 0
    print(f"If you guess correctly you win {possible_winning}")

    #winning condition
    if (wager <= 100) and (1 <= guess <= 6 and guess == first_dice_roll):
        print(f"Congratulations, you win {possible_winning}")
        First_winning = possible_winning

    #if wager is too high.
    elif wager > 100:
        print("That's too much sorry")

    #loosing condition
    else:
            wager <= 100 and (1 <= guess <= 6 and guess != first_dice_roll)
            print(f"You lost your wager {wager}")
            First_winning = -wager 
else:
    print("Invalid input, Please try again") 


#part-2 (second the game)
#
double_wager = wager*2
second_possible_winning = possible_winning * 2 

  
double_the_game = input(f"Would you like to go second play for {second_possible_winning}? (yes/no) ") 

if double_the_game == "no":
    print(f"Thank you, your current total is {First_winning}.") 
elif double_the_game == "yes":
    second_guess = int(input("What is your guess number guess? (1-6) "))

    #second winning condition
    if second_guess == second_dice_roll:
        second_winning =  second_possible_winning
        final_winning = First_winning + second_winning
        print(f"Wow! you won all {final_winning} in total")
        

    #second loosing 
    elif second_guess != second_dice_roll:
        second_winning = -double_wager
        final_winning = First_winning + second_winning
        print(f"You lose all {final_winning} in total")
                     


