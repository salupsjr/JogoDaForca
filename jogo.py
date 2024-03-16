import desenhos as d
from random import choice

def jogar():
  lista_de_palavras = list()
  arquivo = open("palavras.txt", "r")
  for linha in arquivo:
    palavra = linha.strip()
    lista_de_palavras.append(palavra)
  
  palavra_sorteada = choice(lista_de_palavras).lower()
  
  digitadas = []
  acertos = []
  erros = 0
  
  while True:
    adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
  
    # * CONDIÇÃO DE VITÓRIA
    if adivinha == palavra_sorteada:
      print("VOCÊ ACERTOU!!!")
      break
    
    # * TENTATIVAS
    tentativa = input("DIGITE UMA LETRA: ").lower().strip()
    if tentativa in digitadas:
      print("VOCÊ JÁ DIGITOU ESSA LETRA!")
      continue
    else:
      digitadas += tentativa
      if tentativa in palavra_sorteada:
        acertos += tentativa
      else:
        erros += 1
        print("VOCÊ ERROU!")
  
    d.desenho_forca(erros)
  
    # * CONDIÇÃO DE DERROTA
    if erros == 6:
      print("ENFORCADO!")
      print(f"A PALAVRA ERA: {palavra_sorteada}")
      break