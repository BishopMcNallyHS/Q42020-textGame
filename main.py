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
  
  if (choice == "red_door"):
    red_door()
    #come back for part 2
  if (choice == "blue_door"):
    blue_door()

def red_door():
  print("\nYou see a great red dragon!!")
  dragon_move = input("\nWhat do you do? type RUN or FIGHT > ")
  if (dragon_move.upper() == "RUN"):
    start_adventure()
  elif (dragon_move.upper() == "FIGHT"):
    print("\nYou try to fight the dragon....")
    game_over("Eaten by a dragon")
  else:
    next_scene("red_door")#error check in case of bad input starts the function again

#create game_over() that takes in a string describing the reason of the game over
def game_over(reason):
  if (reason == "win"):
    print("\nCongrats YOU WIN!!")
  else:
    print("\nWell that was silly you were " + reason)
  exit(0)

# PART 2
#create blue door option
backpack = []
def blue_door():
  global backpack
  '''
    The player finds a treasure chest, options to investigate the treasure 
    chest or guard.

    If player chooses
    - Treasure chest: show its contents
    - Guard: nothing for now
    '''
    # The variable treasure_chest is an object type called a list
    # A list can be empty as well.
    # our treasure_chest list contains 4 items.
  treasure_chest = ["diamonds", "gold", "silver", "sword"]
  print("\nYou see a room with a wooden treasure chest on the left, \nand a sleeping guard on the right in front of the door")
  # Ask player what to do.
  action = input("\nDo you go for the treasure or sneak past the guard? > type TREASURE or SNEAK >")

  #check the user action
  if (action.upper() == "TREASURE"):
    choice = input("\nOooh, treasure! Open it: type YES or NO > ") 
    if (choice.upper() == "YES"):
      print("\nLet's see what's in here... /grins")
      print("\nThe chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
      print("\nYou find some")

      # FOR LOOP
      # for each treasure (variable created on the fly in the for loop)
      # in the treasure_chest list, print the treasure.
      for treasure in treasure_chest:
        print(treasure)
      treasure_num = len(treasure_chest)
      treasure_choice = input("\nTake all " + str(treasure_num) +" items? type YES or NO > ")

      if (treasure_choice.upper() == "YES"):
        for treasure in range(len(treasure_chest)):
          backpack.append(treasure_chest.remove(treasure))
        show_backpack()
      else:
        print("\nWho needs treasure, I'm outta here!")
    else:
      print("\nNo time to waste, gotta sneak past the guard!")
  else:
    print("\nThe guard is more interesting, let's go that way!")
  # PART 3 
  # Deal with the guard
  
def show_backpack():
  global backpack
  print("\nCurrently in my backpack: ")
  print(backpack)
  
# run the game
main()





