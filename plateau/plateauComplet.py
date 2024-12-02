def plateauComplet(plateau):
  for row in plateau:
    if " " in row:
      return False
  return True     
  