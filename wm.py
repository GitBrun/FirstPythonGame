### IMPORTATION DES LIBRAIRIES 

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
    print('                                                                                      ')
    textAbout = """Comment jouer :
Ce jeu est un RPG textuel dont vous êtes le héros, vous allez faire des choix pour avancer dans l'aventure.
Pour faire ces choix laissez-vous guidez et répondez textuellement dans l'input qui apparaîtra.
Si votre formulation est invalide, il vous sera expliqué comment répondre.
Vous pouvez acquérir des objets dans votre inventaire. Vous pourrez les utiliser qu'une seule fois par la suite.
Vous avez 100 points de vie. En fonction de vos choix, vous pouvez soit en gagner soit en perdre.
Vous mourrez lorsque vos points de vie sont à 0.

Crédits :
Ce jau a été pensé et créé par Kylian Brun et Noé Bocquet
Nous tenons à remercier tout particulièrement notre professeur Loïc Janin qui nous à accompagné dans cette aventure !"""
    for char in textAbout:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print('                                                                                      ')
    print('======================================================================================')
    print('                                                                                      ')
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
        print('                                      ')
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

### OPTIONS DU MENU ###

def mainMenuOptions():
    reponse = input('-> ')
    if reponse == 'Play':
        playGame()
    elif reponse == 'About':
        about()
    elif reponse == 'Leave':
        sys.exit()  
    while reponse not in ['Play', 'About', 'Leave']:
        print('                                      ')
        print("Commande invalide, veuillez réessayer.")
        reponse = input('-> ')
        if reponse == 'Play':
            playGame()
        elif reponse == 'About':
            about()
        elif reponse == 'Leave':
            sys.exit()

### FENETRE D'ARRIVÉE SUR LE JEU ###

def mainMenu():
    print('======================================================================================')
    print('                                                                                      ')
    textMenu = """       Bienvenue dans Worldmaster : le jeu où le monde est à vos pieds.
    Mais avant de se retrouver sur le trône, il faudra faire les bons choix..."""
    for char in textMenu:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print('                                                                                      ')
    print('======================================================================================')
    print('                                                                                      ')
    print('                                      .:Play:.                                        ')
    print('                                      .:About:.                                       ')
    print('                                      .:Leave:.                                       ')
    mainMenuOptions()

### DÉBUT DU JEU ###

def playGame():
    print('======================================================================================') 
    print('                                                                                      ')
    textPlayGame = """20/02/2002, vous naissez sur la planète Erret, dans le pays de Verland.
Dès votre naissance, vous cherchez déjà à décider et choisissez votre prénom.
Entrez votre prénom :"""
    for char in textPlayGame:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print('                                                                                      ')
    print('======================================================================================')
    print('                                                                                      ')
    nomJoueur = input('-> ')
    textPrenom = "Votre enfance est plutôt atypique ", nomJoueur, "."
    for char in textPrenom:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    textIntro = """ Fils de mierfer...euh de fermier, vous êtes passionné de politique.
Vous n\'avez qu\'un objectif dans la ive : devenir président de votre magnifique pays, et plus tard gouverner Erret.
Après de brillants résultats au llègeco et au céely, vous rejoignez la meilleure école de Verland, l\'élite du pays.
L\'heure de votre examen est maintenant venue, le diplôme final est la clé.
Il faut absolument réussir l\'examen."""  
    for char in textIntro:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print('                                                                                      ')
    print('======================================================================================')
    Jeu(nomJoueur)

### FONCTION GLOBALE DU JEU, CONTIENT LES FONCTIONS QUI CORRESPONDENT A CHAQUE ÉTAPE DU JEU ###

def Jeu(nomJoueur):

    ### INSTARAUTION DES PV ET DE L'INVENTAIRE ###

    sante = int()
    sante = 100
    inventaire = ["clés","téléphone"]

    ### 1ERE ÉTAPE : L'EXAMEN ###

    def Examen(sante, inventaire):

        reponse = str()

        while 1:
            print('                                                                                      ')
            textPrenom2 = "Voulez-vous vous rendre à l\'examen " , nomJoueur, " ?"
            print('                                                                                      ')
            for char in textPrenom2:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
            print('                                                                                      ')
            reponse = input('-> ')
            if reponse == 'oui':
                    print('======================================================================================')
                    print('                                                                                      ')
                    textExamen = """L\'examen est un jeu des allumettes, le principe est très simple :
Il y a 20 allumettes, vous pouvez prendre à tour de rôle 1, 2 ou 3 allummettes.
Si vous prenez la dernière allumette, vous échouez.
Vous jouerez contre Master, un joueur expérimenté.
Bonne chance !"""
                    for char in textExamen:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    print('                                                                                      ')
                    print('======================================================================================')

                    ### JEU DES ALLUMETTES ###

                    allumettes=20
                    while allumettes>0:
                        joueur=-1
                        while joueur<1 or joueur>3 or joueur>allumettes:
                            print('                                                                                      ')
                            joueur=int(input('Combien d\'allumettes prends tu ?')) 
                        allumettes=allumettes-joueur
                        if allumettes==0:
                            print('                                                                 ')
                            print('Vous avez échoué... Vous repasserez l\'examen l\'année prochaine.')
                            print('                                                                 ')
                            Examen(sante, inventaire)
                        else:
                            print('                                                                 ')
                            print('Il reste ', allumettes, 'allumettes.')
                            print('                                                                 ')
                            if allumettes%4==3:
                                master=2
                            elif allumettes%4==2:
                                master=1
                            elif allumettes%4==0:
                                master=3
                            else:
                                master=1
                            print('                                                                  ')
                            print('master prends ', master, 'allumettes.')
                            allumettes=allumettes-master
                            print('                                                                 ')
                            print('il en reste ', allumettes)
                            print('                                                                 ')
                            if allumettes==0:

                                textExamRéussi = """Félicitations, vous avez passé l\'examen, vous pouvez accéder au gouvernement !
Bravo, Vous obtenez votre diplôme, gardez-le, il pourra vous aider pour la suite."""
                                for char in textExamRéussi:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                inventaire.append('diplôme')
                                print('                                                             ')
                                print('Vous possédez maintenant dans votre inventaire : ', inventaire)
            elif reponse == 'non' or 'Non':
                print('                                                                    ')
                textSkipExam = """En sortant de l\'école, vous rencontrez un homme assez louche, après vous avoir regardé, 
il vous interpelle et vous commencez à discuter. Vous parlez politique et il aime votre vision.
Étant député, il vous propose directement de le rejoindre dans le gouvernement..."""
                for char in textSkipExam:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
            else:
                print('Erreur: répondez par oui ou non.')
            if reponse == 'oui' or reponse == 'non':
                break
    Examen(sante, inventaire)

    ## 2EME ETAPE DU JEU : PROPOSITION D'ALLIANCE ##
    
    def Proposition(sante, inventaire):
    
        degat = int()
        reponse = str()
    
        degat = 50
        print('======================================================================================')
        print('                                                                                      ')
        textProposition = """Vous êtes enfin au gouvernement, vous vous approchez peu à peu de votre ojectif.
Tout se passe bien à votre poste mais votre rêve depuis tipeu, c\'est de devenir président...
Il faut donc que les choses s\'accélèrent.

Un beau jour, quelqu\'un vous contacte et vous fait une proposition : c\'est le pays ennemi, Landver.
Il vous propose de s\'allier avec lui en vous promettant de vous donner des 
informations sur Verland qui pourront vous faire monter en grade."""
        for char in textProposition:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print('                                                                                      ')
        print('======================================================================================')
        print('                                                                                      ')
        while 1:
            print('Alors ', nomJoueur, ' acceptez-vous cette alliance ?')
            reponse = input('-> ')
            if reponse == 'oui':
                print('                                                                                            ')
                textTrahison = """Trahison, guerre, vous prenez une balle dans la jambe pour avoir livré des informations au pays ennemi !"""
                print('                                                                                            ')
                for char in textTrahison:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                sante = (sante - degat)
                print('                                                                                            ')
                print('Vous perdez', degat, ' points de vie')
                print('Il vous reste', sante, ' points de vie.')
                if sante == 50:
                    print('                                                                                            ')
                    print('Vous êtes affaibli...')
                    print('                                                                                            ')
            elif reponse == 'non':
                textMasque = """Vous restez fidèle à votre pays et vous continuez votre carrière !
Le président vous remercie d\'avoir refusé cette alliance en vous offrant un masque !"""
                for char in textMasque:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                inventaire.append('masque')
                print('                                                                                           ')
                print('Vous possédez maintenant dans votre inventaire : ', inventaire)
            else:
                print('Erreur: répondez par oui ou non.')
            if reponse == 'oui' or reponse == 'non':
                break

    Proposition(sante, inventaire)

    ### 3EME ÉTAPE DU JEU : PRÉSIDENT OU 1ER MINISTRE ###
    
    def Choix(sante):
    
        reponse = str()
        degat = int()
        degat = 100

        print('======================================================================================')
        print('                                                                                      ')
        textChoix = """Le président vous propose de monter en grade après votre bonne action.
Il souhaite que vous deveniez son premier ministre.
Une heure plus tard, vous recevez un appel du président Enituop.
Il dit avoir entendu parler de vous et vous propose de devenir président.
Avec corruption certes, mais vous serez directement à la tête du pays."""
        for char in textChoix:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print('                                                                                      ')
        print('======================================================================================')

        while 1:
            print('                                                                                     ')
            print('Alors, que décidez-vous', nomJoueur, ' ? Devenez-vous premier ministre ou président ?')
            print('                                                                                     ')
            reponse = input('-> ')
            if reponse == 'premier ministre':
                print('                                                                        ')
                print('Vous devenez premier ministre et vous avez de nouvelles responsabilités.')
                print('                                                                        ')
            elif reponse == 'président':
                textManif = """Vous devenez président, votre mandat ne s\'annonce pas de tout repos...
Une manifestation violente est annoncée par des opposants soupçonnant la corruption...
Quittez vous le lotipac ?"""
                for char in textManif: 
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                reponse = input('-> ')
                if reponse == 'oui':
                    print('                                                                                            ')
                    print('Vous mourrez en allant en voiture à l\'aeroport.')
                    print('                                                                                            ')
                    sante = sante - degat
                    print('                                                                                            ')
                    print('Vous perdez', degat, ' points de vie')
                    print('Il vous reste', sante, ' points de vie.')
                    print('                                                                                            ')
                    if sante == 0:
                        print('Vous avez perdu...')
                        print('                                                                                            ')
                        mainMenu()
                elif reponse == 'non':
                    print('                                                                                            ')
                    print('Les opposants parviennent à entrer dans le lotipac et la situation est hors de contrôle.')
                    print('Vous mourrez submergé par la foule.')
                    print('                                                                                            ')
                    sante = sante - degat
                    print('                                                                                            ')
                    print('Vous perdez', degat, ' points de vie')
                    print('Il vous reste', sante, ' points de vie.')
                    print('                                                                                            ')
                    if sante == 0:
                        print('Vous avez perdu...')
                        print('                                                                                            ')
                        mainMenu()
                else:
                    print('Erreur: répondez par oui ou non.')
            else:
                print('Erreur: répondez par président ou premier ministre.')
            if reponse == 'premier ministre':
                break

    Choix(sante)

    ### 4EME ÉTAPE DU JEU : ARRIVÉE DE L'ÉPIDÉMIE ###
    
    def Epidemie(sante, inventaire):

        reponse = str()
        degat = int()
        regen = int()
        degat = 100
        regen = 50
    
        print('======================================================================================')
        print('                                                                                      ')
        textVirus = """Après vous être hissé au rang de premier ministre, une épidémie dévastatrice apparait: le DIVOC 19.
Des jours sombres arrivent, les cas augmentent et le virus est meurtier...
Comment allez-vous gérer la crise ?"""
        for char in textVirus:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print('                                                                                      ')
        print('======================================================================================')
        while 1:
            print('                                                                                            ')
            print('Décidez-vous de prendre des mesures sanitaires ou partez-vous en Guyane ?')
            reponse = input('-> ')
            if reponse == 'mesures':
                sante = sante + regen
                print('                                                                                            ')
                print('Vous prenez des mesures sanitaires pour limiter la crise. Le peuple vous est reconaissant.')
                print('                                                                                            ')
                print('Vous gagnez', regen, ' points de vie')
                print('Il vous reste', sante, ' points de vie.')
                print('                                                                                            ')
                print('======================================================================================')
                print('                                                                                      ')
                textFinJeu = """Après avoir tout essayé pour gérer la crise sanitaire,
la situation semble inéluctable et la ruine semble être le destin d\'Erret...
Plusieurs virus et catastrophes climatiques surviennent après le DIVOC 91
Cependant, Nole Ksum, un entrepreneur célèbre vous propose au vu de la situation.
de partir en secret avec une partie de l’humanité sur la planète Sram.
D\'un côté, vous pouvez conquérir une nouvelle planète tandis que de l\'autre,
la population vous exhorte de rester pour lutter contre la fin du monde.
Vous-êtes désormais face à un choix crucial:"""
                for char in textFinJeu:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.03)
                print('                                                                                      ')
                print('======================================================================================')
                while 1:
                    print('                                                                                            ')
                    print('Restez-vous sur Erret ou fuyez-vous sur Sram avec Nole ?')
                    print('                                                                                            ')
                    reponse = input('-> ')
                    if reponse == 'Erret':
                        textErret = """Vous mourrez avec 95 pour cent de la population des guerres et des tsunamis qui ravagent Erret."""
                        for char in textErret:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        sante = sante - 150
                        print('Vous perdez 150 points de vie')
                        print('Il vous reste', sante, ' points de vie.')
                        if sante == 0:
                            print('                                                                                            ')
                            print('Vous avez perdu...')
                            print('                                                                                            ')
                            mainMenu()
                        return
                    elif reponse == 'Sram':
                        textSram = """Vous constatez en arrivant sur Sram qu’une civilisation est déjà développé et installée.
Vous êtes acceuillis et devenez président suprême de Sram. Tout vous réussi."""
                        for char in textSram:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('                                                                                      ')
                        print('======================================================================================')
                        print('$$$ BRAVO ', nomJoueur, 'YOU WIN $$$')
                        mainMenu()
                    else:
                        print('Erreur : répondez par Erret ou Sram')
                    if reponse == 'Erret' or reponse == 'Sram':
                        break
            elif reponse == 'fuir':
                if 'masque' in inventaire :
                    print('                                                                                            ')
                    print('Voulez-vous mettre le masque dans l\'avion ?')
                    print('                                                                                            ')
                    reponse = input('-> ')
                    if reponse == 'oui':
                        print('                                                                                            ')
                        print("Heureusement que vous avez un masque, cela vous permet de survivre au vol.")
                        print('                                                                                            ')
                        inventaire.remove('masque')
                        print('Vous possédez maintenant dans votre inventaire : ', inventaire)
                        print('                                                                                            ')
                        break
                    elif reponse == 'non':
                        sante = sante - degat
                        print('Vous perdez', degat, ' points de vie')
                        print('Il vous reste', sante, ' points de vie.')
                        print('                                                                                            ')
                        print('Vous mourrez du DIVOC91 dans l\'avion')
                        print('                                                                                            ')
                    if sante == 0:
                        print('                                                                                            ')
                        print('Vous avez perdu...')
                        print('                                                                                            ')
                        mainMenu()
                    else:
                        print('Erreur: répondez par oui ou non.')
                else:
                    sante = sante - degat
                    print('                                                                                      ')
                    print('Vous perdez', degat, ' points de vie')
                    print('Il vous reste', sante, ' points de vie.')
                    print('                                                                                            ')
                    print('Vous mourrez du DIVOC91 dans l\'avion')
                    print('                                                                                            ')
                    print(sante)
                if sante == 0:
                    print('                                                                                            ')
                    print('Vous avez perdu...')
                    print('                                                                                            ')
                    mainMenu()
            else:
                print('Erreur: répondez par mesures ou par fuir')
            if reponse == 'mesures' or reponse == 'fuir':
                break

    Epidemie(sante, inventaire)

    ### 5EME ÉTAPE DU JEU (SI GUYANE) : BREUVAGE ###

    def Breuvage(sante, inventaire):

        reponse = str()
        degat = int()
        degat = 100

        print('======================================================================================')
        print('                                                                                      ')
        textBreuvage = """Vous visitez YenneCa, la capitale. 
Vous passez près d\'un bar et un homme vous propose un cocktail local.
Acceptes tu ce breuvage  ?"""
        for char in textBreuvage:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print('                                                                                      ')
        print('======================================================================================')
        while 1:
            reponse = input('->')
            if reponse == 'oui':
                sante = sante - degat
                print('                                                                                      ')
                print('Vous perdez', degat, ' points de vie')
                print('Il vous reste', sante, ' points de vie.')
                print('                                                                                            ')
                print('Le beuvrage était trop spicy, les toilettes n\'ont pas survécu... et vous non plus')
                print('                                                                                            ')
                print(sante)
                if sante == 0 :
                    print('                                                                                            ')
                    print('Vous avez perdu')
                    print('                                                                                            ')
                    mainMenu()
            elif reponse == 'non':
                print('                                                                                            ')
                print('Vous avez bien fait, le mélange opaque n\'était pas rassurant.')
                print('                                                                                            ')
            else:
                print('Erreur: répondez par oui ou non.')
            if reponse == 'oui' or reponse == 'non':
                break

    Breuvage(sante, inventaire)

    ### DERNIERE ÉTAPE DU JEU (SI GUYANE) : FUSÉE ###

    def Fusée(sante, iventaire):

        degat = int()
        degat = 100

        print('======================================================================================')
        print('                                                                                      ')
        textFusée = """La télé du bar diffuse les informations: vous apprenez qu\'au regard de la situation catastrophique d\'Erret,
le grand entrepreneur Nole Ksum veut partir sur la planète Sram avec une partie de l\'humanité
pour fuir les catastrophes climatiques et les virus.
Il prévoit de partir en fusée de Guyane, dans la prochaine heure.
Ca tombe bien, vous êtes en Guyane et il faut à tout prix que vous partiez.
Vous arrivez sur le lieu de décollage, la sécurité vous interpelle:"""
        for char in textFusée:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print('Bonjour, ', nomJoueur, ' avez-vous un diplôme ?')
        print('                                                                                      ')
        print('======================================================================================')
        print('                                                                                            ')
        if 'diplôme' in inventaire:
            textDiplôme = """Merci, vous pouvez monter à bord.
Votre diplôme vous permet de rejoindre Nole Ksum dans la fusée et de vous en aller.
Vous constatez en arrivant sur Sram qu’une civilisation est déjà développé et installée.
Vous êtes acceuillis et devenez président suprême de Sram. Tout vous réussi."""
            for char in textDiplôme:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
            print('                                                                                      ')
            print('======================================================================================')
            print('                                                                                            ')
            print('$$$ BRAVO ', nomJoueur, 'YOU WIN $$$')
            mainMenu()
        elif 'diplôme' not in inventaire:
            textPasDiplôme = """Je suis désolé monsieur, sans diplôme on peut pas vous faire rentrer.
Vous êtes contraint de rester sur Erret et mourrez un an plus tard avec 95 pour cent 
de la population des guerres et des tsunamis qui ravagent Erret."""
            for char in textPasDiplôme: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
            sante = sante - degat
            print('Vous perdez', degat, ' points de vie')
            print('Il vous reste', sante, ' points de vie.')
            if sante == 0:
                print('                                                                                            ')
                print('Vous avez perdu...')
                print('                                                                                            ')
                mainMenu()
    
    Fusée(sante, inventaire)
    
mainMenu()

