import os 
import time

global nome

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
    try:
        global nome

        clear()
        nome = input('Digite o seu login: ')
        senha = input('Digite a sua senha: ')
        
        file = open('login.csv', 'a', encoding='utf8')
        file.close()
        file = open('login.csv', 'r', encoding='utf8')
        linhas = file.readlines()

        for linha in linhas:
            dados = linha.strip().split(';')
            if nome == dados[0] and senha == dados[1]:
                print('Login bem sucedido')
                file.close()
                loading()
                return tela_despesas()

        print('Login ou senha incorretos')
        file.close()
        time.sleep(1.5)
        return tela_inicio()
        
    except:
        print("ERRO")
        time.sleep(1)
        return tela_inicio()

    #ABRIR ARQUIVO E VERIFICAR SE LOGIN ESTA DENTRO -> SE LOGIN NAO ESTIVER, EXIBIR MENSAGEM, ESPERAR E VOLTAR TELA INICIO


#TELA CADASTRO
def cadastro():
    try:
        global nome

        clear()
        nome = input('Digite o seu login: ')
        senha = input('Digite a sua senha: ')

        f = open('login.csv', 'a')
        f.close()

        arquivo = open('login.csv', 'r', encoding='utf8')
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(';')
            if nome == dados[0]:
                print('Nome já existente. Tente novamente')
                time.sleep(1.5)
                return cadastro()
        arquivo.close()

        file = open('login.csv', 'a', encoding='utf8')
        file.write(f'{nome};{senha}\n')
        file.close()
        loading()
        print('Conta criada!')
        time.sleep(1.5)
        return tela_despesas()
    
    except:
        print("ERRO")
        time.sleep(1)
        return tela_inicio()
    

#TELA INICIAL
def tela_inicio():
    try:
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
            return print("FIM DO PROGRAMA")
        else:
            print("Opção não existe. Reiniciando...")
            time.sleep(1)
            tela_inicio()

    except ValueError:
        print("ERRO. CARACTERES INVALIDOS")
        time.sleep(1)
        return tela_inicio()


#TELA PRINCIPAL (PÓS TELA INICIAL DE LOGIN)
def tela_despesas():
    try:
        clear()
        print("-------------[DESPESAS]-------------")
        print("[1]ADICIONAR GASTOS") 
        print("[2]VISUALIZAR")
        print("[3]APAGAR GASTOS")
        print("[4]EDITAR")
        print("\n[5]VOLTAR")

        decisao = int(input())
        if decisao == 1:
            loading()
            return ADICIONAR_GASTOS()
        elif decisao == 2:
            loading()
            return VISUALIZAR_GASTOS()
        elif decisao == 3:
            loading()
            return APAGAR_GASTOS()
        elif decisao == 4:
            loading()
            return EDITAR()
        elif decisao == 5:
            loading()
            return tela_inicio()
        else:
            os.system("cls")
            print("OPÇÃO INVÁLIDA")
            time.sleep(1)
            tela_despesas()

    except ValueError:
        print("ERRO. CARACTERES INVALIDOS")
        time.sleep(1)
        return tela_inicio()


#TELA ADICIONAR GASTOS
def ADICIONAR_GASTOS():
    clear()
    try:
        f = open(f"{nome}.csv", "a")
        titulo = input("Digite o título da despesa: ").lower()
        categoria = input("Digite a categoria da despesa: ").lower()
        valor = float(input("Digite o valor da despesa: "))

        linha = f"{titulo};{categoria};{valor}\n"  # Monta a linha com os valores separados por ponto e vírgula

        f.write(linha)
        f.close()
        tela_despesas()
    except ValueError:
        print("ERRO. CARACTERES INVALIDOS")
        time.sleep(1)
        return ADICIONAR_GASTOS()


#TELA VISUALIZAÇÃO DE GASTOS
def VISUALIZAR_GASTOS():
    clear()
    total_gastos=0
    f = open(f"{nome}.csv", "r")
    linhas = f.readlines()  # Lê todas as linhas do arquivo

    for linha in linhas:
        titulo, categoria, valor = linha.strip().split(";")  # Divide a linha em campos usando o ponto e vírgula como separador
        valor = float(valor)  # Converte o valor para float
        total_gastos+=valor # Adiciona na variavel dos gastos totais

        print("--------------------")
        print("Título:", titulo)
        print("Categoria:", categoria)
        print("Valor:", valor)
        print("--------------------")

    f.close()
    print(f"EXTRATO TOTAL: {total_gastos}")

    print("\n[1]VOLTAR")
    print("[2]APAGAR DESPESA")
    print("[3]PESQUISAR POR CATEGORIA")
    print("[4]EDITAR DESPESA")

    decisao = input()
    if decisao == "1":
        loading()
        tela_despesas()
    elif decisao == "2":
        loading()
        APAGAR_GASTOS()
    elif decisao == "3":
        return VISUALIZACAO_CATEGORIA()
    elif decisao == "4":
        loading()
        return EDITAR()
    else:
        os.system("cls")
        print("OPÇÃO INVÁLIDA")
        print("Retornando...")
        time.sleep(1.5)
        VISUALIZAR_GASTOS()

        

def VISUALIZACAO_CATEGORIA():
    try:
        clear()
        total = 0
        encontrado = False

        categoria = input("Digite a categoria dos gastos a serem exibidos: ").lower()

        f = open(f"{nome}.csv", "r")

        linhas = f.readlines()
        print()
        for linha in linhas:
            campos = linha.strip().split(";")

            if campos[1] == categoria:
                titulo = campos[0]
                valor = float(campos[2])
                print(f"Título: {titulo} | Valor: {valor}")
                total += valor
                encontrado = True
        f.close()

        if encontrado:
            print(f"\nExtrato da categoria '{categoria}': Total = R$ {total:.2f}")
        else:
            print(f"Nenhum gasto encontrado na categoria '{categoria}'.")

        print("\n[1]VOLTAR")

        voltar = int(input())

        if voltar == "1":
            loading()
            VISUALIZAR_GASTOS()
        else:
            time.sleep(1)
            VISUALIZAR_GASTOS()
    except FileNotFoundError:
        print("NENHUM GASTO COMPUTADO")
        time.sleep(1)
        return tela_despesas()

#TELA APAGAR OS GASTOS (INCOMPLETA)
def APAGAR_GASTOS(): #cria um arquivo temporario, onde são armazenados todos os gastos, menos o citado. Daí, o arquivo principal é reescrito com as informações do original.
    try:
        clear()
        titulo = input("Digite o título do gasto a ser removido: ").lower()

        encontrado = False

        with open(f"{nome}.csv", "r") as f, open(f"{nome}_temp.csv", "w") as f_temp:

            linhas = f.readlines()

            for linha in linhas:
                campos = linha.strip().split(";")

                if campos[0] == titulo:
                    encontrado = True
                else:
                    f_temp.write(linha)

        if encontrado:
            with open(f"{nome}.csv", "w") as f, open(f"{nome}_temp.csv", "r") as f_temp:
            
                f.write(f_temp.read())

            with open(f"{nome}_temp.csv", "w"):
                pass

            print(f"Gasto com o título '{titulo}' removido com sucesso.\n")
            time.sleep(1.5)
            tela_despesas()

        else:
            with open(f"{nome}_temp.csv", "w"):
                pass

            print(f"Gasto com o título '{titulo}' não encontrado.\n")
            time.sleep(1.5)
            tela_despesas()

    except:
        print("ERRO")
        time.sleep(1)
        return tela_despesas()

def EDITAR():
    try:
        clear()
        titulo = input("Digite o título da despesa a ser editada: ")

        encontrado = False

        with open(f"{nome}.csv", "r") as f, open(f"{nome}_temp.csv", "w") as f_temp:
            linhas = f.readlines()

            for linha in linhas:
                campos = linha.strip().split(";")

                if campos[0] == titulo:
                    encontrado = True
                    nova_categoria = input("Digite a nova categoria (ou deixe em branco para manter a mesma): ")
                    novo_valor = input("Digite o novo valor (ou deixe em branco para manter o mesmo): ")

                    if nova_categoria == "":
                        nova_categoria = campos[1]
                    if novo_valor == "":
                        novo_valor = campos[2]
                    else:
                        novo_valor = float(novo_valor)

                    nova_linha = f"{titulo};{nova_categoria};{novo_valor}\n"
                    f_temp.write(nova_linha)
                else:
                    f_temp.write(linha)

        if encontrado == True:
            with open(f"{nome}.csv", "w") as f, open(f"{nome}_temp.csv", "r") as f_temp:
                conteudo_temporario = f_temp.read()
                f.write(conteudo_temporario)

            with open(f"{nome}_temp.csv", "w"):
                pass

            print(f"Despesa com o título '{titulo}' atualizada com sucesso.")
        else:
            with open(f"{nome}_temp.csv", "w"):
                pass

            print(f"Despesa com o título '{titulo}' não encontrada.")
        
        print("\n[1]VOLTAR")

        voltar = int(input())

        if voltar == 1:
            loading()
            tela_despesas()
        else:
            time.sleep(1)
            tela_despesas()
        
    except ValueError:
        print("ERRO")
        time.sleep(1)
        return tela_despesas()


tela_inicio()
