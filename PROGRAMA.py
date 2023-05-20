import os 
import time


#FUNCAO CLEAR
def clear():
    return os.system("cls")

#FUNCAO MENSAGEM DE CARREGAMENTO
def loading():
    clear()
    print("Carregando...")
    time.sleep(1.5)

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
    else:
        print("Opção não existe. Reiniciando...")
        time.sleep(1)
#TELA PRINCIPAL (PÓS TELA INICIAL DE LOGIN)
def tela_despesas():
    clear()
    print("-------------[DESPESAS]-------------")
    print("[1]ADICIONAR GASTOS") 
    print("[2]VISUALIZAR")
    print("[3]APAGAR GASTOS")
    print("[4]EDITAR")

    decisao = int(input())
    if decisao == 1:
        loading()
        return ADICIONAR_GASTOS()
    if decisao == 2:
        loading()
        return VISUALIZAR_GASTOS()
    if decisao == 3:
        loading()
        return APAGAR_GASTOS()
    if decisao == 4:
        loading()
        return "tela edicao"

#TELA ADICIONAR GASTOS
def ADICIONAR_GASTOS():
    clear()
    f = open("valores.csv", "a")
    titulo = input("Digite o título da despesa: ")
    categoria = input("Digite a categoria da despesa: ")
    valor = float(input("Digite o valor da despesa: "))

    linha = f"{titulo};{categoria};{valor}\n"  # Monta a linha com os valores separados por ponto e vírgula

    f.write(linha)
    f.close()
    tela_despesas()

#TELA VISUALIZAÇÃO DE GASTOS
def VISUALIZAR_GASTOS():
    clear()
    f = open("valores.csv", "r")
    linhas = f.readlines()  # Lê todas as linhas do arquivo

    for linha in linhas:
        titulo, categoria, valor = linha.strip().split(";")  # Divide a linha em campos usando o ponto e vírgula como separador
        valor = float(valor)  # Converte o valor para float

        print("--------------------")
        print("Título:", titulo)
        print("Categoria:", categoria)
        print("Valor:", valor)
        print("--------------------")

    f.close()
    voltar = input("[1]Voltar: ")
    if voltar == "1":
        loading()
        tela_despesas()

            #  -> PERGUNTA: CATEGORIA ESPECIFICA; PERGUNTA: GASTOS POR CATEGORIA

#TELA APAGAR OS GASTOS (INCOMPLETA)
def APAGAR_GASTOS():
    clear()
    titulo = input("Digite o título do gasto a ser removido: ")

    encontrado = False

    with open("valores.csv", "r") as f, open("valores_temp.csv", "w") as f_temp:

        linhas = f.readlines()

        for linha in linhas:
            campos = linha.strip().split(";")

            if campos[0] == titulo:
                encontrado = True
            else:
                f_temp.write(linha)

    if encontrado:
        with open("valores.csv", "w") as f_original, open("valores_temp.csv", "r") as f_temp:
        
            f_original.write(f_temp.read())

        with open("valores_temp.csv", "w"):
            pass

        print(f"Gasto com o título '{titulo}' removido com sucesso.\n")
    else:
        with open("valores_temp.csv", "w"):
            pass

        print(f"Gasto com o título '{titulo}' não encontrado.\n")

def EDITAR():
    print("")
tela_inicio()