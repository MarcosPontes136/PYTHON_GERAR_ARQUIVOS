from GERAR_ARQUIVOS.FUNCOES_DE_GERAR_ARQUIVO import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
  if opcao == "I":
    inserir(usuarios)
  if opcao == "P":
    pesquisar(usuarios, input("Qual nome deseja pesquisar: "))
  if opcao == "E":
    excluir(usuarios)
  if opcao == "L":
    listar(usuarios)
  opcao = perguntar()


