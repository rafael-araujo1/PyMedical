import os

os.makedirs("database", exist_ok=True)

medicos = {}

def carregar_medicos():
  dados_iniciais = {
  # CRM: [Nome, Email, Especialização, Idade, Sexo, Telefone]
  "1111111" : ["Tony Honesto Jefferson", "tonyhonesto@email.com", "especial", 15, 'M', "(84) 9 1111-1111"],
  "2222222" : ["Vanessa Scott", "vanessascott@email.com", "especial", 18, 'F', "(84) 9 2222-2222"],
  "3333333" : ["Calvin Scott", "calvinscott@email.com", "especial", 35, 'M', "(84) 9 3333-3333"],
  "4444444" : ["Jasmine Scott", "jasminescott@email.com", "especial", 35, 'F', "(84) 9 4444-4444"],
  "5555555" : ["Franklin Mumford", "franklinmumford@email.com", "especial", 6, 'M', "(84) 9 5555-5555"]
}
  try:
    arq_medicos = open("database/medicos.txt", "rt")
    linhas = arq_medicos.readlines()
    arq_medicos.close()

    if not linhas:
      medicos.update(dados_iniciais)
      salvar_pacientes()
      return

    for linha in linhas:
      dados = linha.strip().split(', ')
      if len(dados) == 7:
        crm = dados[0]
        nome = dados[1]
        email = dados[2]
        especializacao = dados[3]
        idade = dados[4]
        sexo = dados [5]
        telefone = dados[6]
        medicos[crm] = [nome, email, especializacao, idade, sexo, telefone]
  except FileNotFoundError:
    medicos.update(dados_iniciais)
    salvar_medicos()

def cadastrar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR MÉDICO]\n")
    medico_nome = input("Insira o nome do Médico: ")
    medico_email = input("Insira o email do Médico: ")
    medico_especializacao = input("Insira a especialização do Médico: ")
    medico_crm = input("Insira o CRM do Médico: ")
    medico_idade = input("Insira a idade do Médico: ")
    medico_sexo = input("Insira o sexo do Médico: ")
    medico_telefone = input("Insira o telefone do Médico: ")

    medicos[medico_crm] = [medico_nome, medico_email, medico_especializacao,
                            medico_idade, medico_sexo, medico_telefone]
    os.system("cls" if os.name == "nt" else "clear")
    print(f"[MÉDICOS]\n{medicos}")

    print("""
+==============================================+
|                                              |
| x Médico cadastrado com sucesso              |
|                                              |
+==============================================+
""")
    input("Aperte [ENTER] para continuar")


def buscar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR MÉDICO]\n")
    crm = input("Insira o CRM do médico: ")

    if crm in medicos:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[{medicos[crm][0]}]

x Email: {medicos[crm][1]}
x Especialização: {medicos[crm][2]}
x Idade: {medicos[crm][3]}
x Sexo: {medicos[crm][4]}
x Telefone: {medicos[crm][5]}
""")
    else:
        print("Médico não encontrado!\n")
    input("Aperte [ENTER] para continuar")


def atualizar_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[ALTERAR DADOS DO MÉDICO]\n")

    crm = input("Insira um CRM: ")
    if crm in medicos:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[DADOS ATUAIS DO MÉDICO]
              
x Nome: {medicos[crm][0]}
x Email: {medicos[crm][1]}
x Especialização: {medicos[crm][2]}
x Idade: {medicos[crm][3]}
x Sexo: {medicos[crm][4]}
x Telefone: {medicos[crm][5]}
""")

        print("[NOVOS DADOS]\n")
        nome = input("Insira o nome do Médico: ")
        email = input("Insira o email do Médico: ")
        especializacao = input("Insira a especialização do Médico: ")
        idade = input("Insira a idade do Médico: ")
        sexo = input("Insira o sexo do Médico: ")
        telefone = input("Insira o telefone do Médico: ")
        
        medicos[crm] = [nome, email, especializacao, idade, sexo, telefone]

        print("""
+==============================================+
|                                              |
| x Médico alterado com sucesso                |
|                                              |
+==============================================+
""")

    else:
        print("Médico não encontrado!")
    input("Aperte [ENTER] para continuar")


def excluir_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR MÉDICO]\n")
    crm = input("Insira o CRM do Médico: ")
    if crm in medicos:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""x Nome: {medicos[crm][0]}
x Email: {medicos[crm][1]}
x Especialização: {medicos[crm][2]}
x Idade: {medicos[crm][3]}
x Sexo: {medicos[crm][4]}
x Telefone: {medicos[crm][5]}
""")
        opc_exclusao = input("Realmente deseja excluir o médico [S/N]? ").upper()
        if opc_exclusao == 'S':
          del medicos[crm]
          print(f"Médicos: {medicos}")
          print("""
+==============================================+
|                                              |
| x Médico excluído com sucesso                |
|                                              |
+==============================================+
""")
        else:
          print("Exclusão cancelada!")
    else:
        print("Médico não encontrado!\n")
    input("Pressione [ENTER] para voltar")


def salvar_medicos():
    arq_medicos = open("database/medicos.txt", "wt")

    for crm in medicos:
        nome = medicos[crm][0]
        email = medicos[crm][1]
        especializacao = medicos[crm][2]
        idade = medicos[crm][3]
        sexo = medicos[crm][4]
        telefone = medicos[crm][5]
        arq_medicos.write(f"{crm}, {nome}, {email}, {especializacao}, {idade}, {sexo}, {telefone}\n")
    arq_medicos.close()


def listar_medicos():
    os.system("cls" if os.name == "nt" else "clear")
    print("[MÉDICOS]\n")

    if not medicos:
        print("Não há médicos cadastrados no sistema.\n")

    else:
        print(f"{'NOME':<22} | {'CRM':<28} | {'ESPECIALIZAÇÃO':<28} | {'EMAIL':<28} | {'IDADE':<5} | {'SEXO':<4} | {'TELEFONE'}")
        print('-' * 140)
        for crm, dados in medicos.items():
            nome = dados[0]
            email = dados[1]
            especializacao = dados[2]
            idade = dados[3]
            sexo = dados[4]
            telefone = dados[5]
            print(f"{nome:<22} | {crm:<28} | {especializacao:<28} | {email:<28} | {idade:<5} | {sexo:<4} | {telefone}")
        print('-' * 140)

    input("\nPressione [ENTER] para voltar")
    