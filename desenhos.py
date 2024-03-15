def imprimir_palavra_secreta(palavra, acertos):
  adivinha = ""
  for letra in palavra:
    if letra in acertos:
      adivinha += letra
    else:
      adivinha += "\u003F"
  print(f"QUAL A PALAVRA:  ({len(palavra)} letras)")
  for letra in adivinha:
    print(f"{letra} ", end="")
  print()

  return adivinha

def desenho_forca(erros):
  print("X==:==")
  print("X  :   ")
  if erros >= 1:
    print("X  O  ")
  else:
    print("X")

  linha2 = ""
  if erros >= 2:
    linha2 += "  |   "
  elif erros == 3:
    linha2 = " \|   "
  elif erros >= 4:
    linha2 = " \|/ "
  print(f"X{linha2}")

  linha3 = ""
  if erros == 5:
    linha3 += " /    "
  elif erros >= 6:
    linha3 += " / \ "
  print(f"X{linha3}")
  print("X\n===========")
  
  