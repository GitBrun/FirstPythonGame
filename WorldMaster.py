### IMPORT THE NECESSARY LIBRAIRIES

import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 200

### SETUP THE PLAYER

class player:
    def __init__(self):
        self.name = ''
        self.solves = 0
player1 = player()

### SETUP THE MAIN MENU OPTIONS

def mainMenuOptions():
  option = input('- ')
  if option.lower() == ('Play'):
    playGame()
  elif option.lower() == ('Load'):
    loadGame()
  elif option.lower() == ('About'):
    about()
  elif option.lower() == ('Leave'):
    sys.exit()  
  while option.lower() not in ['Play', 'Load' 'About', 'Leave']:
    print("Commande invalide, veuillez réessayer.")
    option = input("- ")
    if option.lower() == ("Play"):
      playGame()
    elif option.lower() == ("Load"):
      loadGame()
    elif option.lower() == ("About"):
      about()
    elif option.lower() == ("Leave"):
      sys.exit()   

def mainMenu():
	os.system('clear')
	print('-' * 124)
	print('- Bienvenue dans Worldmaster : le jeu où le monde est à vos pieds.  -')
	print("-      Mais avant de se retrouver sur le trône, il faudra faire les bons choix...     -")
	print('-' * 124)
	print("                 .: Play :.                  ")
	print("                 .: Load :.                  ")
	print("                 .: About :.                  ")
  print("                 .: Leave :.                  ")
  print('-' * 124)
	mainMenuOptions()		

### LOAD PREVIOUS GAME BACKUP  

def loadGame():
  #todo charger une sauvegarde
  playGame()

### ABOUT THE GAME (TUTO, CREDITS...)

def about():
  print('-' * 124)
  print('-          How to play :         -')
  print('-                   -')
  print('-          Credits :          -')
  print('-          This game was created by Kylian Brun and Noé Bocquet          -')
  print('-          A special thanks to our Teacher LoÏc Janin who who accompanied us in this adventure !          -')
  print('-' * 124)
  mainMenu()

### LEAVE THE GAME

def leaveGame():
  sys.exit()

### GAMEPLAY

def playGame()
  print('-' * 124) 
  print("-          #todo date 2021, vous naissez sur la planète Erret, dans le pays de Verland.          -")
  print("-          Dès votre naissance, vous cherchez déjà à décider et choisissez votre prénom :          -")
  question_1 = "Commment vous appelez-vous? " 
	for character in question_1:
	  sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	nom_Joueur = input("> ")
	player1.name = nom_Joueur
  print("-          Votre enfance est plutôt atypique, fils de mierfer...euh de fermier, vous êtes passionné de politique.          -")
  print("-          Vous n'avez qu'un objectif dans la ive : devenir président de votre magnifique pays, et plus tard gouverner Erret.          -")
  print("-          Après de brillants résultats au llègeco et au céely, vous rejoignez la meilleure école de Verland, l'élite du pays.          -")
  print("-          L'heure de votre examen est maintenant venue, le diplôme final est la clé. Il faut absolument réussir l'examen.          -")
  print('-' * 124)
  examen()
  print('-' * 124)
  print("-          Vous êtes enfin au gouvernement, vous vous approchez peu à peu de votre ojectif.          -")  
  print("-          Tout se passe bien à votre poste mais votre rêve depuis tipeu, c'est de devenir président...           -")   
  print("-          Il faut donc que les choses s'accélèrent.          -")
  print('-' * 124)
  print("-          Un beau jour, quelqu'un vous contacte et vous fait une proposition : c'est le pays ennemi, Landver.          -")
  print("-          Il vous propose de s'allier avec lui en vous promettant vous donner des informations sur Verland qui pourront vous faire monter en grade.          -")
  print('-' * 124)
  Landver()

### STEP 1 : EXAMEN

def examen():
  print('-' * 124) 
  print("-          Voulez-vous vous rendre à l'examen ?          -")
  print('-' * 124)
  option = input('- ')
  if option.lower() == ('oui') or ('Oui'):
    passerExamen()
  elif option.lower() == ('non') or ('Non'):
    skipExamen()
  while option.lower() not in ['oui', 'Oui' 'non', 'Non']:
    print("Commande invalide, veuillez répondre par oui ou non.")
    option = input("- ")
    if option.lower() == ('oui') or ('Oui'):
      passerExamen()
    elif option.lower() == ('non') or ('Non'):
      skipExamen()