#---------imports--------------------------------------------------------------------
from os import *
import os
from colorama import Fore, Back, init, Style
init(autoreset=True)
import sys
from gametext import *
from asciitests import *

#---------code / game---------------------------------------------------------------------
def intro():
 print("This is a text-based turn based game")

 print("\nYou will have to make choices, based on these the game will play out differently\
        \nThere will be enemies that you have to defeat, and items to collect.\n")

def press_enter():
 while True:
  a = input("Press ENTER to continue ")
  if a == "":
    return 
  else:
    print("Invalid input")

def game_over():
   print("You have fought valiantly, but unfortunately enough.... you have died.")
   press_enter()
   exit
#adds an item to the inventory based on the item argument, only use items that are in all_items
def add_to_inventory(item):
    items = all_items()
    if item in items:
        player_inventory[item] = items[item]

#prints the item and the description of the items in the inventory
def view_inventory():
    print("\n--- INVENTORY ---")
    if not player_inventory:
        print("Inventory is empty.")
    else:
        for item, description in player_inventory.items():
            print(f"{item}: {description}")

def wait(x):
    time.sleep(x)  


def menu():
    def options():
        print("\n--- MENU ---")
        print("1. View inventory")
        print("2. View map")
        print("3. Exit menu")
    options()
    while True:
        user_choice = input("Enter your choice (1-3): ")
        if user_choice == "1":
            view_inventory()
            options()
        elif user_choice == "2":
            print("You don't have a map of this place.")
            options()
        elif user_choice == "3":
            print("Exiting menu..\n")
            break
        else:
            print("Invalid input. Try again.")

def choice():
    while True:
        user_input = input("Choose between (1-2) or type 'menu': ")
        if user_input in ["1", "2"]:
            return user_input
        elif user_input.lower() == "menu":
            menu()
        else:
            print("Invalid input. Try again.")


def status(player_health, enemy, enemy_health):
    print(f"\nMario's health is: {player_health} {enemy}'s health is: {enemy_health}") #display status of player and enemy
    wait(1.5)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_quit():
 print("1. Start the game")
 print("2. Quit the game.")


# player / mario variables
player = "Mario"
player_health = 100
player_damage_full = 25
player_armor = 0
 
# enemy 1 goomba
enemy1 = "Goomba"
enemy1_health = 50
enemy1_damage = 10
 
# enemy 2 ghost / piranha plant
enemy2_1 = 'Ghost'
enemy2_2 = 'Piranha plant'
enemy2_health = 80
enemy2_damage = 20

#enemy boss bowser
boss = 'Bowser' 
boss_health = 150
boss_damage = 35

player_inventory = {}

def encounter(enemy_damage, enemy_health, enemy, difficulty):     #Encounter pos: 1 enemy damage, 2 enemy health, 3 enemy name, 4 difficulty(dificulty from 1-10(enemy attacks x out of 10))
 from random import randrange
 global player_health
 global player_armor
 global player_damage_full  #the last three globals are to access the player variables
 player_damage = player_damage_full
 original_damage = enemy_damage
 if player_armor > 0: # armor reduces enemy damage(necessary because otherwise the damage gets divided by 0)
    enemy_damage -= (enemy_damage / player_armor)
 enemy_action = 0 #indicator for enemy action from 1 to 10
 turn = 1 #turn indicator 1 = player turn, 2 = enemy turn
 
 
 while player_health > 0 and enemy_health > 0:
    status(player_health, enemy, enemy_health)
    crit = False
   
 
    if turn == 1: # player turn
        enemy_action = randrange(1, 11) #random enemy action from 1 to 10 #lower is attack, higher is block
 
        if enemy_action <= difficulty:
            print(Fore.RED + f"{enemy} will attack in their turn") #enemy attack message
        elif enemy_action > difficulty and enemy_action < 10:
            print(Fore.RED + f"{enemy} will block in their turn") #enemy block message
        elif enemy_action == 10:
            print(Fore.RED + f"{enemy} hides their intent") #enemy hides intent message
            enemy_action = randrange(1, 11) + 1  # random intent
 
        wait(1)
 
        print(Fore.GREEN + "Mario's turn:", turn)
        turn += 1
        player_choice = choice()
   
        if player_choice == '1': #player attack
            attack = randrange(1, 11)
            if attack == 10:
               player_damage *= 1.5
               crit = True
            enemy_health -= player_damage
            player_damage = player_damage_full #reset player damage after attack so it doesn't stay reduced after blocking
            print('\nMario attacks the', enemy)
            wait(1)
            if crit == True:
               print('Critical strike!')
               wait(1)
            print(f"{enemy}'s health is now: ",max(0, enemy_health)) #display enemy health after attack
            wait(2)
 
            if enemy_health <= 0:
               print(f"{Fore.RED + Style.BRIGHT + (enemy)} has been defeated\n") #enemy defeated message
               return player_health
 
        elif player_choice == '2': #player block
            enemy_damage -= 5 #reduce enemy damage for next attack
            player_damage = player_damage_full #reset player damage after blocking so it doesn't stay reduced after blocking
            print(f"\nMario will block the attack in the next turn")
            wait(2)
 
    elif turn == 2: # enemy turn
        print(Fore.RED + f"{enemy}'s turn: {turn}")
        turn -= 1
        wait(2)
 
        if enemy_action <= difficulty: #enemy attack
           print(enemy, 'attacks Mario')
           player_health -= enemy_damage
           enemy_damage = original_damage #reset enemy damage after attack so it doesn't stay reduced after blocking
           wait(2)
 
           if player_health <= 0: #check if player is dead
              game_over()
              sys.exit(0)
             
        elif enemy_action > difficulty: #enemy block
           player_damage = max(0, player_damage_full - 10) #reduce player damage for next attack
           enemy_damage = original_damage #reset enemy damage after blocking so it doesn't stay reduced after blocking
           print(enemy, 'blocks')
           wait(2)
    clear()


def game():
 clear()
 intro_to_story()
 user_choice = choice()
 if user_choice == "1":
  clear()
  sewer_hat() # sewer direction with hat
  global player_armor
  player_armor += 10 # adds 10 to the base playerarmor
  add_to_inventory("Red hat")
 elif user_choice == "2":
  clear()
  sewer_wpn_pipe() # sewer direction with pipe
  global player_damage_full
  player_damage_full += 10 # adds 10 to the base playerdamage
  add_to_inventory("Pipe")
  
 
 press_enter()
 clear() 
 text_after_sewer() # text after either choices of sewer
 press_enter()
 encounter(enemy1_damage, enemy1_health, enemy1, 2) # encounter 1 (goomba)
 
 press_enter()
 clear()
 goomba_defeated() # text after goomba has been defeated
 while True:
    userchoice = choice()   
    if userchoice == "1":
        clear()
        choice_after_goomba_garden() # choice after goomba defeated is direction garden
        second_choice = choice()
        if second_choice == "1":
            clear()
            garden_left1() # first part of text left choice garden
            press_enter()
            clear()
            garden_left2() # second part of text left choice garden
            player_damage_full += 5 # adds 5 to the base playerdamage
            add_to_inventory("Red mushroom")
            break
        
        elif second_choice == "2":
            clear()
            garden_right() # text for right choice garden
            press_enter()
            clear()
            encounter(enemy2_damage, enemy2_health, enemy2_2, 4) # encounter 2 (piranha plant)
            press_enter()
            clear()
            piranha_defeated() # text for when piranha plant has been defeated
            press_enter()
            break
        
            
    
    elif userchoice == "2":
        clear()
        choice_after_goomba_prison() # text for when choice after goomba encounter is right (prison)
        press_enter()
        continuation_prison() # extra text for prison
        user_choice_chambers = choice()
        if user_choice_chambers == "1":
           clear()
           prison_pharmacy1() # text for choice is left (prison pharmacy)
           press_enter()
           clear()
           prison_pharmacy2() # extra text for pharmacy
           global player_health
           player_health = 100 # player got healing item, health is fully restored
           break

        elif user_choice_chambers == "2":
           clear()
           prison_mortuary() # text for  choice is right (prison mortuary)
           press_enter()
           clear()
           encounter(enemy2_damage, enemy2_health, enemy2_1, 4)    # encounter 2 (Boo)
           press_enter()
           clear()
           boo_defeated()    # text for when boo is defeated     
        break
    
 press_enter()
 clear()
 before_castle_door() # text for when before the castle gates
 press_enter()
 clear()
 encounter(boss_damage, boss_health, boss, 6) # encounter 3 (Bowser)
 press_enter()
 clear()
 bowser_defeated() # text for when Bowser is defeated
 press_enter()
 print(Style.BRIGHT + "THE END")
 sys.exit(0)
       


if __name__ == "__main__":
    while True:
        intro()
        start_quit()
        userchoice = choice()
        if userchoice == "1":
            game()
            break
        elif userchoice == "2":
            print("Bye, bye!")
            break
