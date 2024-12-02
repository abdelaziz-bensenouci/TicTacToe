plateau = [[" " for i in range(3)] for i in range(3)]

def affiche_plateau(plateau):
  for i in range(3):
    print(" ", "|"," ", "|", " ")
    if i < 2:
      print("---------")

affiche_plateau(plateau)

