#---------imports--------------------------------------------------------------------
 
from colorama import Fore, Back, init, Style
init(autoreset=True)
import sys
from gametext import *
#---------code / game---------------------------------------------------------------------
def intro():
 print("This is a text-based turn based game")

 print("\nYou will have to make choices, based on these the game will play out differently\
        \nThere will be enemies that you have to defeat, and items to collect.\n")
def game_over():
   print("You have fought valiantly, but unfortunately enough.... you have died.")
   exit

def press_enter():
 while True:
  a = input("Press ENTER to continue ")
  if a == "":
    return 
  else:
    print("Invalid input")

def menu():
   print("1. View inventory")
   print("2. Exit menu")

def choice():
 while True:
  choice = input("Choose between (1-2): ")
  if choice in ["1", "2"]:
   return choice
  else:
   print("Invalid input.")


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

def encounter(enemy_damage, enemy_health, enemy, difficulty):     #Encounter pos: 1 enemy damage, 2 enemy health, 3 enemy name, 4 difficulty(dificulty from 1-10)
 from random import randrange
 global player_health
 global player_armor
 global player_damage_full  #the last three globals are to access the player variables
 player_damage = player_damage_full
 if player_armor > 0: # armor reduces enemy damage(necessary because otherwise the damage gets divided by 0)
        enemy_damage -= (enemy_damage / player_armor)
 enemy_action = 0 #indicator for enemy action from 1 to 10
 turn = 1 #turn indicator 1 = player turn, 2 = enemy turn
 
 while player_health > 0 and enemy_health > 0:
    print(f"\nMario's health is: {player_health} {enemy}'s health is: {enemy_health}") #display status of player and enemy
    if turn == 1: # player turn
        print(Fore.GREEN + "Mario's turn:", turn)
        turn += 1
        while True:
         choice = input('1: attack or 2: block: ') #player choice input
         if choice in ['1', '2']:
             choice = int(choice)
             break
         else:
            print("Invalid input, try again.")
   
        if choice == 1: #player attack
            enemy_health -= player_damage
            player_damage = player_damage_full #reset player damage after attack so it doesn't stay reduced after blocking
            print('\nMario attacks the', enemy)
            print(f"{enemy}'s health is now: ",max(0, enemy_health)) #display enemy health after attack
            if enemy_health <= 0:
               print(f"{Fore.RED + Style.BRIGHT + (enemy)} has been defeated\n") #enemy defeated message
               break
        elif choice == 2: #player block
            enemy_damage -= 5 #reduce enemy damage for next attack
            player_damage = player_damage_full #reset player damage after blocking so it doesn't stay reduced after blocking
            print(f"\nMario will block the {enemy}'s next attack")
    elif turn == 2: # enemy turn
        print(Fore.RED + f"{enemy}'s turn: {turn}")
        turn -= 1
        enemy_action = randrange(1, 11) #random enemy action from 1 to 10 #lower is attack, higher is block
        if enemy_action <= difficulty: #enemy attack
           player_health -= enemy_damage
           enemy_damage = enemy1_damage #reset enemy damage after attack so it doesn't stay reduced after blocking
           if player_health <= 0: #check if player is dead
              game_over()
              sys.exit(0)
             
        elif enemy_action > difficulty: #enemy block
           player_damage = max(0, player_damage_full - 10) #reduce player damage for next attack
           enemy_damage = enemy1_damage #reset enemy damage after blocking so it doesn't stay reduced after blocking
           print(enemy, 'blocks') #nog functie bijzetten als input error is


def game():
 
 intro_to_story()
 user_choice = choice()
 if user_choice == "1":
  sewer_hat() # sewer direction with hat
  global player_armor
  player_armor += 10 # adds 10 to the base playerarmor
 elif user_choice == "2":
  sewer_wpn_pipe() # sewer direction with pipe
  global player_damage_full
  player_damage_full += 10 # adds 10 to the base playerdamage
  
 
 press_enter()
  
 text_after_sewer() # text after either choices of sewer
 press_enter()
 encounter(enemy1_damage, enemy1_health, enemy1, 2) # encounter 1 (goomba)
 
 press_enter()
 goomba_defeated() # text after goomba has been defeated
 while True:
    userchoice = choice()   
    if userchoice == "1":
        choice_after_goomba_garden() # choice after goomba defeated is direction garden
        second_choice = choice()
        if second_choice == "1":
            garden_left1() # first part of text left choice garden
            press_enter()
            garden_left2() # second part of text left choice garden
            player_damage_full += 5 # adds 5 to the base playerdamage
            break
        
        elif second_choice == "2":
            garden_right() # text for right choice garden
            press_enter()
            encounter(enemy2_damage, enemy2_health, enemy2_2, 4) # encounter 2 (piranha plant)
            press_enter()
            piranha_defeated() # text for when piranha plant has been defeated
            press_enter()
            break
        
            
    
    elif userchoice == "2":
        choice_after_goomba_prison() # text for when choice after goomba encounter is right (prison)
        press_enter()
        continuation_prison() # extra text for prison
        user_choice_chambers = choice()
        if user_choice_chambers == "1":
           prison_pharmacy1() # text for choice is left (prison pharmacy)
           press_enter()
           prison_pharmacy2() # extra text for pharmacy
           global player_health
           player_health = 100 # player got healing item, health is fully restored
           break

        elif user_choice_chambers == "2":
           prison_mortuary() # text for  choice is right (prison mortuary)
           press_enter()
           encounter(enemy2_damage, enemy2_health, enemy2_1, 4)    # encounter 2 (Boo)
           press_enter()
           boo_defeated()    # text for when boo is defeated     
        break
    
 press_enter()
 before_castle_door() # text for when before the castle gates
 press_enter()
 encounter(boss_damage, boss_health, boss, 6) # encounter 3 (Bowser)
 press_enter()
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
