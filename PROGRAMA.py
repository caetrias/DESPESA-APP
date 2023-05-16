import os 
import time


#FUNCAO CLEAR
def clear():
    return os.system("cls")

def login():
    print("-------[LOGIN]-------")
    login = input("Digite seu nome:")
    #ABRIR ARQUIVO E VERIFICAR SE LOGIN ESTA DENTRO -> SE LOGIN NAO ESTIVER, EXIBIR MENSAGEM, ESPERAR E VOLTAR TELA INICIO

#TELA CADASTRO
def cadastro():
    clear()
    print("-------[CADASTRO]-------")
    nome = input("\nDigite um nome para identificação: ")
    cadastros = open("cadastros.txt", "a")
    cadastros.write(nome)
    cadastros.close()

    return 
#TELA INICIAL
def tela_inicio():
    clear()
    print("-------------[BEM-VINDO(A)]-------------")
    print("[1]Logar") 
    print("[2]Cadastro")
    print("[3]Encerrar Programa")
    decisao = int(input())
    if decisao == 1:
        return login()
    if decisao == 2:
        return cadastro()
    if decisao == 3:
        return print("FIM DE PROGRAMA")

tela_inicio()