import os 
import time


#FUNCAO CLEAR
def clear():
    return os.system("cls")

#TELA DO LOGIN
def login():
    clear()
    print("-------[LOGIN]-------")
    print("INCOMPLETO")
    time.sleep(1)
    tela_despesas()
    #ABRIR ARQUIVO E VERIFICAR SE LOGIN ESTA DENTRO -> SE LOGIN NAO ESTIVER, EXIBIR MENSAGEM, ESPERAR E VOLTAR TELA INICIO

#TELA CADASTRO
def cadastro():
    clear()
    print("-------[CADASTRO]-------")
    nome = input("\nDigite um nome para identificação: ")
    cadastros = open("cadastros.txt", "a")
    cadastros.write(nome)
    cadastros.close()
    tela_inicio()
    
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

def tela_despesas():
    clear()
    print("-------------[DESPESAS]-------------")
    print("[1]ADICIONAR GASTOS") 
    print("[2]VISUALIZAR")
    print("[3]APAGAR GASTOS")
    print("[4]EDITAR")

    decisao = int(input())
    if decisao == 1:
        return ADICIONAR_GASTOS()
    if decisao == 2:
        return VISUALIZAR_GASTOS()
    if decisao == 3:
        return APAGAR_GASTOS()
    if decisao == 4:
        return "tela edicao"

def ADICIONAR_GASTOS():
    print("") #-> input TITULO do gasto, CATEGORIA, VALOR

def VISUALIZAR_GASTOS():
    print("") #-> read no arquivo CSV/dicionario
              #  -> PERGUNTA: CATEGORIA ESPECIFICA; PERGUNTA: GASTOS POR CATEGORIA

def APAGAR_GASTOS():
    print("") #-> ESCOLHE CATEGORIA -> exibe lista (ex.: brinquedo:10) -> PERGUNTA: limpar categoria
              #                                                        -> PERGUNTA: apagar um titulo
              #                                                        -> PERGUNTA: apagar um valor do titulo

def EDITAR():
    print("")
tela_inicio()