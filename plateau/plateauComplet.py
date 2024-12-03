def plateauComplet(plateau):
  for ligne in plateau:
    if " " in ligne:
      return False
  return True     