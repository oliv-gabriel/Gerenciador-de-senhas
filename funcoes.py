import json
import string
import random

def escolha(n):
    while True:
        if n == 1:
            plataforma = input("Qual plataforma você deseja criar uma nova senha: ")
            conta = input("Em que conta você irá utilizar: ")
            salvar(plataforma, conta, random_generator())
        elif n == 2:
            palavra = input("Senha de qual conta ou plataforma você deseja procurar? ")
            buscar_dados(lista_dicionarios, palavra)
        else:
            while n != 1 or 2:
               print("O que você deseja fazer?\nCriar nova conta, digite 1\nBuscar por senha, digite 2")
               nu = int(input("Digite o numero refente a escolha:"))
               escolha(nu)
                
      
def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

def salvar(plataforma, conta, senha):
   f = open('senhas.txt','at')
   f.write(f"Plataforma: {plataforma}\nConta: {conta}\nSenha: {senha}\n{'-'*50}\n")
   f.close()

arquivo_txt = 'senhas.txt'
def ler_arquivo_txt(nome_arquivo):
    lista_dicionarios = []
    dicionario = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços em branco e quebras de linha
            if linha and not linha.startswith('-'):
                if linha.startswith("Plataforma:"):
                    chave = "Plataforma"
                    valor = linha[len("Plataforma:"):]
                    dicionario[chave.strip()] = valor.strip()
                elif linha.startswith("Conta:"):
                    chave = "Conta"
                    valor = linha[len("Conta:"):]
                    dicionario[chave.strip()] = valor.strip()
                elif linha.startswith("Senha:"):
                    chave = "Senha"
                    valor = linha[len("Senha:"):]
                    dicionario[chave.strip()] = valor.strip()
                else:
                    print(f"A linha '{linha}' não contém o formato esperado. Ignorando a linha.")
            elif linha.startswith('-') and dicionario:
                lista_dicionarios.append(dicionario)
                dicionario = {}
    if dicionario:
        lista_dicionarios.append(dicionario)
    return lista_dicionarios
lista_dicionarios = ler_arquivo_txt(arquivo_txt)


def buscar_dados(dicionario, termo):
    resultados = []
    for dados in dicionario:
        for valor in dados.values():
            if termo.lower() in valor.lower():
                resultados.append(dados)
                break  # Interrompe o loop interno ao encontrar uma correspondência

    if resultados:
        print(f"Resultado(s) da busca para o termo '{termo}':")
        for resultado in resultados:
            print(resultado)
    else:
        print(f"Nenhum resultado encontrado para o termo '{termo}'.")

