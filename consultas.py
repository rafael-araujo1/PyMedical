import os

os.makedirs("database", exist_ok=True)

consultas = {}

def carregar_consultas():
    dados_iniciais = {
  # CÓDIGO: [Dia, Horário, Paciente(email), Médico(CRM)]
  "111" : ["segunda-feira", "7:00", "kylejr@email.com", "2222222"],
  "222" : ["terca-feira", "7:00", "michaelkyle@email.com", "3333333"],
  "333" : ["quarta-feira", "7:00", "jaykyle@email.com", "2222222"],
  "444" : ["quinta-feira", "7:00", "kadyklye@email.com", "5555555"],
  "555" : ["sexta-feira", "7:00", "clairekyle@email.com", "1111111"]
}
    try:
        arq_consultas = open("database/consutltas.txt", "rt")
        linhas = arq_consultas.readlines()
        arq_consultas.close()

        if not linhas:
            consultas.update(dados_iniciais)
            salvar_consultas()
            return
        

        for linha in linhas:
            dados = linha.strip().split(', ')
            if len(dados) == 5:
                codigo = dados[0]
                dia = dados[1]
                horario = dados[2]
                paciente = dados[3]
                medico = dados[4]
                consultas[codigo] = [dia, horario, paciente, medico]
    except FileNotFoundError:
        consultas.update(dados_iniciais)
        salvar_consultas()


def cadastrar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR CONSULTA]\n")
    consulta_codigo = input("Insira o código da Consulta: ")
    consulta_dia = input("Insira o dia da Consulta: ")
    consulta_horario = input("Insira o horário da Consulta: ")
    consulta_paciente = input("Insira o paciente da Consulta [EMAIL]: ")
    consulta_medico = input("Insira o médico da Consulta [CRM]: ")

    consultas[consulta_codigo] = [consulta_dia, consulta_horario, consulta_paciente, consulta_medico]
    os.system("cls" if os.name == "nt" else "clear")
    print(f"[CONSULTAS]\n{consultas}")

    print("""
+==============================================+
|                                              |
| x Consulta cadastrada com sucesso            |
|                                              |
+==============================================+
""")
    input("Aperte [ENTER] para continuar")


def buscar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR CONSULTA]\n")
    codigo = input("Insira o código da Consulta: ")
    if codigo in consultas:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[CONSULTA {codigo}]

x Dia: {consultas[codigo][0]}
x Horário: {consultas[codigo][1]}
x Paciente: {consultas[codigo][2]}
x Médico: {consultas[codigo][3]}
""")
    else:
        print("Consulta não encontrada!\n")
    input("Aperte [ENTER] para continuar")


def atualizar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[ALTERAR DADOS DA CONSULTA]\n")

    codigo = input("Insira um código: ")
    if codigo in consultas:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[DADOS ATUAIS DA CONSULTA]
            
x Dia: {consultas[codigo][0]}
x Horário: {consultas[codigo][1]}
x Paciente: {consultas[codigo][2]}
x Médico: {consultas[codigo][3]}
""")

        print("[NOVOS DADOS]\n")
        dia = input("Insira o dia da Consulta: ")
        horario = input("Insira o horário da Consulta: ")
        paciente = input("Insira o paciente da Consulta [EMAIL]: ")
        medico = input("Insira o médico da Consulta [CRM]: ")
        
        consultas[codigo] = [dia, horario, paciente, medico]

        print("""
    +==============================================+
    |                                              |
    | x Consulta alterada com sucesso              |
    |                                              |
    +==============================================+
    """)

    else:
        print("Consulta não encontrada!")
    input("Aperte [ENTER] para continuar")


def excluir_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR CONSULTA]\n")
    codigo = input("Insira o código da Consulta: ")
    if codigo in consultas:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""[CONSULTA {codigo}]
            
x Dia: {consultas[codigo][0]}
x Horário: {consultas[codigo][1]}
x Paciente: {consultas[codigo][2]}
x Médico: {consultas[codigo][3]}
""")
        opc_exclusao = input("Realmente deseja excluir a consulta [S/N]? ").upper()
        if opc_exclusao == 'S':
            del consultas[codigo]
            print(f"Consultas: {consultas}")
            print("""
+==============================================+
|                                              |
| x Consulta excluída com sucesso              |
|                                              |
+==============================================+
""")
        else:
            print("Exclusão cancelada!")
    else:
        print("Consulta não encontrada!\n")
    input("Pressione [ENTER] para voltar")


def salvar_consultas():
    arq_consultas = open("database/consultas.txt", "wt")

    for codigo in consultas:
        dia = consultas[codigo][0]
        horario = consultas[codigo][1]
        paciente = consultas[codigo][2]
        medico = consultas[codigo][3]
        arq_consultas.write(f"{codigo}, {dia}, {horario}, {paciente}, {medico}\n")
    arq_consultas.close()
