import desenhos as d

palavra = "maravilha"

digitadas = []
acertos = []
erros = 0

while True:
  adivinha = d.imprimir_palavra_secreta(palavra, acertos)

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

  d.desenho_forca(erros)

  # * CONDIÇÃO DE DERROTA
  if erros == 6:
    print("ENFORCADO!")
    print(f"A PALAVRA ERA: {palavra}")
    break