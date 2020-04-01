# Author name: Mr. Truong
# Version #: 0.1
# April 1, 2020

# PART 1 
# ask the player for their name and store the INPUT into an appropriately named variable
# Greet the player by their name
player_name = input("What's your name? > ")
print("Hi " + player_name + ", Welcome to the adventure zone!")

# Create a start_adventure function to start the game
# briefly print a description of the setting
# then give them a choice using an if statement
def start_adventure():
  print("You awake in a dimly lit dungeon like room, you see a RED door and a BLUE door")
  door = input("Which door will you go through? type RED or BLUE")
  if (door.toUpperCase() == "RED"):
    print("You go through the RED Door")
    next_scene(red_door)
  elif (door.toUpperCase() == "BLUE"):
    print("You go through the BLUE Door")
    next_scene(blue_door)

#create a next_scene function that contorls the rest of the game
def next_scene(choice):
  if