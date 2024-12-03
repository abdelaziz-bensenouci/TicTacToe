plateau = [" " for _ in range(9)]

#### Affichage du plateau #####
def affich_plateau(plateau, initial=False):
    if initial:
        print("Plateau initial : (utilisez les numéros pour jouer)")
        print("1 | 2 | 3")
        print("---------")
        print("4 | 5 | 6")
        print("---------")
        print("7 | 8 | 9")
    else:
        for ligne in range(3):
            start = ligne * 3
            print(plateau[start], "|", plateau[start + 1], "|", plateau[start + 2])
            if ligne < 2:
                print("---------")
                	#	Chaque ligne contient 3 cases, donc les indices des cases sont :
                    #	Ligne 0 : indices 0, 1, 2
                    #	Ligne 1 : indices 3, 4, 5
                    #
                    #	Ligne 2 : indices 6, 7, 8
                    #	La formule ligne * 3 calcule l’indice de départ de chaque ligne :
                    #	Si ligne = 0 → start = 0
                    #	Si ligne = 1 → start = 3
                    #	Si ligne = 2 → start = 6

