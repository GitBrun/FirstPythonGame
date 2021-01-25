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
    reponse = input('-> ')
    if reponse == 'Play':
        playGame()
    elif reponse == 'About':
        about()
    elif reponse == 'Leave':
        sys.exit()  
    while reponse not in ['Play', 'About', 'Leave']:
        print("Commande invalide, veuillez réessayer.")
        reponse = input('-> ')
        if reponse == 'Play':
            playGame()
        elif reponse == 'About':
            about()
        elif reponse == 'Leave':
            sys.exit()   

def mainMenu():
    print('======================================================================================')
    print('=          Bienvenue dans Worldmaster : le jeu où le monde est à vos pieds.          =')
    print('=     Mais avant de se retrouver sur le trône, il faudra faire les bons choix...     =')
    print('======================================================================================')
    print('                                      .:Play:.                                        ')
    print('                                      .:About:.                                       ')
    print('                                      .:Leave:.                                       ')
    mainMenuOptions()		

### ABOUT THE GAME (TUTO, CREDITS...)

def about():
    print('======================================================================================')
    print('=                                    How to play :                                   =')
    print('=                                                                                    =')
    print('=                                      Credits :                                     =')
    print('=                This game was created by Kylian Brun and Noé Bocquet                =')
    print('=                    A special thanks to our Teacher LoÏc Janin who                  =')
    print('=                           accompanied us in this adventure !                       =')
    print('======================================================================================')
    mainMenu()

### LEAVE THE GAME

def leaveGame():
    sys.exit()

### GAMEPLAY

def playGame():
    print('======================================================================================') 
    print('=       20/02/2002, vous naissez sur la planète Erret, dans le pays de Verland.      =')
    print('=   Dès votre naissance, vous cherchez déjà à décider et choisissez votre prénom :   =')
    print("=         Votre enfance est plutôt atypique, fils de mierfer...euh de fermier,       =")
    print('=                          vous êtes passionné de politique.                         =')
    print("=            Vous n'avez qu'un objectif dans la ive : devenir président              =")
    print('=               de votre magnifique pays, et plus tard gouverner Erret.              =')
    print("=                 Après de brillants résultats au llègeco et au céely,               =")
    print("=            vous rejoignez la meilleure école de Verland, l'élite du pays.          =")
    print("-      L'heure de votre examen est maintenant venue, le diplôme final est la clé.    =")
    print("=                        Il faut absolument réussir l'examen.                        =")
    print('======================================================================================')
    examen()
    print('======================================================================================')
    print("=  Vous êtes enfin au gouvernement, vous vous approchez peu à peu de votre ojectif   =")
    print("=              Tout se passe bien à votre poste mais votre rêve depuis tipeu         =")
    print("=                              c'est de devenir président...                         =")
    print("=                      Il faut donc que les choses s'accélèrent.                     =")
    print('=                                                                                    =')
    print("=       Un beau jour, quelqu'un vous contacte et vous fait une proposition :         =")
    print("=                              c'est le pays ennemi, Landver.                        =")
    print("=          Il vous propose de s'allier avec lui en vous promettant de vous           =")
    print('=    donner des informations sur Verland qui pourront vous faire monter en grade.    =')
    print('======================================================================================')
    #Landver()

### STEP 1 : EXAMEN

def examen():
    print('======================================================================================')
    print("=                       Voulez-vous vous rendre à l'examen ?                         =")
    print('======================================================================================')
    option = input('-> ')
    if option.lower() == ('oui') or ('Oui'):
        passerExamen()
    elif option.lower() == ('non') or ('Non'):
        skipExamen()
    while option.lower() not in ['oui', 'Oui' 'non', 'Non']:
        print("Commande invalide, veuillez réessayer.")
        if option.lower() == ('oui') or ('Oui'):
            passerExamen()
        elif option.lower() == ('non') or ('Non'):
            skipExamen()

def passerExamen():
    print('======================================================================================')
    print("=         L'examen est un jeu des allumettes, le principe est très simple :          =")
    print("=  Il y a 21 allumettes, vous pouvez prendre à tour de rôle 1, 2 ou 3 allummettes.   =")
    print("=               Si vous prenez la dernière allumette, vous échouez.                  =")
    print("=                Vous jouerez contre Master, un joueur expérimenté                   =")
    print("=                                 Bonne chance!                                      =")
    print('======================================================================================')
    allumettes=21
    while allumettes>0:
        joueur=-1
        while joueur<1 or joueur>3 or joueur>allumettes:
            joueur=int(input("Combien d'allumettes prends tu ?")) 
        allumettes=allumettes-joueur
        if allumettes==0:
            print("Vous avez échoué... Vous repasserez l'examen l'année prochaine.")
            passerExamen()
        else: 
            print("Il reste ", allumettes, "allumettes.")
            if allumettes%4==3:
                master=2
            elif allumettes%4==2:
                master=1
            elif allumettes%4==0:
                master=3
            else:
                master=1
            print("master prends ", master, "allumettes.")
            allumettes=allumettes-master
            print("il en reste ", allumettes)
            if allumettes==0:
                print("Félicitations, vous avez passé l'examen, vous pouvez accéder au gouvernement !")
    

def skipExamen():
    print('======================================================================================')
    print("=           En sortant de l'école, vous rencontrez un homme assez louche,            =")
    print("=    après vous avoir regardé, il vous interpelle et vous commencez à discuter.      =")
    print("=            Vous parlez politique et il aime votre vision. Étant député,            =")
    print("=         il vous propose directement de le rejoindre dans le gouvernement...        =")
    print('======================================================================================')
        
mainMenu()


