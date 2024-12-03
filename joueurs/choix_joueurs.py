
# test_variable = "je suis un test"

#### Détermine qui seront les joueurs #####

def choixJoueurs():
    choix = 0

    while choix not in [1,2]:
        choix = int(input("Si vous désirez jouer contre l'IA, tapez 1, sinon tapez 2 pour jouer contre un autre joueur: "))
        if choix == 1:
            joueur_prenom1 = input("Entrez le nom du joueur: ")
            print(joueur_prenom1.upper(), "aura le symbole X")
            liste_joueurs = [joueur_prenom1, "IA"]
        elif choix == 2:
            joueur_prenom1 = input("Entrez le nom du premier joueur: ")
            joueur_prenom2 = input("Entrez le nom du deuxième joueur: ")
            liste_joueurs = [joueur_prenom1, joueur_prenom2]
            
            listSymbole = ["X", "O"]
            for joueur_index in range(len(liste_joueurs)):
                print(f"{liste_joueurs[joueur_index].upper()} aura le symbole {listSymbole[joueur_index]}")
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
    return liste_joueurs

liste_joueurs = choixJoueurs()