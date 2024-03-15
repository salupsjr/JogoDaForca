palavra = "maravilha"

digitadas = []
acertos = []
erros = 0

while True:
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

  # * CONDIÇÃO DE VITÓRIA
  if adivinha == palavra:
    print("VOCÊ ACERTOU!!!")
    break
  
  # * TENTATIVAS
  tentativa = input("DIGITE UMA LETRA: ").lower().strip()
  if tentativa in digitadas:
    print("VOCÊ JÁ DIGITOU ESSA LETRA!")
    continue
  else:
    digitadas += tentativa
    if tentativa in palavra:
      acertos += tentativa
    else:
      erros += 1
      print("VOCÊ ERROU!")

  # * DESENHO DA FORCA
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

  # * CONDIÇÃO DE DERROTA
  if erros == 6:
    print("ENFORCADO!")
    print(f"A PALAVRA ERA: {palavra}")
    break