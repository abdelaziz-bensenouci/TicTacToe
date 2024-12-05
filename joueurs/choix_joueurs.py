import random

#### Détermine qui seront les joueurs #####

def choix_joueurs():
    choix = 0
    choix_mode = 0
    liste_joueurs = []  # Initialise la liste si la fonction existe prématurement

    while choix not in [1, 2]:
        try:
            choix = int(input("Si vous désirez jouer contre l'IA tapez 1, sinon tapez 2 pour jouer contre un autre joueur: "))
            if choix not in [1, 2]:
                print("Choix invalide. Veuillez entrer 1 ou 2.")  # Gère tout ce qui n'est pas numérique
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre (1 ou 2).")  # Gère tout ce qui n'est pas numérique

    liste_symbole = ["X", "O"]
    random.shuffle(liste_symbole)

    if choix == 1:
        while True:
            try:
                choix_mode = int(input("Quel niveau de jeu desirez-vous? Tapez 1 pour facile, 2 pour difficile: "))
                if choix_mode not in [1, 2]:
                    print("Choix invalide. Veuillez entrer 1 ou 2.")  # Gère tout ce qui n'est pas numérique
                    continue
                break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre (1 ou 2).")  # Gère tout ce qui n'est pas numérique

        joueur_prenom1 = input("Entrez le nom du joueur: ")
        liste_joueurs = [joueur_prenom1, "IA"]

        for joueur_index in range(len(liste_joueurs)):
            print(f"{liste_joueurs[joueur_index].upper()} aura le symbole {liste_symbole[joueur_index]}")

    elif choix == 2:
        joueur_prenom1 = input("Entrez le nom du premier joueur: ")
        joueur_prenom2 = input("Entrez le nom du deuxième joueur: ")
        liste_joueurs = [joueur_prenom1, joueur_prenom2]

        for joueur_index in range(len(liste_joueurs)):
            print(f"{liste_joueurs[joueur_index].upper()} aura le symbole {liste_symbole[joueur_index]}")

    return liste_joueurs, choix_mode


liste_joueurs, choix_mode = choix_joueurs()