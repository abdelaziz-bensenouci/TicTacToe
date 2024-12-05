# Tic-Tac-Toe en Python

Ce projet est un jeu de Tic-Tac-Toe (Morpion) développé en Python. Il permet à deux joueurs de s'affronter ou à un joueur de défier une intelligence artificielle (IA).

## Fonctionnalités

*   **Mode 2 joueurs :** Deux joueurs peuvent s'affronter en saisissant tour à tour leur coup.
*   **Mode solo (contre l'IA) :** Un joueur peut jouer contre une IA qui tentera de gagner ou, au minimum, d'empêcher le joueur de gagner.
*   **Affichage clair du plateau :** Le plateau de jeu est affiché de manière intuitive à chaque tour.
*   **Détection de victoire et de match nul :** Le jeu détecte automatiquement quand un joueur gagne ou quand il y a match nul.
*   **Gestion des erreurs de saisie :** Le jeu vérifie que les entrées des joueurs sont valides.

## Comment jouer

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/abdelaziz-bensenouci/TicTacToe
    ```
2.  **Naviguer vers le répertoire du projet :**
    ```bash
    cd TicTacToe
    ```
3.  **Lancer le jeu :**
    ```bash
    python -m main
    ```
4.  **Suivre les instructions :** Le jeu vous demandera si vous voulez jouer contre l'IA ou un autre joueur, puis vous demandera de saisir vos coups à tour de rôle.

## Code

Le code est structuré en plusieurs fonctions :

*   `choix_joueurs()`: Demande aux joueurs d'entrer leurs noms et détermine qui joue avec quel symbole (X ou O). Gère aussi le choix du mode de jeu (contre l'IA ou un autre joueur).
*   `affich_plateau(plateau, initial)`: Affiche le plateau de jeu. Si `initial` est vrai, affiche le plateau avec les numéros des cases pour aider les joueurs à choisir leur coup.
*   `verifie_gagnant(plateau, symbole)`: Vérifie si le joueur avec le `symbole` donné a gagné.
*   `plateau_complet(plateau)`: Vérifie si le plateau est plein (match nul).
*   `IA(plateau, symbole)`: Détermine le coup de l'IA. L'IA essaie d'abord de gagner, puis d'empêcher le joueur de gagner, et enfin joue un coup aléatoire si aucune des deux premières options n'est possible.
*   `jouer()`: Fonction principale qui gère le déroulement du jeu.

## Intelligence Artificielle (IA)

L'IA utilise une stratégie à trois niveaux :

1.  **Priorité 1 : Gagner.** Vérifie si elle peut gagner à ce tour et joue pour gagner.
2.  **Priorité 2 : Bloquer.** Si le joueur peut gagner au prochain coup, l'IA le bloque.
3.  **Priorité 3 : Jouer un coup aléatoire.** Si aucune des deux premières conditions n'est remplie, l'IA joue un coup aléatoire parmi les cases disponibles. L'IA va jouer en priorité au centre du plateau si disponible.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests pour améliorer le jeu.

## Auteurs

*   [Abdelaziz BENSENOUCI](https://github.com/abdelaziz-bensenouci)
*   [Aicha CHADLI](https://github.com/aicha-chadli)
*   [Ryhad BOUGHANMI](https://github.com/ryhad-boughanmi)