#### Vérifie si il y a un gagnant #####
def verifieGagnant(plateau, symbole):
    for i in range(3):
        if plateau[i * 3] == plateau[i * 3 + 1] == plateau[i * 3 + 2] == symbole:
            return True
    for i in range(3):
        if plateau[i] == plateau[i + 3] == plateau[i + 6] == symbole:
            return True
    if plateau[0] == plateau[4] == plateau[8] == symbole:
        return True
    if plateau[2] == plateau[4] == plateau[6] == symbole:
        return True
    return False