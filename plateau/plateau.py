plateau = [[" " for i in range(3)] for i in range(3)]

def affich_plateau(plateau):
  for i in range(3):
    print(" ", "|"," ", "|", " ")
    if i < 2:
      print("---------")

affich_plateau(plateau)

