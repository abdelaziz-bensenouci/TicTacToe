from plateau import plateau, affich_plateau, plateau_complet, verifie_gagnant
import random

#### création d'une IA ####
def IA(plateau, symbole, choix_mode):
    
    """
    Description :
        L'IA suit une logique de priorités pour jouer son coup en fonction du mode choisi.
        Difficile:
            1. Vérifie si elle peut gagner à ce tour et joue pour gagner.
            2. Bloque l'adversaire s'il est sur le point de gagner.
            3. Privilégie le centre, puis joue une case libre au hasard.
        facile:
            1. L’IA vérifie si l’adversaire peut gagner au prochain tour. Si oui, elle bloque en jouant dans la case menacée.
		    2. Si aucun blocage n’est nécessaire, elle choisit une case libre au hasard.


    Fonctions :
        - `IA(plateau, symbole)` :
            Gère le choix de la case où l'IA doit jouer en fonction des priorités définies.

    Paramètres :
        - `plateau` : Liste de 9 éléments représentant l'état du plateau (cases libres ou occupées).
        - `symbole` : Symbole de l'IA ("X" ou "O").

    Retour :
        Aucune valeur retournée. Le plateau est modifié directement.
    """

    adversaire = "X" if symbole == "O" else "O"

################################################################################################################################
                            # Mode Facile
################################################################################################################################
    
    if choix_mode == 1:
        ########### Priorité 1: Bloquer le joueur #####################
        for case in range(9):
            if plateau[case] == " ":
                plateau[case] = adversaire
                if verifie_gagnant(plateau, adversaire):
                    plateau[case] = symbole  
                    return
                plateau[case] = " "  
            
            
    ################## Priorité 2: Joue dans une case libre ####################
        cases_dispos = [case for case in range(9) if plateau[case] == " "]  
        if cases_dispos:
            choix = random.choice(cases_dispos)  
            plateau[choix] = symbole


################################################################################################################################
                            # Mode difficile
################################################################################################################################

    if choix_mode == 2: 
    ############ Priorité 1: Vérifie si l'IA peut gagner ###############
        for case in range(9):
            if plateau[case] == " ":
                plateau[case] = symbole
                if verifie_gagnant(plateau, symbole):
                    return  
                plateau[case] = " "  
        
        ############## Priorité 2: Bloquer le joueur ####################
        for case in range(9):
            if plateau[case] == " ":
                plateau[case] = adversaire
                if verifie_gagnant(plateau, adversaire):
                    plateau[case] = symbole 
                    return
                plateau[case] = " "  
        
        ############### Priorité 3: Joue dans une case libre ####################
        if plateau[4] == " ":
            plateau[4] = symbole
        else:
            cases_dispos = [case for case in range(9) if plateau[case] == " "]  
            if cases_dispos:
                choix = random.choice(cases_dispos)  
                plateau[choix] = symbole
        

    