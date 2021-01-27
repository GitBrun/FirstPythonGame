# TO DO :  
# Implanter nouvelle partie du shéma 
# Flush texts qui s'écrivent
# Mise en page
# Fix about & leave

# Commenter le code 
# Nomenclature uniforme dans tout le code
# Nom joueur
# Uniforme TU et VOUS
# oui or Oui
# play or Play etc

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
    print('                                      .:Menu:.                                        ')
    print('                                      .:Play:.                                        ')
    print('                                      .:Leave:.                                       ')   
    reponse = input('-> ')
    if reponse == 'Menu':
        mainMenu()
    elif reponse == 'Play':
        playGame()
    elif reponse == 'Leave':
        sys.exit()  
    while reponse not in ['Play', 'About', 'Leave']:
        print("Commande invalide, veuillez réessayer.")
        reponse = input('-> ')
        if reponse == 'Menu':
            mainMenu()
        elif reponse == 'Play':
            playGame()
        elif reponse == 'Leave':
            sys.exit()
    
    

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
    print('======================================================================================')
    print('Entrez votre prénom : ')
    nomJoueur = input('-> ')
    print('======================================================================================')
    print('=                  Votre enfance est plutôt atypique,', nomJoueur)                    
    print('=        fils de mierfer...euh de fermier,  vous êtes passionné de politique         =')
    print('=            Vous n\'avez qu\'un objectif dans la ive : devenir président            =')
    print('=               de votre magnifique pays, et plus tard gouverner Erret.              =')
    print('=                 Après de brillants résultats au llègeco et au céely,               =')
    print('=            vous rejoignez la meilleure école de Verland, l\'élite du pays.         =')
    print('-     L\'heure de votre examen est maintenant venue, le diplôme final est la clé.    =')
    print('=                       Il faut absolument réussir l\'examen.                        =')
    print('======================================================================================')
    Jeu(nomJoueur)

def Jeu(nomJoueur):
    sante = int()
    sante = 100

    print('Début du jeu')
    
    def Examen():

        reponse = str()

        while 1:
            print('Voulez-vous vous rendre à l\'examen ', nomJoueur, ' ?')
            reponse = input('-> ')
            if reponse == 'oui' or 'Oui':
                    print('======================================================================================')
                    print('=         L\'examen est un jeu des allumettes, le principe est très simple :         =')
                    print('=  Il y a 20 allumettes, vous pouvez prendre à tour de rôle 1, 2 ou 3 allummettes.   =')
                    print('=               Si vous prenez la dernière allumette, vous échouez.                  =')
                    print('=                Vous jouerez contre Master, un joueur expérimenté                   =')
                    print('=                                 Bonne chance!                                      =')
                    print('======================================================================================')
                    allumettes=20
                    while allumettes>0:
                        joueur=-1
                        while joueur<1 or joueur>3 or joueur>allumettes:
                            joueur=int(input('Combien d\'allumettes prends tu ?')) 
                        allumettes=allumettes-joueur
                        if allumettes==0:
                            print('Vous avez échoué... Vous repasserez l\'examen l\'année prochaine.')
                            Examen()
                        else: 
                            print('Il reste ', allumettes, 'allumettes.')
                            if allumettes%4==3:
                                master=2
                            elif allumettes%4==2:
                                master=1
                            elif allumettes%4==0:
                                master=3
                            else:
                                master=1
                            print('master prends ', master, 'allumettes.')
                            allumettes=allumettes-master
                            print('il en reste ', allumettes)
                            if allumettes==0:
                                print('Félicitations, vous avez passé l\'examen, vous pouvez accéder au gouvernement !')
                                print('Bravo, Vous obtenez votre diplôme, gardez-le, il pourra vous aider pour la suite.')
            elif reponse == 'non' or 'Non':
                print('======================================================================================')
                print('=          En sortant de l\'école, vous rencontrez un homme assez louche,            =')
                print('=    après vous avoir regardé, il vous interpelle et vous commencez à discuter.      =')
                print('=            Vous parlez politique et il aime votre vision. Étant député,            =')
                print('=         il vous propose directement de le rejoindre dans le gouvernement...        =')
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
        print('=  Vous êtes enfin au gouvernement, vous vous approchez peu à peu de votre ojectif   =')
        print('=              Tout se passe bien à votre poste mais votre rêve depuis tipeu         =')
        print('=                             c\'est de devenir président...                         =')
        print('=                     Il faut donc que les choses s\'accélèrent.                     =')
        print('=                                                                                    =')
        print('=       Un beau jour, quelqu\'un vous contacte et vous fait une proposition :        =')
        print('=                            c\'est le pays ennemi, Landver.                         =')
        print('=          Il vous propose de s\'allier avec lui en vous promettant de vous          =')
        print('=    donner des informations sur Verland qui pourront vous faire monter en grade.    =')
        print('======================================================================================')
        while 1:
            print('Alors ', nomJoueur, ' acceptez-vous cette alliance ?')
            reponse = input('-> ')
            if reponse == 'oui':
                print('Trahison, guerre, votre pays vous exécute pour avoir livré des informations au pays ennemi !')
                sante = (sante - degat)
                print(sante)
                if sante == 0:
                    print('Vous êtes affaibli...')
                    Proposition(sante)
            elif reponse == 'non':
                print('Vous restez fidèle à votre pays et vous continuez votre carrière !')
                print('Le président vous remercie d\'avoir refusé cette alliance en vous offrant un masque !')
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

        print('======================================================================================')
        print('         Le président vous propose de monter en grade après votre bonne action.       ')
        print('                    Il souhaite que vous deveniez son premier ministre.               ')
        print('            Une heure plus tard, vous recevez un appel du président Enituop           ')
        print('       Il dit avoir entendu parler de vous et vous propose de devenir président.      ')
        print('        Avec corruption certes, mais vous serez directement à la tête du pays.        ')
        print('======================================================================================')

        while 1:
            print('Alors, que décidez-vous', nomJoueur, ' ? Devenez-vous premier ministre ou président ?')
            reponse = input('-> ')
            if reponse == 'premier ministre':
                print('Vous devenez premier ministre et vous avez de nouvelles responsabilités.')
            elif reponse == 'président':
                print('Vous devenez président, votre mandat ne s\'annonce pas de tout repos...')
                print('Une manifestation violente est annoncée par des opposants soupçonnant la corruption...')
                print('Quittez vous le lotipac ?')
                reponse = input('-> ')
                if reponse == 'oui':
                    print('Vous mourrez en allant en voiture à l\'aeroport.')
                    sante = sante - degat
                    print(sante)
                    if sante == 0:
                        print('Vous avez perdu...')
                        mainMenu()
                elif reponse == 'non':
                    print('Les opposants parviennent à entrer dans le lotipac et la situation est hors de contrôle.')
                    print('Vous mourrez submergé par la foule.')
                    sante = sante - degat
                    print(sante)
                    if sante == 0:
                        print('Vous avez perdu...')
                        mainMenu()
                else:
                    print('Erreur: répondez par oui ou non.')
            else:
                print('Erreur: répondez par président ou premier ministre.')
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
    
        print('Après vous être hissé au rang de premier ministre, une épidémie dévastatrice apparait: le DIVOC 19.')
        print('Des jours sombres arrivent', nomJoueur, ' , les cas augmentent et le virus est meurtier...')
        print('Comment allez-vous gérer la crise ?')
        while 1:
            print('Décidez-vous de prendre des mesures sanitaires ou partez-vous en Guyane ?')
            reponse = input('-> ')
            if reponse == 'mesures':
                sante = sante + regen
                print('Vous prenez des mesures sanitaires pour limiter la crise. Le peuple vous est reconaissant.')
                print(sante)
            elif reponse == 'fuir':
                sante = sante - degat
                print('Vous mourrez du DIVOC91 dans l\'avion')
                print(sante)
                if sante == 0:
                    print('Vous avez perdu...')
                    mainMenu()
            else:
                print('Erreur: répondez par mesures ou par fuir')
            if reponse == 'mesures' or reponse == 'fuir':
                break

    Epidemie(sante)

    print(' Vous êtes à la fin du jeu')
    
    def Findejeu(sante):
    
        reponse = str()
        degat = int()
        degat = 100
    
        print('Après avoir tout essayé pour gérer la crise sanitaire,')
        print('la situation semble inéluctable et la ruine semble être le destin d\'Erret...')
        print('Plusieurs virus et catastrophes climatiques surviennent après le DIVOC 91.')
        print('Cependant, Nole Ksum, un entrepreneur célèbre vous propose au vu de la situation.')
        print('de partir en secret avec une partie de l’humanité sur la planète Sram.')
        print('D\'un côté, vous pouvez conquérir une nouvelle planète tandis que de l\'autre,')
        print('la population vous exhorte de rester pour lutter contre la fin du monde.')   
    
        print('Vous-êtes désormais face à un choix crucial:')
        while 1:
            print('Restez-vous sur Erret ou fuyez-vous sur Sram avec Nole ?')
            reponse = input('-> ')
            if reponse == 'Erret':
                print('Vous mourrez avec 95 pour cent de la population des guerres et des tsunamis qui ravagent Erret.')
                sante = sante - degat
                print(sante)
                if sante == 0:
                    print('Vous avez perdu...')
                    mainMenu()
                return
            elif reponse == 'Sram':
                print('Vous constatez en arrivant sur Sram qu’une civilisation est déjà développé et installée.')
                print('Vous êtes acceuillis et devenez président suprême de Sram. Tout vous réussi.')
                print('$$$ BRAVO ', nomJoueur, 'YOU WIN $$$')
            else:
                print(' Il n\'y a que deux choix possibles')
            if reponse == 'Erret' or reponse == 'Sram':
                break
    
    Findejeu(sante)
    
mainMenu()

