def Jeu():
    sante = int()
    sante = 100

    print('Début du jeu')
    
    def Examen():

        reponse = str()

        print('20 ans plus tard...')
        print('Vous rendez vous à l\'examen ?')
        while 1:
            print('Allez vous à l\'examen : oui ou non ?')
            reponse = input()
            if reponse == 'oui':
                print('Passage de l\'examen, répondez à la question suivante : combien font 2*2 ?')
                print('Saisir la bonne réponse')
                reponse = input()
                if reponse == '4':
                    print('C\'est une bonne réponse, vous recevez votre diplôme !')
                    return
                else:
                    print('Mauvaise réponse, vous repassez l\'examen l\'année prochaine !')
            elif reponse == 'non':
                print('Vous rencontreze quelqu\'un du gouvernement qui vous pistonne.')
            else:
                print('Erreur répondez oui ou non')
            if reponse == 'oui' or reponse == 'non':
                break
    Examen()

    print('2ème étape du jeu')
    
    def Proposition(sante):
    
        degat = int()
        reponse = str()
    
        degat = 100
    
        print('Après être enfin arriver au gouvernement vous voilà face à un terrible choix...')

        print('Un pays ennemi vous propose une alliance... acceptez ou refusez !')
        while 1:
            print('Vous acceptez : oui ou non ?')
            reponse = input()
            if reponse == 'oui':
                print('Trahison, guerre, votre pays vous exécute pour avoir livré des informations au pays ennemi !')
                sante = (sante - degat)
                print(sante)
                if sante == 0:
                    print('Vous avez perdu!')
                    quit()
            elif reponse == 'non':
                print('Vous restez fidèle à votre pays et vous continuez votre carrière')
                print(' Vous pouvez continuer !')
            else:
                print('Erreur répondez oui ou non')
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
            if reponse == 'mesure' or reponse == 'fuir':
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
    
    Findejeu(sante)
Jeu()