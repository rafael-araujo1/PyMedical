import os

os.makedirs("database", exist_ok=True)

pacientes = {}

def carregar_pacientes():
    dados_iniciais = {
  # EMAIL: [Nome, Idade, Sexo, Telefone]
  "michaelkyle@email.com" : ["Michael Kyle", 35, 'M', "(84) 9 1111-1111"],
  "jaykyle@email.com" : ["Janet Kyle", 35, 'F', "(84) 9 2222-2222"],
  "kylejr@email.com" : ["Michael Kyle Jr.", 18, 'M', "(84) 9 3333-3333"],
  "clairekyle@email.com" : ["Claire Kyle", 16, 'F', "(84) 9 4444-4444"],
  "kadykyle@email.com" : ["Kady Kyle", 6, 'F', "(84) 9 5555-5555"]
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
            if len(dados) == 5:
                email = dados[0]
                nome = dados[1]
                idade = int(dados[2])
                sexo = dados[3]
                telefone = dados[4]
                pacientes[email] = [nome, idade, sexo, telefone]
    except FileNotFoundError:
        pacientes.update(dados_iniciais)
        salvar_pacientes()

def cadastrar_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR PACIENTE]\n")
    paciente_nome = input("Insira o nome do paciente: ")
    paciente_email = input("Insira o email do paciente: ")
    paciente_idade = input("Insira a idade do paciente: ")
    paciente_sexo = input("Insira o sexo do paciente: ")
    paciente_telefone = input("Insira o telefone do paciente: ")
    pacientes[paciente_email] = [paciente_nome, paciente_idade, paciente_sexo, paciente_telefone]
    os.system("cls" if os.name == "nt" else "clear")
    print(f"[PACIENTES]\n{pacientes}")

    print("""
+==============================================+
|                                              |
| x Paciente cadastrado com sucesso            |
|                                              |
+==============================================+
""")
    input("Aperte [ENTER] para continuar")


def buscar_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR PACIENTE]\n")
    email = input("Insira o email do paciente: ")
    if email in pacientes:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[{pacientes[email][0]}]

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

    email = input("Insira um email: ")
    if email in pacientes:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[DADOS ATUAIS DO PACIENTE]
              
x Nome: {pacientes[email][0]}
x Idade: {pacientes[email][1]}
x Sexo: {pacientes[email][2]}
x Telefone: {pacientes[email][3]}
""")

        print("[NOVOS DADOS]\n")
        nome = input("Insira o nome do paciente: ")
        idade = input("Insira a idade do paciente: ")
        sexo = input("Insira o sexo do paciente: ")
        telefone = input("Insira o telefone do paciente: ")
        
        pacientes[email] = [nome, idade, sexo, telefone]

        print("""
+==============================================+
|                                              |
| x Paciente alterado com sucesso              |
|                                              |
+==============================================+
""")

    else:
        print("Paciente não encontrado!")
    input("Aperte [ENTER] para continuar")


def excluir_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR PACIENTE]\n")
    email = input("Insira o email do paciente: ")
    if email in pacientes:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[{pacientes[email][0]}]
              
x Idade:{ pacientes[email][1]}
x Sexo: {pacientes[email][2]}
x Telefone: {pacientes[email][3]}
""")
        opc_exclusao = input("Realmente deseja excluir o paciente [S/N]? ").upper()
        if opc_exclusao == 'S':
          del pacientes[email]
          print(f"Pacientes: {pacientes}")
          print("""
+==============================================+
|                                              |
| x Paciente excluído com sucesso              |
|                                              |
+==============================================+
""")
        else:
          print("Exclusão cancelada!")
    else:
        print("Paciente não encontrado!\n")
    input("Pressione [ENTER] para voltar")


def salvar_pacientes():
    arq_pacientes = open("database/pacientes.txt", 'wt')

    for email in pacientes:
        nome = pacientes[email][0]
        idade = pacientes[email][1]
        sexo = pacientes[email][2]
        telefone = pacientes[email][3]
        arq_pacientes.write(f"{email}, {nome}, {idade}, {sexo}, {telefone}\n")
    arq_pacientes.close()


def listar_pacientes():
    os.system("cls" if os.name == "nt" else "clear")
    print("[PACIENTES]\n")

    if not pacientes:
        print("Não há pacientes cadastrados no sistema.\n")

    else:
        print(f"{'NOME':<22} | {'EMAIL':<28} | {'IDADE':<5} | {'SEXO':<4} | {'TELEFONE'}")
        print('-' * 90)
        for email, dados in pacientes.items():
            nome = dados[0]
            idade = dados[1]
            sexo = dados[2]
            telefone = dados[3]
            print(f"{nome:<22} | {email:<28} | {idade:<5} | {sexo:<4} | {telefone}")
            print('-' * 90)

    input("\nPressione [ENTER] para voltar")
    
