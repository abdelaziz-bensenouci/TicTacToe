from plateau import plateau, affich_plateau, plateau_complet, verifie_gagnant
from joueurs.choix_joueurs import choix_joueurs, liste_joueurs
from IA.IA import IA


################################## Dynamique du jeux ###########################################
def jouer(choix_mode):
    
    """
    Description :
        Il s'agit de la dynamique du jeu Morpion(Tic Tac Toe).
        Le jeu permet à deux joueurs (joueur VS joueur ou joueur VS IA) de s'affronter.
        Le plateau est mis à jour après chaque tours et les résultats 
        (victoire, défaite ou match nul) sont déterminés.

    Fonction principale du jeu.
        Cette fonction gère la boucle principale :
            - Affiche le plateau de jeu.
            - Alterne entre les tours des joueurs (joueur ou IA).
            - Vérifie après chaque tour si un joueur a gagné ou si le plateau est complet (match nul).
            - Affiche le résultat (victoire ou match nul) et termine la partie.

        Variables utilisées :
            - `plateau` : Liste représentant l'état actuel du plateau (cases libres ou occupées).
            - `joueurs` : Liste des noms des joueurs (ou "IA").
            - `symbole` : "X" ou "O" attribué au joueur en cours.
            - `case` : Case choisie par le joueur (1 à 9).

        Erreurs :
            - Vérifie que la case saisie est valide (entre 1 et 9).
            - Empêche de jouer dans une case déjà occupée.

        Termine la partie
    """
    
    affich_plateau(plateau, initial=True)
    
    
    while True:
        for nom_joueur in range(2):
            if liste_joueurs[nom_joueur] == "IA":
                print("C'est au tour de l'IA")
                symbole = "O" if nom_joueur == 1 else "X"
                IA(plateau, symbole, choix_mode) 
            else:
                joueur = liste_joueurs[nom_joueur]
                print(f"C'est au tour de {joueur.upper()}")
                case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                
                while case < 1 or case > 9 or plateau[case - 1] != " ":
                    if plateau[case - 1] != " ":
                        print("Cette case est déjà occupée.")
                    else:
                        print("Saisir un nombre entre 1 et 9 correspondant à une case libre !")
                    case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                    
                symbole = "X" if nom_joueur == 0 else "O"
                plateau[case - 1] = symbole
                
            affich_plateau(plateau)
            
            if verifie_gagnant(plateau, symbole):
                if liste_joueurs[nom_joueur] == "IA":
                    print("Désolé, l'IA a gagné !")
                else:
                    print(f"Félicitations ! {liste_joueurs[nom_joueur].upper()} a gagné !")
                return
            
            if plateau_complet(plateau):
                print("Match nul!")
                return