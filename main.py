from bd import conectar
import jogo, bd

def mostrar_menu():
  print("="*30)
  print(" " * 8 + "JOGO DA FORCA")
  print("="*30)
  print("\n1- JOGAR")
  print("2- SCORE")
  print("3- SAIR\n")
  print("="*30)

while True:
  conn = bd.conectar()
  bd.criar_tabela(conn)
  
  mostrar_menu()
  opcao = int(input("DIGITE UMA OPÇÃO (1/2/3): "))

  if opcao == 1:
    print("BORA JOGAR!")    
    jogo.jogar()
    input(f"Pressione ENTER para continuar...")
  elif opcao == 2:
    print("SCORE")
    dados = bd.listar_dados()
    if not dados:
      print("NÃO HÁ DADOS")
    else: 
      i = 1
      for dado in dados:
        print(f"{i} - {dado[1]} - Pontuação: {dado[2]}")
        i += 1
    input(f"Pressione ENTER para continuar...")
  elif opcao == 3:
    print("SAINDO... ATÉ MAIS!")
    break
  else:
    print("OPÇÃO INVÁLIDA!")

bd.desconectar(conn)