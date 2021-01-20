def perguntar ():
    return input("O deseja realizar?\n " +
                 "<I> - Inserir um novo usuario:\n " +
                 "<P> - Para pesquisar um usuario:\n " +
                 "<E> - Excluir um usuario:\n " +
                 "<L> - Listar os usuarios:\n\n").upper()


def inserir (dicionario):
    dicionario[input("\nDigite seu Login: ").upper()] = [input("Digite o nome: "),
                                                        input("Digite sua data de nascimento: ").upper(),
                                                        input("Digite sua data de acesso: ").upper(),
                                                        input("Digite a sua ultima estação acessada: ").upper()]
    salvar(dicionario)

def salvar (dicionario):
    with open("banco_de_dados.txt", "a") as arquivo: #função "with" abre o arquivo com o nome desejado
        for chave, valor in dicionario.items():
            arquivo.write(chave + "." + str(valor) + '\n') #Função "write" escreve dentro do arquivo criado



def pesquisar (dicionacio, chave):
    with open("banco_de_dados.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            if arquivo!=None:
                print("Nome:" + linha[::])


def excluir(dicionario, chave):
    if dicionario.get(chave):
        del dicionario[chave]
        print("--------OBEJETO ELIMINADO!--------")


def listar(dicionario):
    with open("banco_de_dados.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)