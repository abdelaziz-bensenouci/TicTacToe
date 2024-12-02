from plateau import plateau, affich_plateau, plateauComplet, verifieGagnant
from joueurs.choix_joueurs import choixJoueurs, joueurs
from IA.IA import IA

################################## Dynamique du jeux ###########################################
def jouer():
    affich_plateau(plateau, initial=True)
    while True:
        for i in range(2):
            if joueurs[i] == "IA":
                print("C'est au tour de l'IA")
                symbole = "O" if i == 1 else "X"
                IA(plateau, symbole) 
            else:
                joueur = joueurs[i]
                print("C'est au tour de ", joueur.upper())
                case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                while case < 1 or case > 9 or plateau[case - 1] != " ":
                    if plateau[case - 1] != " ":
                        print("Cette case est déjà occupée.")
                    else:
                        print("Saisir un nombre entre 1 et 9 correspondant à une case libre !")
                    case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                symbole = "X" if i == 0 else "O"
                plateau[case - 1] = symbole
            affich_plateau(plateau)
            if verifieGagnant(plateau, symbole):
                if joueurs[i] == "IA":
                    print("Désolé, l'IA a gagné !")
                else:
                    print("Félicitations !", joueurs[i].upper(), "a gagné !")
                return
            if plateauComplet(plateau):
                print("Match nul!")
                return
            
print("test")