# Author name: Mr. Truong
# Version #: 0.1
# April 1, 2020

# PART 1 
# create main()
# ask the player for their name and store the INPUT into an appropriately named variable
# Greet the player by their name
#
def main():
  player_name = input("What's your name? > ")
  print("Hi " + player_name + ", Welcome to the adventure zone!")
  start_adventure()

# Create start_adventure() to start the game
# briefly print a description of the setting
# then give them a choice using an if statement
def start_adventure():
  print("\nYou awake in a dimly lit dungeon like room,\nyou see a RED door and a BLUE door")
  door = input("\nWhich door will you go through? type RED or BLUE > ")
  if (door.upper() == "RED"):
    print("\nYou go through the RED Door")
    next_scene("red_door")
  elif (door.upper() == "BLUE"):
    print("\nYou go through the BLUE Door")
    next_scene("blue_door")
  else:
    start_adventure()#error check in case of bad input starts the function again

#create next_scene() that contorls the rest of the game
def next_scene(choice):
  player_choice = choice
  if (choice == "red_door"):
    print("\nYou see a great red dragon!!")
    dragon_move = input("\nWhat do you do? type RUN or FIGHT > ")
    if (dragon_move.upper() == "RUN"):
      start_adventure()
    elif (dragon_move.upper() == "FIGHT"):
      print("\nYou try to fight the dragon....")
      game_over("Eaten by a dragon")
    else:
      next_scene(player_choice)#error check in case of bad input starts the function again

  if (choice == "blue_door"):
    print("next scene")

#create game_over() that takes in a string describing the reason of the game over
def game_over(reason):
  if (reason == "win"):
    print("\nCongrats YOU WIN!!")
  else:
    print("\nWell that was silly you were " + reason)
  exit(0)
  
# PART 2
#create blue door option
main()# run the game





