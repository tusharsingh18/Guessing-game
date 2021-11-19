# print("This is the number guessing game")
# input = int(input("Guess your number between 1 to 100: \n"))
# Guess = 1
# Game_over = False
# while not Game_over:
#     print("you win ! and you guess the number in (guess) time")
#     Game_over = True
#

# This is the final code of this exercise :---------------------------------------
# n = 18
# number_of_guesses = 1
# print("Number of guesses is limited to only 9 times:  ")
# while (number_of_guesses<=9):
#      guess_number = int(input("Guess the number : \n"))
#     if guess_number <18:
#         print("You enter Lesser number please enter greater number. \n")
#     elif guess_number >18:
#         print("You enter greater number please enter less number . \n")
#     else:
#     print("You win \n")
#     print(number_of_guesses, "no.of guess he took to finish .")
#     break
#     print(9-number_of_guesses,"No.of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game over")
#


# Next code for this exercise

number = 19
attempt = 0
Number_of_guesses = 9
while (Number_of_guesses):
    attempt = attempt + 1
    user=int(input("Enter your first number:"))
    if user > number:
        print("You enter greater number please enter smaller number")
    elif input == number:
        print("You enter correct number")
        print("Number of attempt :" + str(attempt))
        break

    else:
        print("Your number is lesser ")

    Number_of_guesses = Number_of_guesses-1
    print("Remaining number of guesses :"+str(Number_of_guesses))





