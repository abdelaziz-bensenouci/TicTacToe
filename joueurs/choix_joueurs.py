import random

#### Détermine qui seront les joueurs #####

def choix_joueurs():
    
    """
    Détermine les participants et leurs symboles pour une partie de jeu.

    Cette fonction demande à l'utilisateur de choisir le mode de jeu (contre l'IA ou un autre joueur),
    assigne les noms des joueurs, leur attribue un symbole aléatoire ("X" ou "O"), 
    et retourne la liste des joueurs ainsi que le mode de jeu choisi.

    Retourne :
        Un tuple* contenant :
            - liste_joueurs (list) : Une liste de deux éléments correspondant aux noms des joueurs.
              Si le joueur affronte l'IA, la liste sera de la forme [nom_du_joueur, "IA"].
            - choix_mode (int) : Le mode de jeu :
                - 0 si les joueurs s'affrontent entre eux.
                - 1 pour jouer contre l'IA en mode facile.
                - 2 pour jouer contre l'IA en mode difficile.
        * un tuple car quand python retourne plus d'une valeur, il les met dans un tuple.

    Exceptions gérées :
        - Gère les entrées invalides (les non-numériques ou valeurs hors des choix proposés).
        - Fournit des messages d'erreur clairs pour guider l'utilisateur en cas de mauvaise saisie.

    Exemple d'exécution :
        1. L'utilisateur choisit de jouer contre l'IA (choix = 1).
        2. Il choisit le mode de difficulté (1 ou 2).
        3. Il entre son nom.
        4. La fonction attribue un symbole aléatoire ("X" ou "O") au joueur et à l'IA.
        5. La liste des joueurs et le mode de jeu sont retournés :
           (["Nom_du_Joueur", "IA"], 1) pour le mode facile ou (["Nom_du_Joueur", "IA"], 2) pour le mode difficile.

        1. L'utilisateur choisit de jouer contre un autre joueur (choix = 2).
        2. Il entre les noms des deux joueurs.
        3. La fonction attribue aléatoirement un symbole ("X" ou "O") à chaque joueur.
        4. La liste des joueurs et le mode de jeu (0) sont retournés :
           (["Joueur1", "Joueur2"], 0).
    """
    
    
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