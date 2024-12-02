##### IA ############
def IA(plateau, symbole):
    for i in range(3):
################################### Priorité 1: Vérifie si l'IA peut gagner #########################
            if plateau[i][0] == plateau[i][1] == symbole and plateau[i][2] == " ":
                plateau[i][2] = symbole
                return
            if plateau[i][1] == plateau[i][2] == symbole and plateau[i][0] == " ":
                plateau[i][0] = symbole
                return
            if plateau[i][0] == plateau[i][2] == symbole and plateau[i][1] == " ":
                plateau[i][1] = symbole
                return
            if plateau[0][i] == plateau[1][i] == symbole and plateau[2][i] == " ":
                plateau[2][i] = symbole
                return
            if plateau[1][i] == plateau[2][i] == symbole and plateau[0][i] == " ":
                plateau[0][i] = symbole
                return
            if plateau[0][i] == plateau[2][i] == symbole and plateau[1][i] == " ":
                plateau[1][i] = symbole
                return
        
            #Vérifie les diagonales
            if plateau[0][0] == plateau[1][1] == symbole and plateau[2][2] == " ":
                plateau[2][2] = symbole
                return
            if plateau[1][1] == plateau[2][2] == symbole and plateau[0][0] == " ":
                plateau[0][0] = symbole
                return
            if plateau[0][2] == plateau[1][1] == symbole and plateau[2][0] == " ":
                plateau[2][0] = symbole
                return
            if plateau[1][1] == plateau[2][0] == symbole and plateau[0][2] == " ":
                plateau[0][2] = symbole
                return
            if plateau[0][0] == plateau[2][2] == symbole and plateau[1][1] == " ":
                plateau[1][1] = symbole
                return

########################### Priorité 2: Bloquer le joueur ###################################
    for i in range(3):
        # Vérifie les lignes
        if plateau[i][0] == plateau[i][1] == "X" and plateau[i][2] == " ":
            plateau[i][2] = symbole
            return
        if plateau[i][1] == plateau[i][2] == "X" and plateau[i][0] == " ":
            plateau[i][0] = symbole
            return
        if plateau[i][0] == plateau[i][2] == "X" and plateau[i][1] == " ":
            plateau[i][1] = symbole
            return
        
        # Vérifie les colonnes
        if plateau[0][i] == plateau[1][i] == "X" and plateau[2][i] == " ":
            plateau[2][i] = symbole
            return
        if plateau[1][i] == plateau[2][i] == "X" and plateau[0][i] == " ":
            plateau[0][i] = symbole
            return
        if plateau[0][i] == plateau[2][i] == "X" and plateau[1][i] == " ":
            plateau[1][i] = symbole
            return

    #Vérifie les diagonales 
    if plateau[0][0] == plateau[1][1] == "X" and plateau[2][2] == " ":
        plateau[2][2] = symbole
        return
    if plateau[1][1] == plateau[2][2] == "X" and plateau[0][0] == " ":
        plateau[0][0] = symbole
        return
    if plateau[0][2] == plateau[1][1] == "X" and plateau[2][0] == " ":
        plateau[2][0] = symbole
        return
    if plateau[1][1] == plateau[2][0] == "X" and plateau[0][2] == " ":
        plateau[0][2] = symbole
        return
    if plateau[0][0] == plateau[2][2] == "X" and plateau[1][1] == " ":
        plateau[1][1] = symbole
        return

########################## Priorité 3: Joue dans une case libre #############################
    if plateau[1][1] == " ":
                plateau[1][1] = symbole
                return
    
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = symbole
                return