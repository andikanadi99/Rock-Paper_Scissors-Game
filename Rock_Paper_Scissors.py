#Implements a rock paper and scissor game that goes on until user quits
import random

"""
* This program assignes the object choice based on the given number input.
* Parameters:
*     input: Move choice.
* Return:     Correctly worded choice.
"""
def move(input):
  if input == 1:
    return "Rock"
  elif input == 2:
    return "Paper"
  else:
    return "Scissor"

"""
* This program returns a letter to represent if user won, loss or draw
* Parameters:
*     user_input: user's move.
*     computer_input: computer's move.
* Return:     Letter if user won or lost.
"""
def game(user_input,computer_input):
  options = ['w','l','d']

  #Gets and prints both the user and computer move
  userMove = move(user_input)
  computerMove = move(computer_input)
  print('You pick ' + userMove)
  print('Computer picks ' + computerMove)
  print()

  #Checking for winning conditions based on what user picked
  #Rock conditions
  if(user_input == 1):
    if(computer_input == 1):
      return 'd'
    elif(computer_input == 2):
      return "l"
    else:
      return "w"

  #Paper conditions
  elif(user_input == 2):
    if(computer_input == 1):
      return 'w'
    elif(computer_input == 2):
      return "d"
    else:
      return "l"

  #Scissor conditions
  else:
    if(computer_input == 1):
      return 'l'
    elif(computer_input == 2):
      return "w"
    else:
      return "d"



# MAIN function:
userScore = 0
computerScore = 0

#Intro message
print()
print('Welcome to the rock, paper and scissor game.\nIn this game, you will be playing the classic game against an AI.')
print()
name = input('What is your name: ')
print()
#Ask user if they want to play the game
user_input = input("To play the game, type yes. Anything else inputted will cause the game to quit.\nDo you want to play? ")
if user_input.lower() != 'yes':
  exit()
else:
  print('\n')
  quit = False

  #Game prompts user until quits
  while not quit:

    #Prompts user for a move. Then checks and print if user won, loss or draw
    valid = False
    while not valid:
      user_input = input('Select your choice with the associated digit: Rock(1), Paper(2), Scissor(3): ')
      if(user_input == '1' or user_input == '2' or user_input == '3'):
        valid = True
      else:
        print("Invalid input, try again.")

    user_input = int(user_input)
    computer_input = random.randint(1,3)
    win = game(user_input,computer_input)

    #If-Else statements to check if user or computer won
    if win == 'w':
      print(name + ' won!')
      userScore += 1
    elif win == 'l':
      print('Computer won!')
      computerScore += 1
    else:
      print('Draw.')

    #Display score of user and computer
    print(name + ' score: ' + str(userScore))
    print('Computer score: ' + str(computerScore))

    #Quit prompt
    user_input = input("Do you still want to play? ")
    if user_input != 'yes':
      quit = True
    else:
      print()
#Conclussion:
print()
print('Final Scores:')
print(name + ' score: ' + str(userScore))
print('Computer score: ' + str(computerScore))
print("Goodbye")
