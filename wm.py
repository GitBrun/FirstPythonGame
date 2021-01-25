### IMPORT THE NECESSARY LIBRAIRIES

import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 200

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
    Jeu()

def Jeu():
    sante = int()
    sante = 100

    print('Début du jeu')
    
    def Examen():

        reponse = str()

        while 1:
            print('Voulez-vous vous rendre à l\'examen ?')
            reponse = input("-> ")
            if reponse == 'oui':
                    print('======================================================================================')
                    print("=         L'examen est un jeu des allumettes, le principe est très simple :          =")
                    print("=  Il y a 20 allumettes, vous pouvez prendre à tour de rôle 1, 2 ou 3 allummettes.   =")
                    print("=               Si vous prenez la dernière allumette, vous échouez.                  =")
                    print("=                Vous jouerez contre Master, un joueur expérimenté                   =")
                    print("=                                 Bonne chance!                                      =")
                    print('======================================================================================')
                    allumettes=20
                    while allumettes>0:
                        joueur=-1
                        while joueur<1 or joueur>3 or joueur>allumettes:
                            joueur=int(input("Combien d'allumettes prends tu ?")) 
                        allumettes=allumettes-joueur
                        if allumettes==0:
                            print("Vous avez échoué... Vous repasserez l'examen l'année prochaine.")
                            Examen()
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
            elif reponse == 'non':
                print('======================================================================================')
                print("=           En sortant de l'école, vous rencontrez un homme assez louche,            =")
                print("=    après vous avoir regardé, il vous interpelle et vous commencez à discuter.      =")
                print("=            Vous parlez politique et il aime votre vision. Étant député,            =")
                print("=         il vous propose directement de le rejoindre dans le gouvernement...        =")
                print('======================================================================================')
            else:
                print('Erreur: répondez par oui ou non.')
            if reponse == 'oui' or reponse == 'non':
                break
    Examen()

    print('2ème étape du jeu')
    
    def Proposition(sante):
    
        degat = int()
        reponse = str()
    
        degat = 100
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
        while 1:
            print('Acceptez-vous cette alliance ?')
            reponse = input()
            if reponse == 'oui':
                print('Trahison, guerre, votre pays vous exécute pour avoir livré des informations au pays ennemi !')
                sante = (sante - degat)
                print(sante)
                if sante == 0:
                    print('Vous avez perdu...')
                    mainMenuOptions()
            elif reponse == 'non':
                print('Vous restez fidèle à votre pays et vous continuez votre carrière !')
                print(' Le président vous remercie d\'avoir refusé cette alliance en vous offrant un masque !')
            else:
                print('Erreur: répondez par oui ou non.')
            if reponse == 'oui' or reponse == 'non':
                break

    Proposition(sante)

    print('3ème étape du jeu')
    
    def Choix(sante):
    
        reponse = str()
        degat = int()
        degat = 100
    
        print('Vous pouvez devenir 1er ministre, ou via la corruption vous pouvez devenir président...')

        print('Que décidez vous ?')
        while 1:
            print('Vous devenez premier ministre ou président ?')
            reponse = input()
            if reponse == 'premier ministre':
                print('Vous devenez premier ministre et vous avez de nouvelles responsabilités')
            elif reponse == 'président':
                print('Vous devenez président, votre mandat ne s\'annonce pas de tout repos...')
                print('Une manifestation violente est annoncée par des opposants soupçonnant la corruption...')
                print('Quittez vous le lotipac (oui ou non)')
                reponse = input()
                if reponse == 'oui':
                    print('Vous mourrez en allant en voiture à l\'aeroport')
                    sante = sante - degat
                    print(sante)
                    if sante == 0:
                        print(' Vous avez perdu !')
                    quit()
                elif reponse == 'non':
                    print('Vous mourrez submergés par la foule')
                    sante = sante - degat
                    print(sante)
                    if sante == 0:
                        print(' Vous avez perdu !')
                    quit()
                else:
                    print('Erreur répondez oui ou non')
            else:
                print('Erreur seulement deux choix disponibles')
            if reponse == 'premier ministre':
                break

    Choix(sante)
    
    print('Vous êtes à l\'étape 4 du jeu')
    
    def Epidemie(sante):

        reponse = str()
        degat = int()
        regen = int()
        degat = 100
        regen = 100
    
        print('Après vous êtes haussés au rang de premier ministre, une épidémie dévastatrice apparait : le DIVOC 19, des jours sombres arrivent, comment allez vous gérer la crise ?')

        print('Comment gérez - vous la crise ?')
        while 1:
            print('Vous prenez des mesures sanitaires, ou vous fuyez en Guadeloupe')
            reponse = input()
            if reponse == 'mesures':
                sante = sante + regen
                print('Vous prenez des mesures sanitaires pour limiter la crise.')
                print(sante)
            elif reponse == 'fuir':
                sante = sante - degat
                print('Vous mourrez du DIVOC91 dans l\'avion')
                print(sante)
                if sante == 0:
                    print(' Vous avez perdu !')
                    quit()
            else:
                print('Erreur il n\'y a que deux choix disponibles.')
            if reponse == 'mesures' or reponse == 'fuir':
                break

    Epidemie(sante)

    print(' Vous êtes à la fin du jeu')
    
    def Findejeu(sante):
    
        reponse = str()
        degat = int()
        degat = 100
    
        print('Après avoir tout essayer pour gérer la crise sanitaire, la situation semble inéluctable et la ruine semble être le destin de Erret,')
        print('Cependant un entrepreneur Nole Ksum vous propose de vous enfuir avec lui sur Sram, tandis que la population vous exhorte de rester pour lutter contre la fin du monde')
        print('Que décidez vous ? Rester et lutter pour votre pays ou vous enfuir comme un lâche ?')
   
    
        print('Que choisissez vous ?')
        while 1:
            print('Vous restez sur Erret, ou vous fuyez sur Sram')
            reponse = input()
            if reponse == 'Erret':
                print('Vous mourrez sur Erret de maladie comme tous les gueux')
                sante = sante - degat
                print(sante)
                if sante == 0:
                    print(' Vous avez perdu !')
                    quit()
                return
            elif reponse == 'Sram':
                print('Vous partez sur Sram et après de nombreux assassinats qui n\'ont aucun rapport avec vous, vous vous hissez au rang de président suprême')
            else:
                print(' Il n\'y a que deux choix possibles')
            if reponse == 'Erret' or reponse == 'Sram':
                break
    
mainMenu()

