#rock, paper, scissors game
import random

def get_choices():
  player_choice = input("Ener a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice, "computer" : computer_choice}
  
  return choices

choices = get_choices()
print(choices)
