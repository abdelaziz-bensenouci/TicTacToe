#### Vérifie si il y a un gagnant #####
def verifie_gagnant(plateau, symbole):
    
    """
    Description :
        Ce fichier contient une fonction pour vérifier si un joueur a gagné.
        La vérification porte sur :
        - Les lignes
        - Les colonnes
        - Les diagonales

    Fonctions :
        - `verifie_gagnant(plateau, symbole)` :
            Vérifie si le symbole donné a formé une ligne, une colonne, ou une diagonale complète sur le plateau.

    Paramètres :
        - `plateau` : Liste de 9 éléments représentant l'état du plateau de jeu.
        - `symbole` : Symbole du joueur ("X" ou "O") à vérifier.

    Retour :
        - `True` : Si le joueur a gagné.
        - `False` : Sinon.
    """

    for index_case in range(3):
        if plateau[index_case * 3] == plateau[index_case * 3 + 1] == plateau[index_case * 3 + 2] == symbole:
            return True
    for index_case in range(3):
        if plateau[index_case] == plateau[index_case + 3] == plateau[index_case + 6] == symbole:
            return True
    if plateau[0] == plateau[4] == plateau[8] == symbole:
        return True
    if plateau[2] == plateau[4] == plateau[6] == symbole:
        return True
    return False