import os
import re

os.makedirs("database", exist_ok=True)

pacientes = {}

def validar_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)

def validar_telefone(telefone):
    return re.match(r"^\(\d{2}\) 9\d{4}-\d{4}$", telefone)

def validar_cpf(cpf):
    return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf)

def carregar_pacientes():
    # Email: [Nome, Idade, Sexo, Telefone, CPF, Status_Ativo]
    dados_iniciais = {
        "michaelkyle@email.com" : ["Michael Kyle", 35, 'M', "(84) 91111-1111", "111.111.111-11", True],
        "jaykyle@email.com" : ["Janet Kyle", 35, 'F', "(84) 92222-2222", "222.222.222-22", True],
        "kylejr@email.com" : ["Michael Kyle Jr.", 17, 'M', "(84) 93333-3333", "333.333.333-33", True],
        "clairekyle@email.com" : ["Claire Kyle", 15, 'F', "(84) 94444-4444", "444.444.444-44", True],
        "kadykyle@email.com" : ["Kady Kyle", 6, 'F', "(84) 92222-2222", "555.555.555-55", True]
    }
    try:
        arq_pacientes = open("database/pacientes.txt", "rt")
        linhas = arq_pacientes.readlines()
        arq_pacientes.close()

        if not linhas:
            pacientes.update(dados_iniciais)
            salvar_pacientes()
            return
        
        for linha in linhas:
            dados = linha.strip().split(', ')
            if len(dados) == 6:
                email = dados[0]
                nome = dados[1]
                idade = int(dados[2])
                sexo = dados[3]
                telefone = dados[4]
                cpf = dados[5]
                status_ativo = True if dados[6] == 'True' else False 
                
                pacientes[email] = [nome, idade, sexo, telefone, cpf, status_ativo]
    except FileNotFoundError:
        pacientes.update(dados_iniciais)
        salvar_pacientes()

def salvar_pacientes():
    arq_pacientes = open("database/pacientes.txt", 'wt')
    for email, dados in pacientes.items():
        nome = dados[0]
        idade = dados[1]
        sexo = dados[2]
        telefone = dados[3]
        cpf = dados[4]
        status = dados[5]
        arq_pacientes.write(f"{email}, {nome}, {idade}, {sexo}, {telefone}, {cpf}, {status}\n")
    arq_pacientes.close()

def cadastrar_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR PACIENTE]\n")
    
    email_valido = False
    while not email_valido:
        email = input("Insira o email [nome@email.com]: ")
        if not validar_email(email):
            print("Erro: O email deve conter '@.'")
        elif email in pacientes:
            print("Erro: Este email já está cadastrado no sistema.")
        else:
            email_valido = True

    nome = input("Insira o nome do paciente: ")

    idade_valida = False
    while not idade_valida:
        idade_input = input("Insira a idade: ")
        if idade_input.isdigit() and int(idade_input) > 0:
            idade = int(idade_input)
            idade_valida = True
        else:
            print("Erro: A idade deve ser maior que 0.")

    sexo_valido = False
    while not sexo_valido:
        sexo = input("Insira o sexo (M/F): ").upper()
        if sexo in ['M', 'F']:
            sexo_valido = True
        else:
            print("Erro: O sexo deve ser 'M' ou 'F'.")

    telefone_valido = False
    while not telefone_valido:
        telefone = input("Insira o telefone [(11) 91111-1111]: ")
        if validar_telefone(telefone):
            telefone_valido = True
        else:
            print("Erro: Siga estritamente o formato (XX) 9XXXX-XXXX.")

    cpf_valido = False
    while not cpf_valido:
        cpf = input("Insira o CPF [111.111.111-11]: ")
        if validar_cpf(cpf):
            cpf_valido = True
        else:
            print("Erro: Siga estritamente o formato XXX.XXX.XXX-XX.")

    pacientes[email] = [nome, idade, sexo, telefone, cpf, True]
    
    print("""\n+==============================================+
|                                              |
| x Paciente cadastrado com sucesso            |
|                                              |
+==============================================+\n""")
    input("Aperte [ENTER] para continuar")

def buscar_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR PACIENTE]\n")
    email = input("Insira o email do paciente: ")
    
    if email in pacientes and pacientes[email][5] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[{pacientes[email][0]}]
x CPF: {pacientes[email][4]}
x Idade: {pacientes[email][1]}
x Sexo: {pacientes[email][2]}
x Telefone: {pacientes[email][3]}
""")
    else:
        print("Paciente não encontrado!\n")
    input("Aperte [ENTER] para continuar")

def atualizar_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[ALTERAR DADOS DO PACIENTE]\n")

    email = input("Insira o email do paciente que deseja alterar: ")
    
    if email in pacientes and pacientes[email][5] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[DADOS ATUAIS]
Nome: {pacientes[email][0]}
Idade: {pacientes[email][1]}
Sexo: {pacientes[email][2]}
Telefone: {pacientes[email][3]}
CPF: {pacientes[email][4]}
""")
        print("[NOVOS DADOS]")
        
        nome = input("Insira o novo nome: ")

        idade_valida = False
        while not idade_valida:
            idade_input = input("Insira a nova idade: ")
            if idade_input.isdigit() and int(idade_input) > 0:
                idade = int(idade_input)
                idade_valida = True
            else:
                print("Erro: A idade deve ser maior que 0.")

        sexo_valido = False
        while not sexo_valido:
            sexo = input("Insira o novo sexo (M/F): ").upper()
            if sexo in ['M', 'F']:
                sexo_valido = True
            else:
                print("Erro: O sexo deve ser 'M' ou 'F'.")

        telefone_valido = False
        while not telefone_valido:
            telefone = input("Insira o novo telefone no formato (11) 91111-1111: ")
            if validar_telefone(telefone):
                telefone_valido = True
            else:
                print("Erro: Siga estritamente o formato (XX) 9XXXX-XXXX.")

        cpf_valido = False
        while not cpf_valido:
            cpf = input("Insira o novo CPF no formato 111.111.111-11: ")
            if validar_cpf(cpf):
                cpf_valido = True
            else:
                print("Erro: Siga estritamente o formato XXX.XXX.XXX-XX.")

        pacientes[email] = [nome, idade, sexo, telefone, cpf, True]

        print("""\n+==============================================+
|                                              |
| x Paciente atualizado com sucesso            |
|                                              |
+==============================================+\n""")
    else:
        print("Paciente não encontrado!")
    
    input("Aperte [ENTER] para continuar")

def excluir_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR PACIENTE]\n")
    email = input("Insira o email do paciente: ")
    
    if email in pacientes and pacientes[email][5] == True:
        print(f"Deseja excluir o paciente {pacientes[email][0]}?")
        opc_exclusao = input("[S/N]: ").upper()
        
        if opc_exclusao == 'S':
            pacientes[email][5] = False
            print("""\n+==============================================+
|                                              |
| x Paciente excluído com sucesso              |
|                                              |
+==============================================+\n""")
        else:
            print("Exclusão cancelada!")
    else:
        print("Paciente não encontrado!\n")
    input("Pressione [ENTER] para voltar")

def listar_pacientes():
    os.system("cls" if os.name == "nt" else "clear")
    print("[PACIENTES ATIVOS]\n")

    pacientes_ativos = {email: dados for email, dados in pacientes.items() if dados[5] == True}

    if not pacientes_ativos:
        print("Não há pacientes ativos cadastrados no sistema.\n")
    else:
        print(f"{'NOME':<22} | {'EMAIL':<28} | {'CPF':<15} | {'IDADE':<5} | {'SEXO':<4} | {'TELEFONE'}")
        print('-' * 110)
        for email, dados in pacientes_ativos.items():
            print(f"{dados[0]:<22} | {email:<28} | {dados[4]:<15} | {dados[1]:<5} | {dados[2]:<4} | {dados[3]}")
            print('-' * 110)

    input("\nPressione [ENTER] para voltar")
