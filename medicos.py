import os
import re

os.makedirs("database", exist_ok=True)

medicos = {}

def validar_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)

def validar_telefone(telefone):
    return re.match(r"^\(\d{2}\) 9\d{4}-\d{4}$", telefone)

def validar_cpf(cpf):
    return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf)

def validar_crm(crm):
    return re.match(r"^[A-Z]{2} \d{6}$", crm)

def carregar_medicos():
    # CRM: [Nome, Email, Especialização, Idade, Sexo, Telefone, CPF, Status_Ativo]
    dados_iniciais = {
        "RN 111111" : ["Tony Honesto Jefferson", "tonyhonesto@email.com", "Clínica Geral", 15, 'M', "(84) 91111-1111", "111.111.111-11", True],
        "RN 222222" : ["Vanessa Scott", "vanessascott@email.com", "Clínica Geral", 18, 'F', "(84) 92222-2222", "222.222.222-22", True],
        "RN 333333" : ["Calvin Scott", "calvinscott@email.com", "Clínica Geral", 35, 'F', "(84) 93333-3333", "333.333.333-33", True],
        "RN 444444" : ["Jasmine Scott", "jasminescott@email.com", "Clínica Geral", 35, 'F', "(84) 94444-4444", "444.444.444-44", True],
        "RN 555555" : ["Franklin Mumford", "franklinmumford@email.com", "Clínica Geral", 6, 'F', "(84) 95555-5555", "555.555.555-55", True]

    }
    try:
        arq_medicos = open("database/medicos.txt", "rt")
        linhas = arq_medicos.readlines()
        arq_medicos.close()

        if not linhas:
            medicos.update(dados_iniciais)
            salvar_medicos()
            return

        for linha in linhas:
            dados = linha.strip().split(', ')
            if len(dados) == 9:
                crm = dados[0]
                nome = dados[1]
                email = dados[2]
                especializacao = dados[3]
                idade = int(dados[4])
                sexo = dados[5]
                telefone = dados[6]
                cpf = dados[7]
                status_ativo = True if dados[8] == 'True' else False 
                
                medicos[crm] = [nome, email, especializacao, idade, sexo, telefone, cpf, status_ativo]
    except FileNotFoundError:
        medicos.update(dados_iniciais)
        salvar_medicos()

def salvar_medicos():
    arq_medicos = open("database/medicos.txt", "wt")
    for crm, dados in medicos.items():
        nome = dados[0]
        email = dados[1]
        especializacao = dados[2]
        idade = dados[3]
        sexo = dados[4]
        telefone = dados[5]
        cpf = dados[6]
        status = dados[7]
        arq_medicos.write(f"{crm}, {nome}, {email}, {especializacao}, {idade}, {sexo}, {telefone}, {cpf}, {status}\n")
    arq_medicos.close()

def cadastrar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR MÉDICO]\n")
    
    crm_valido = False
    while not crm_valido:
        crm = input("Insira o CRM [UF 123456]: ").upper()
        if not validar_crm(crm):
            print("Erro: O CRM deve seguir o formato 'UF 123456'.")
        elif crm in medicos:
            print("Erro: Este CRM já está cadastrado no sistema.")
        else:
            crm_valido = True

    nome = input("Insira o nome do Médico: ")

    email_valido = False
    while not email_valido:
        email = input("Insira o email [nome@email.com]: ")
        if not validar_email(email):
            print("Erro: O email deve conter '@.'")
        else:
            email_valido = True

    especializacao = input("Insira a especialização do Médico: ")

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
        sexo = input("Insira o sexo [M/F]: ").upper()
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

    medicos[crm] = [nome, email, especializacao, idade, sexo, telefone, cpf, True]
    
    print("""\n+==============================================+
|                                              |
| x Médico cadastrado com sucesso              |
|                                              |
+==============================================+\n""")
    input("Aperte [ENTER] para continuar")

def buscar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR MÉDICO]\n")
    crm = input("Insira o CRM do médico: ").upper()

    if crm in medicos and medicos[crm][7] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[{medicos[crm][0]}]")
x CPF: {medicos[crm][6]}")
x Email: {medicos[crm][1]}")
x Especialização: {medicos[crm][2]}")
x Idade: {medicos[crm][3]}")
x Sexo: {medicos[crm][4]}")
x Telefone: {medicos[crm][5]}
""")
        
    else:
        print("Médico não encontrado!\n")
    input("Aperte [ENTER] para continuar")

def atualizar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[ALTERAR DADOS DO MÉDICO]\n")

    crm = input("Insira o CRM do médico que deseja alterar: ").upper()
    
    if crm in medicos and medicos[crm][7] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[DADOS ATUAIS]\
Nome: {medicos[crm][0]}
Email: {medicos[crm][1]}
Especialização: {medicos[crm][2]}
Idade: {medicos[crm][3]}
Sexo: {medicos[crm][4]}
Telefone: {medicos[crm][5]}
CPF: {medicos[crm][6]}
""")
        
        print("[NOVOS DADOS]")
        
        nome = input("Insira o novo nome: ")

        email_valido = False
        while not email_valido:
            email = input("Insira o novo email [nome@email.com]: ")
            if not validar_email(email):
                print("Erro: O email deve conter '@.'")
            else:
                email_valido = True

        especializacao = input("Insira a nova especialização: ")

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
            telefone = input("Insira o novo telefone [(11) 91111-1111]: ")
            if validar_telefone(telefone):
                telefone_valido = True
            else:
                print("Erro: Siga estritamente o formato (XX) 9XXXX-XXXX.")

        cpf_valido = False
        while not cpf_valido:
            cpf = input("Insira o novo CPF [111.111.111-11]: ")
            if validar_cpf(cpf):
                cpf_valido = True
            else:
                print("Erro: Siga estritamente o formato XXX.XXX.XXX-XX.")

        medicos[crm] = [nome, email, especializacao, idade, sexo, telefone, cpf, True]

        print("""\n+==============================================+
|                                              |
| x Médico atualizado com sucesso              |
|                                              |
+==============================================+\n""")
    else:
        print("Médico não encontrado!")
    
    input("Aperte [ENTER] para continuar")

def excluir_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR MÉDICO]\n")
    crm = input("Insira o CRM do Médico: ").upper()
    
    if crm in medicos and medicos[crm][7] == True:
        print(f"Deseja excluir o médico {medicos[crm][0]}?")
        opc_exclusao = input("[S/N]: ").upper()
        
        if opc_exclusao == 'S':
            medicos[crm][7] = False
            print("""\n+==============================================+
|                                              |
| x Médico excluído com sucesso                |
|                                              |
+==============================================+\n""")
        else:
            print("Exclusão cancelada!")
    else:
        print("Médico não encontrado!\n")
    input("Pressione [ENTER] para voltar")

def listar_medicos():
    os.system("cls" if os.name == "nt" else "clear")
    print("[MÉDICOS ATIVOS]\n")

    medicos_ativos = {crm: dados for crm, dados in medicos.items() if dados[7] == True}

    if not medicos_ativos:
        print("Não há médicos ativos cadastrados no sistema.\n")
    else:
        print(f"{'NOME':<22} | {'CRM':<10} | {'CPF':<15} | {'ESPECIALIZAÇÃO':<15} | {'EMAIL':<25} | {'IDADE':<5} | {'SEXO':<4} | {'TELEFONE'}")
        print('-' * 130)
        for crm, dados in medicos_ativos.items():
            print(f"{dados[0]:<22} | {crm:<10} | {dados[6]:<15} | {dados[2]:<15} | {dados[1]:<25} | {dados[3]:<5} | {dados[4]:<4} | {dados[5]}")
            print('-' * 130)

    input("\nPressione [ENTER] para voltar")

def listar_medicos_especialidade():
    os.system("cls" if os.name == "nt" else "clear")
    print("[MÉDICOS POR ESPECIALIZAÇÃO]\n")
    
    especializacao = input("Insira a especialização que deseja procurar: ")
    encontrou_medico = False
    
    print(f"\nMédicos encontrados na especialização: {especializacao.title()}\n")
    print(f"{'NOME':<22} | {'CRM':<10} | {'CPF':<15} | {'EMAIL':<25} | {'TELEFONE'}")
    print('-' * 105)
    
    for crm, dados in medicos.items():
        if dados[7] == True and dados[2].upper() == especializacao.upper():
            print(f"{dados[0]:<22} | {crm:<10} | {dados[6]:<15} | {dados[1]:<25} | {dados[5]}")
            print('-' * 105)
            encontrou_medico = True
            
    if not encontrou_medico:
        print(f"Não há médicos especializados em '{especializacao}'.")
        print('-' * 105)
        
    input("\nPressione [ENTER] para voltar")
