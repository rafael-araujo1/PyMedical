import os
import re
from datetime import datetime

os.makedirs("database", exist_ok=True)

consultas = {}

def validar_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)

def validar_crm(crm):
    return re.match(r"^[A-Z]{2} \d{6}$", crm)

def validar_horario(horario):
    return re.match(r"^([01]\d|2[0-3]):[0-5]\d$", horario)

def validar_dia_futuro(dia_str):
    try:
        data_inserida = datetime.strptime(dia_str, "%d/%m/%Y").date()
        data_atual = datetime.now().date()
        return data_inserida >= data_atual 
    except ValueError:
        return False

def carregar_consultas():
    # [Dia, Horário, Paciente(email), Médico(CRM), Status_Ativo]
    dados_iniciais = {
        "111" : ["31/12/2026", "07:00", "kylejr@email.com", "RJ 222222", True],
        "222" : ["31/12/2026", "08:00", "michaelkyle@email.com", "SP 111111", True]
    }
    try:
        arq_consultas = open("database/consultas.txt", "rt")
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
                status_ativo = True if dados[5] == 'True' else False
                
                consultas[codigo] = [dia, horario, paciente, medico, status_ativo]
    except FileNotFoundError:
        consultas.update(dados_iniciais)
        salvar_consultas()

def salvar_consultas():
    arq_consultas = open("database/consultas.txt", "wt")
    for codigo, dados in consultas.items():
        dia = dados[0]
        horario = dados[1]
        paciente = dados[2]
        medico = dados[3]
        status = dados[4]
        arq_consultas.write(f"{codigo}, {dia}, {horario}, {paciente}, {medico}, {status}\n")
    arq_consultas.close()

def cadastrar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CADASTRAR CONSULTA]\n")
    
    codigo_valido = False
    while not codigo_valido:
        consulta_codigo = input("Insira o código da Consulta: ")
        if consulta_codigo in consultas:
            print("Erro: Este código já está sendo utilizado.")
        else:
            codigo_valido = True

    dia_valido = False
    while not dia_valido:
        consulta_dia = input("Insira o dia da Consulta (DD/MM/AAAA): ")
        if not validar_dia_futuro(consulta_dia):
            print("Erro: A data deve estar no formato correto e não pode ser um dia no passado.")
        else:
            dia_valido = True

    horario_valido = False
    while not horario_valido:
        consulta_horario = input("Insira o horário da Consulta (HH:MM): ")
        if not validar_horario(consulta_horario):
            print("Erro: O horário deve seguir o formato HH:MM (ex: 14:30).")
        else:
            horario_valido = True

    paciente_valido = False
    while not paciente_valido:
        consulta_paciente = input("Insira o email do paciente: ")
        if not validar_email(consulta_paciente):
             print("Erro: O email deve conter '@' e '.' após o '@'.")
        else:
             paciente_valido = True

    medico_valido = False
    while not medico_valido:
        consulta_medico = input("Insira o CRM do médico (ex: SP 123456): ").upper()
        if not validar_crm(consulta_medico):
             print("Erro: O CRM deve seguir o formato 'UF 123456'.")
        else:
             medico_valido = True

    consultas[consulta_codigo] = [consulta_dia, consulta_horario, consulta_paciente, consulta_medico, True]
    
    print("\n+==============================================+")
    print("| x Consulta cadastrada com sucesso            |")
    print("+==============================================+\n")
    input("Aperte [ENTER] para continuar")

def buscar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[BUSCAR CONSULTA]\n")
    codigo = input("Insira o código da Consulta: ")
    
    if codigo in consultas and consultas[codigo][4] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"[CONSULTA {codigo}]")
        print(f"x Dia: {consultas[codigo][0]}")
        print(f"x Horário: {consultas[codigo][1]}")
        print(f"x Paciente: {consultas[codigo][2]}")
        print(f"x Médico: {consultas[codigo][3]}")
    else:
        print("Consulta não encontrada ou cancelada!\n")
    input("Aperte [ENTER] para continuar")

def atualizar_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[ALTERAR DADOS DA CONSULTA]\n")

    codigo = input("Insira um código: ")
    if codigo in consultas and consultas[codigo][4] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"[DADOS ATUAIS DA CONSULTA]\nDia: {consultas[codigo][0]}\nHorário: {consultas[codigo][1]}\nPaciente: {consultas[codigo][2]}\nMédico: {consultas[codigo][3]}\n")
        print("[NOVOS DADOS]")
        
        dia_valido = False
        while not dia_valido:
            dia = input("Insira o novo dia da Consulta (DD/MM/AAAA): ")
            if not validar_dia_futuro(dia):
                print("Erro: A data deve estar no formato correto e não pode ser um dia no passado.")
            else:
                dia_valido = True

        horario_valido = False
        while not horario_valido:
            horario = input("Insira o novo horário da Consulta (HH:MM): ")
            if not validar_horario(horario):
                print("Erro: O horário deve seguir o formato HH:MM (ex: 14:30).")
            else:
                horario_valido = True

        paciente_valido = False
        while not paciente_valido:
            paciente = input("Insira o novo email do paciente: ")
            if not validar_email(paciente):
                 print("Erro: O email deve conter '@' e '.' após o '@'.")
            else:
                 paciente_valido = True

        medico_valido = False
        while not medico_valido:
            medico = input("Insira o novo CRM do médico (ex: SP 123456): ").upper()
            if not validar_crm(medico):
                 print("Erro: O CRM deve seguir o formato 'UF 123456'.")
            else:
                 medico_valido = True
        
        consultas[codigo] = [dia, horario, paciente, medico, True]

        print("\n+==============================================+")
        print("| x Consulta alterada com sucesso              |")
        print("+==============================================+\n")
    else:
        print("Consulta não encontrada!")
    input("Aperte [ENTER] para continuar")

def excluir_consulta():
    os.system("cls" if os.name == "nt" else "clear")
    print("[EXCLUIR CONSULTA]\n")
    codigo = input("Insira o código da Consulta: ")
    
    if codigo in consultas and consultas[codigo][4] == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"[CONSULTA {codigo}]\nDia: {consultas[codigo][0]}\nHorário: {consultas[codigo][1]}\nPaciente: {consultas[codigo][2]}\nMédico: {consultas[codigo][3]}\n")
        opc_exclusao = input("Realmente deseja excluir a consulta [S/N]? ").upper()
        
        if opc_exclusao == 'S':
            consultas[codigo][4] = False
            print("\n+==============================================+")
            print("| x Consulta excluída com sucesso (Soft Delete)|")
            print("+==============================================+\n")
        else:
            print("Exclusão cancelada!")
    else:
        print("Consulta não encontrada!\n")
    input("Pressione [ENTER] para voltar")

def listar_consultas():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CONSULTAS ATIVAS]\n")

    consultas_ativas = {codigo: dados for codigo, dados in consultas.items() if dados[4] == True}

    if not consultas_ativas:
        print("Não há consultas ativas cadastradas no sistema.\n")
    else:
        print('-' * 107)
        print(f"| {'CÓDIGO':<10} | {'DIA':<14} | {'HORÁRIO':<12} | {'PACIENTE':<28} | {'MÉDICO':<28}|")
        print('-' * 107)
        for codigo, dados in consultas_ativas.items():
            print(f"| {codigo:<10} | {dados[0]:<14} | {dados[1]:<12} | {dados[2]:<28} | {dados[3]:<28}|")
            print('-' * 107)

    input("\nPressione [ENTER] para voltar")

def listar_consultas_paciente():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CONSULTAS POR PACIENTE]\n")
    paciente_email = input("Insira o email do Paciente: ")
    email_encontrado = False

    print(f"\nConsultas marcadas para o(a) paciente {paciente_email}:\n")
    print('-' * 107)
    print(f"| {'CÓDIGO':<10} | {'DIA':<14} | {'HORÁRIO':<12} | {'PACIENTE':<28} | {'MÉDICO':<28}|")
    print('-' * 107)

    for codigo, dados in consultas.items():
        if dados[4] == True and paciente_email == dados[2]:
            print(f"| {codigo:<10} | {dados[0]:<14} | {dados[1]:<12} | {dados[2]:<28} | {dados[3]:<28}|")
            email_encontrado = True
    
    if not email_encontrado:
        print(f"\nNenhuma consulta ativa marcada para {paciente_email}")
        print('-' * 107)
    else:
        print('-' * 107)
    
    input("\nPressione [ENTER] para voltar")

def listar_consultas_medico():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CONSULTAS POR MÉDICO]\n")
    medico_crm = input("Insira o CRM do Médico: ").upper()
    crm_encontrado = False
    
    print(f"\nConsultas marcadas para o(a) doutor(a) {medico_crm}:\n")
    print('-' * 107)
    print(f"| {'CÓDIGO':<10} | {'DIA':<14} | {'HORÁRIO':<12} | {'PACIENTE':<28} | {'MÉDICO':<28}|")
    print('-' * 107)

    for codigo, dados in consultas.items():
        if dados[4] == True and medico_crm == dados[3]:
            print(f"| {codigo:<10} | {dados[0]:<14} | {dados[1]:<12} | {dados[2]:<28} | {dados[3]:<28}|")
            crm_encontrado = True
    
    if not crm_encontrado:
        print(f"\nNenhuma consulta ativa marcada para o(a) doutor(a) {medico_crm}")
        print('-' * 107)
    else:
        print('-' * 107)
    
    input("\nPressione [ENTER para voltar]")

def listar_consultas_por_periodo():
    os.system("cls" if os.name == "nt" else "clear")
    print("[CONSULTAS POR PERÍODO]\n")

    # Coletar data inicial
    inicio_valido = False
    while not inicio_valido:
        data_inicio_str = input("Insira a data inicial (DD/MM/AAAA): ")
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
            inicio_valido = True
        except ValueError:
            print("Erro: Formato de data inválido ou data inexistente.")

    # Coletar data final
    fim_valido = False
    while not fim_valido:
        data_fim_str = input("Insira a data final (DD/MM/AAAA): ")
        try:
            data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y").date()
            if data_fim >= data_inicio:
                fim_valido = True
            else:
                print("Erro: A data final não pode ser anterior à data inicial.")
        except ValueError:
            print("Erro: Formato de data inválido ou data inexistente.")

    print(f"\nConsultas agendadas entre {data_inicio_str} e {data_fim_str}:\n")
    print('-' * 107)
    print(f"| {'CÓDIGO':<10} | {'DIA':<14} | {'HORÁRIO':<12} | {'PACIENTE':<28} | {'MÉDICO':<28}|")
    print('-' * 107)

    encontrou_consulta = False
    for codigo, dados in consultas.items():
        if dados[4] == True:
            try:
                data_consulta = datetime.strptime(dados[0], "%d/%m/%Y").date()
                
                if data_inicio <= data_consulta <= data_fim:
                    print(f"| {codigo:<10} | {dados[0]:<14} | {dados[1]:<12} | {dados[2]:<28} | {dados[3]:<28}|")
                    encontrou_consulta = True
            except ValueError:
                continue

    if not encontrou_consulta:
        print(f"| Nenhuma consulta encontrada neste período.{' '*63}|")
        print('-' * 107)
    else:
        print('-' * 107)

    input("\nPressione [ENTER] para voltar")
