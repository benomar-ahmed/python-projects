#Créer un script pendu.py
#Dans un premier temps le programme demandera au joueur le niveau avec lequel il souhaiterai jouer.
#Il aura un nombre de vies en fonction du niveau choisi (exemple débutant 10, intermédiaire 7, expert 4).
#Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible et afficher :
#       - Le nombre de vies restantes au joueur
#       - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
#       En expert, la liste n’apparaîtra pas)
#       - Des “_” pour remplacer les lettres non trouvées
#       - Les lettres proposées qui se trouvent dans le mot
#
#La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.




import random


def ligne(args):
    Underscore = "_ "
    i=""
    compt=0
    while compt < len(args):
        i+=Underscore
        compt+=1
    print("Mot à deviner : ",i,end="\n")


NiveauDeJeu = input("Avec quel niveau veux-tu jouer ? Débutant, Intermédiaire ou bien Expert ? : ")
tentative_Débutant = 10
tentative_Intermédiaire = 7
tentative_Expert = 4
dico = open("dico_france.txt", "r", encoding="ISO-8859-1")
Text = dico.read().split()
liste=list(Text)
words = random.choice(liste)
Underscore = "_ "
affichage=""
Lettres_Proposées=""
ligne(words)
if NiveauDeJeu == "Expert":
    while tentative_Expert < 5:
        print(affichage)
        proposition = input("Quelle lettre propose tu ? ")
        if proposition in words:
            Lettres_Proposées += proposition
            
        else:
            tentative_Expert-=1
            if tentative_Expert == 3:
                print("Nombre(s) de vie(s) restant : ",3)
                Lettres_Proposées += proposition
                
            elif tentative_Expert == 2:
                print("Nombre(s) de vie(s) restant : ",2)
                Lettres_Proposées += proposition
               
            elif tentative_Expert == 1:
                print("Nombre(s) de vie(s) restant : ",1)
                Lettres_Proposées += proposition
                
            elif tentative_Expert == 0:
                print("Nombre(s) de vie(s) restant : ",0)
                Lettres_Proposées += proposition
                
                print("Tu as perdu !")
                print("Le mot était : ",words)
                exit()


        affichage = ""
        for x in words:
            if x in Lettres_Proposées:
                affichage += x + " "
            else:
                affichage += "_ "
        for z in words:
            if "_" not in affichage:
                print(">>> Gagné! <<<")
                print(">>> Le mot était : ",affichage,"<<<")
                quit()
    

if NiveauDeJeu == "Intermédiaire":
    while tentative_Intermédiaire < 8:
        print(affichage)
        proposition = input("Quelle lettre propose tu ? ")

        if proposition in words:
            Lettres_Proposées += proposition
            print("Lettres proposées : ",Lettres_Proposées,end="  \n")
        else:
            tentative_Intermédiaire-=1
            if tentative_Intermédiaire == 6:
                print("Nombre(s) de vie(s) restant : ",6)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 5:
                print("Nombre(s) de vie(s) restant : ",5)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 4:
                print("Nombre(s) de vie(s) restant : ",4)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 3:
                print("Nombre(s) de vie(s) restant : ",3)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 2:
                print("Nombre(s) de vie(s) restant : ",2)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 1:
                print("Nombre(s) de vie(s) restant : ",1)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 0:
                print("Nombre(s) de vie(s) restant : ",0)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
                print("Tu as perdu !")
                print("Le mot était : ",words)
                exit()

        affichage = ""
        for x in words:
            if x in Lettres_Proposées:
                affichage += x + " "
            else:
                affichage += "_ "
        for z in words:
            if "_" not in affichage:
                print(">>> Gagné! <<<")
                print(">>> Le mot était : ",affichage,"<<<")
                quit()
if NiveauDeJeu == "Débutant":
    while tentative_Débutant < 11:
        print(affichage)
        proposition = input("Quelle lettre propose tu ? ")

        if proposition in words:
            Lettres_Proposées += proposition
            print("Lettres proposées : ",Lettres_Proposées,end="  \n")
        else:
            tentative_Débutant-=1
            if tentative_Débutant == 9:
                print("Nombre(s) de vie(s) restant : ",9)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 8:
                print("Nombre(s) de vie(s) restant : ",8)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 7:
                print("Nombre(s) de vie(s) restant : ",7)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 6:
                print("Nombre(s) de vie(s) restant : ",6)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 5:
                print("Nombre(s) de vie(s) restant : ",5)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Intermédiaire == 4:
                print("Nombre(s) de vie(s) restant : ",4)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 3:
                print("Nombre(s) de vie(s) restant : ",3)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 2:
                print("Nombre(s) de vie(s) restant : ",2)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 1:
                print("Nombre(s) de vie(s) restant : ",1)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
            elif tentative_Débutant == 0:
                print("Nombre(s) de vie(s) restant : ",0)
                Lettres_Proposées += proposition
                print("Lettres proposées : ",Lettres_Proposées,end="  \n")
                print("Tu as perdu !")
                print("Le mot était : ",words)
                exit()
        affichage = ""
        for x in words:
            if x in Lettres_Proposées:
                affichage += x + " "
            else:
                affichage += "_ "
        for z in words:
            if "_" not in affichage:
                print(">>> Gagné! <<<")
                print(">>> Le mot était : ",affichage,"<<<")
                quit()

