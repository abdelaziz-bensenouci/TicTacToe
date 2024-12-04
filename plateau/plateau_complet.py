"""
Description :
    Ce fichier contient une fonction permettant de vérifier si le plateau de jeu est complètement rempli. 
    Cela est utilisé pour déterminer un match nul.

Fonctions :
    - `plateauComplet(plateau)` :
        Vérifie si toutes les cases du plateau sont occupées.

Paramètres :
    - `plateau` : Liste de 9 éléments représentant l'état actuel du plateau de jeu.

Retour :
    - `True` : Si toutes les cases sont remplies.
    - `False` : S'il reste au moins une case libre.
"""

def plateau_complet(plateau):
  for ligne in plateau:
    if " " in ligne:
      return False
  return True     