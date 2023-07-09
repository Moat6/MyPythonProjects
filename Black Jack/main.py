import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
  user_card = random.choice(cards)
  if user_card == 11 and sum(user_list) > 10:
    user_list.append(1)
  else:
    user_list.append(user_card)

  while sum(comp_list) < 17:
    comp_card = random.choice(cards)
    if comp_card == 11 and sum(comp_list) > 10:
      comp_list.append(1)
    else:
      comp_list.append(comp_card)

def finals():
  print(f"Your Final Hand : {user_list} , Your Final Score : {sum(user_list)}")
  print(
    f"Computer's Final Hand : {comp_list}, Computer's Final Score : {sum(comp_list)}"
  )

def score():
  user = sum(user_list)
  comp = sum(comp_list)
  print(f"Your cards : {user_list} , Your score : {user}")
  print(f"Computer First Card : {comp_list[0]}")

def rules():
  user = sum(user_list)
  comp = sum(comp_list)
  if user == comp and choice == "n":
    finals()
    print("Its a DRAW.")
  elif user == 21:
    finals()
    print("User Wins.")
  elif user > 21:
    finals()
    print("You went over. Computer Wins")
  elif comp > 21 and user < 21:
    finals()
    print("Computer went over. User Wins")
  elif user > comp and choice == "n":
    finals()
    print("You won.")
  elif user < comp and choice == "n":
    finals()
    print("Computer Wins")
  elif choice == "y":
    play()

def play():
  global choice
  choice = input("Type 'y' to get another card, type 'n' to pass :")
  if choice == "y":
    random_card()
    score()
    rules()
  elif choice == "n":
    rules()
  else:
    print("Wrong Input. Please Write in (y/n)")
    play()

while True:
  user_list, comp_list = [], []
  wish = input("\nDo You Want to Play The Game (y/n) :")
  if wish == "y":
    os.system("cls")
    print(logo)
    random_card()
    random_card()
    score()
    if sum(user_list) == 21:
      finals()
      print("Its a BlackJAck. User Wins")
    else:
      play()
  else:
    print("BYE BYE :) ")
    break
