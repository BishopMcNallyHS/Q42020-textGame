# Author name: Mr. Truong
# Version #: 0.1
# April 1, 2020

# PART 1 
# create main()
# ask the player for their name and store the INPUT into an appropriately named variable
# Greet the player by their name
#
import random #p3

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
    red_door_02()
  elif (door.upper() == "BLUE"):
    print("\nYou go through the BLUE Door")
    blue_door_03()
  else:
    start_adventure()#error check in case of bad input starts the function again

def red_door_02():
  print("\nYou see a great red dragon!!")
  dragon_move = input("\nWhat do you do? type RUN or FIGHT > ")
  if (dragon_move.upper() == "RUN"):
    start_adventure()
  elif (dragon_move.upper() == "FIGHT"):
    print("\nYou try to fight the dragon....")
    game_over("Eaten by a dragon")
  else:
    red_door_02()#error check in case of bad input starts the function again

#create game_over() that takes in a string describing the reason of the game over
def game_over(reason):
  if (reason == "win"):
    print("\nCongrats YOU WIN!!")
  else:
    print("\nWell that was silly you were " + reason)
  

# PART 2
#create blue door option
backpack = []

#p3 vars
player_HP = 10 
player_attack_power = 1 

def blue_door_03():
  global backpack
  global player_HP#p3
  global player_attack_power#p3
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
        for treasure in treasure_chest:
          if(treasure == "sword"):
            print("Nice sword! Attack Power +1")
            player_attack_power += 1
          backpack.append(treasure)
        show_backpack()
        treasure_chest.clear()
      else:
        print("\nWho needs treasure, I'm outta here!")
    else:
      print("\nNo time to waste, gotta sneak past the guard!")
  else:
    print("\nThe guard is more interesting, let's go that way!")
  # PART 3 
  # Deal with the guard
  print("\nYou try to sneak past the guard...")
  random_result = random.randint(1,10)
  guard_HP = 5
  if(random_result < 2):#10% chance stays alseep
    print("\nYou manage to sneak past the guard and through the door")
    
  elif(random_result < 5):
    print("\nYou try to sneak past the guard and through the door ")
    print("You wake him but he's not ready to fight")
    guard_attack_power = 1
    fight(guard_HP, guard_attack_power)
  else:
    print("\nYou accidentally kick the treasure chest and wake the guard")  
    print("Looks like you'll need to fight")
    guard_attack_power = 2
    fight(guard_HP, guard_attack_power)
  
  guard_door_04()

def show_backpack():
  global backpack
  print("\nCurrently in my backpack: ")
  print(backpack)

#p3
def fight(enemy_HP, enemy_attack_power):
  global player_HP
  global player_attack_power

  choice = input("\nFight? Type YES or NO > ")
  while (player_HP > 0 and choice.upper() == "YES" and enemy_HP > 0):
    #player attacks
    attack_chance = random.randint(1,10)
    if(attack_chance > 4):
      print("\nYou Hit!")
      enemy_HP -= player_attack_power
    else:
      print("\nYou Miss!")

    #enemy attacks
    attack_chance = random.randint(1,10)
    if(attack_chance > 7):
      print("\nYou're Hit!")
      player_HP -= enemy_attack_power
    else:
      print("\nEnemy Missed!")
    
    print("Player HP: " + str(player_HP))
    print("Enemy HP: " + str(enemy_HP))

    if(player_HP > 0 and enemy_HP > 0):
      choice = input("\nFight? Type YES or NO > ")

  if(enemy_HP < 1 and player_HP > 0):
    print("\nYou killed your enemy!")
    
  else:
    print("you spare your enemy")
  
  if(player_HP < 1):
    game_over(" you were killed by your enemy!!")

def guard_door_04():
  print("\nYour are now in a new room... are you free or do you continue your quest")
  choice = input("type FREEDOM or CONTINUE > ")
  if(choice.upper() == "FREEDOM"):
    game_over("win")
  elif(choice.upper() == "CONTINUE"):
    print("\nThe adventure continues...please continue coding")
  else:
    print("\nInput unknown - try again")
    guard_door_04()
# run the game
main()





