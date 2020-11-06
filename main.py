import random
import os


print("Hello, you will have 10 chances to guess a number between 1 and 100. Inputting a value that is not an integer will prompt you to retry.")


def PlayAgain(): #Asks if you would like to play again  
  while True:
    again = input("Would you like to play? (type yes or no): ")
    if again == "yes": #When user says yes, call function GameStart()
      os.system('clear') #Clears console
      GameStart()
      break
    elif again == "no": #When user says no, stops program
      os.system('clear') #Clears console
      print("Thanks for playing.")
      break


def GameStart(): #Starts the game when the function is called
  x = random.randint(1,100)
  try:
    y = int(input("Pick a number between 1 and 100: ")) #User inputs an integer
  except (ValueError, TypeError): #If the value is not an integer, it will recall the function
    print("Not an integer.")
    GameStart()
  guess = 0 #Restarts the guessing chances value to 0


  while x != y: #Starts the loop when x does not equal y

  
    if x > y > 0: #If the number is higher, it will prompt you to try again
      print('Guess Higher')
      guess = guess + 1
      try:
        y = int(input("Pick a number between 1 and 100: "))
      except (ValueError, TypeError):
        print("Value entered is not an integer.")
        break


    elif x < y < 101: #If the number is lower, it will prompt you to try again
      print('Guess Lower')
      guess = guess + 1
      try:
        y = int(input("Pick a number between 1 and 100: "))
      except (ValueError, TypeError):
        print("Value entered is not an integer.")
        break


    else:
      print("Value entered is out of boundaries.") #If the number is out of boundaries, it will break the loop
      break
    if guess == 9: #If the variable = 9, then the game ends
      print("Too many guesses!")
      break


  else:
    print("Great job! You had to guess " + str(guess) + " time(s)!") #Displays the amount of guesses after winning
    guess = str(guess)
  PlayAgain() 


GameStart()