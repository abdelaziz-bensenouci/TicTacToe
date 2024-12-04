import random

#### création d'une IA ####
def IA(plateau, symbole, choix_mode):
    
    """
    Description :
        L'IA suit une logique de priorités pour jouer son coup :
        1. Vérifie si elle peut gagner à ce tour et joue pour gagner.
        2. Bloque l'adversaire s'il est sur le point de gagner.
        3. Si aucune des situations ci-dessus ne s'applique, joue dans une case libre (en commençant par le centre si disponible).

    Fonctions :
        - `IA(plateau, symbole)` :
            Gère le choix de la case où l'IA doit jouer en fonction des priorités définies.

    Paramètres :
        - `plateau` : Liste de 9 éléments représentant l'état du plateau (cases libres ou occupées).
        - `symbole` : Symbole de l'IA ("X" ou "O").

    Retour :
        Aucune valeur retournée. Le plateau est modifié directement.
    """

################################################################################################################################
                            # Mode Facile
################################################################################################################################
    
    if choix_mode == 1:
        ########### Priorité 2: Bloquer le joueur #####################
        for i in range(3):
            # Vérif les lignes
            if plateau[i * 3] == plateau[i * 3 + 1] == "X" and plateau[i * 3 + 2] == " ":
                plateau[i * 3 + 2] = symbole
                return
            if plateau[i * 3] == plateau[i * 3 + 2] == "X" and plateau[i * 3 + 1] == " ":
                plateau[i * 3 + 1] = symbole
                return
            if plateau[i * 3 + 1] == plateau[i * 3 + 2] == "X" and plateau[i * 3] == " ":
                plateau[i * 3] = symbole
                return
            
            # Vérif les colonnes
            if plateau[i] == plateau[i + 3] == "X" and plateau[i + 6] == " ":
                plateau[i + 6] = symbole
                return
            if plateau[i + 3] == plateau[i + 6] == "X" and plateau[i] == " ":
                plateau[i] = symbole
                return
            if plateau[i] == plateau[i + 6] == "X" and plateau[i + 3] == " ":
                plateau[i + 3] = symbole
                return

        #Vérif les diagonales 
        if plateau[0] == plateau[4] == "X" and plateau[8] == " ":
            plateau[8] = symbole
            return
        if plateau[4] == plateau[8] == "X" and plateau[0] == " ":
            plateau[0] = symbole
            return
        if plateau[2] == plateau[4] == "X" and plateau[6] == " ":
            plateau[6] = symbole
            return
        if plateau[4] == plateau[6] == "X" and plateau[2] == " ":
            plateau[2] = symbole
            return
        if plateau[2] == plateau[6] == "X" and plateau[4] == " ":
            plateau[4] = symbole
            return
    ################## Priorité 3: Joue dans une case libre ####################
        cases_dispos = [i for i in range(9) if plateau[i] == " "]  
        if cases_dispos:
            choix = random.choice(cases_dispos)  
            plateau[choix] = symbole


################################################################################################################################
                            # Mode difficile
################################################################################################################################

    if choix_mode == 2: 
    ############ Priorité 1: Vérifie si l'IA peut gagner ###############
        for i in range(3):
            # Vérif des lignes
            if plateau[i * 3] == plateau[i * 3 + 1] == symbole and plateau[i * 3 + 2] == " ":
                plateau[i * 3 + 2] = symbole
                return
            if plateau[i * 3 + 1] == plateau[i * 3 + 2] == symbole and plateau[i * 3] == " ":
                plateau[i * 3] = symbole
                return
            if plateau[i * 3] == plateau[i * 3 + 2] == symbole and plateau[i * 3 + 1] == " ":
                plateau[i * 3 + 1] = symbole
                return

        # Vérif des colonnes
        for i in range(3):
            if plateau[i] == plateau[i + 3] == symbole and plateau[i + 6] == " ":
                plateau[i + 6] = symbole
                return
            if plateau[i + 3] == plateau[i + 6] == symbole and plateau[i] == " ":
                plateau[i] = symbole
                return
            if plateau[i] == plateau[i + 6] == symbole and plateau[i + 3] == " ":
                plateau[i + 3] = symbole
                return

        # Vérif des diagonales
        if plateau[0] == plateau[4] == symbole and plateau[8] == " ":
            plateau[8] = symbole
            return
        if plateau[4] == plateau[8] == symbole and plateau[0] == " ":
            plateau[0] = symbole
            return
        if plateau[2] == plateau[4] == symbole and plateau[6] == " ":
            plateau[6] = symbole
            return
        if plateau[4] == plateau[6] == symbole and plateau[2] == " ":
            plateau[2] = symbole
            return
        if plateau[2] == plateau[6] == symbole and plateau[4] == " ":
            plateau[4] = symbole
            return
        
        ############## Priorité 2: Bloquer le joueur ####################
        for i in range(3):
            # Vérif les lignes
            if plateau[i * 3] == plateau[i * 3 + 1] == "X" and plateau[i * 3 + 2] == " ":
                plateau[i * 3 + 2] = symbole
                return
            if plateau[i * 3] == plateau[i * 3 + 2] == "X" and plateau[i * 3 + 1] == " ":
                plateau[i * 3 + 1] = symbole
                return
            if plateau[i * 3 + 1] == plateau[i * 3 + 2] == "X" and plateau[i * 3] == " ":
                plateau[i * 3] = symbole
                return
            
            # Vérif les colonnes
            if plateau[i] == plateau[i + 3] == "X" and plateau[i + 6] == " ":
                plateau[i + 6] = symbole
                return
            if plateau[i + 3] == plateau[i + 6] == "X" and plateau[i] == " ":
                plateau[i] = symbole
                return
            if plateau[i] == plateau[i + 6] == "X" and plateau[i + 3] == " ":
                plateau[i + 3] = symbole
                return

        #Vérif les diagonales 
        if plateau[0] == plateau[4] == "X" and plateau[8] == " ":
            plateau[8] = symbole
            return
        if plateau[4] == plateau[8] == "X" and plateau[0] == " ":
            plateau[0] = symbole
            return
        if plateau[2] == plateau[4] == "X" and plateau[6] == " ":
            plateau[6] = symbole
            return
        if plateau[4] == plateau[6] == "X" and plateau[2] == " ":
            plateau[2] = symbole
            return
        if plateau[2] == plateau[6] == "X" and plateau[4] == " ":
            plateau[4] = symbole
            return
        
        ############### Priorité 3: Joue dans une case libre ####################
        if plateau[4] == " ":
            plateau[4] = symbole
        else:
            cases_dispos = [i for i in range(9) if plateau[i] == " "]  
            if cases_dispos:
                choix = random.choice(cases_dispos)  
                plateau[choix] = symbole
        

    