import jogo



def mostrar_menu():
  print("="*30)
  print(" " * 8 + "JOGO DA FORCA")
  print("="*30)
  print("\n1- JOGAR")
  print("2- SCORE")
  print("3- SAIR\n")
  print("="*30)

while True:
  mostrar_menu()
  opcao = int(input("DIGITE UMA OPÇÃO: (1/2/3)"))

  if opcao == 1:
    print("BORA JOGAR!")    
    jogo.jogar()
    input(f"Pressione ENTER para continuar...")
  elif opcao == 2:
    print("SCORE")
  elif opcao == 3:
    print("SAINDO... ATÉ MAIS!")
    break
  else:
    print("OPÇÃO INVÁLIDA!")