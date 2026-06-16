# PyMedical [V7]

import os

os.makedirs("database", exist_ok=True)
arq_pacientes = open("database/pacientes.txt", "wt")
arq_medicos = open("database/medicos.txt", "wt")
arq_consultas = open("database/consultas.txt", "wt")

pacientes = {
  # EMAIL: [Nome, Idade, Sexo, Telefone]
  "michaelkyle@email.com" : ["Michael Kyle", 35, 'M', "(84) 9 1111-1111"],
  "jaykyle@email.com" : ["Janet Kyle", 35, 'F', "(84) 9 2222-2222"],
  "kylejr@email.com" : ["Michael Kyle Jr.", 18, 'M', "(84) 9 3333-3333"],
  "clairekyle@email.com" : ["Claire Kyle", 16, 'F', "(84) 9 4444-4444"],
  "kadykyle@email.com" : ["Kady Kyle", 6, 'F', "(84) 9 5555-5555"]
}

medicos = {
  # CRM: [Nome, Email, Especialização, Idade, Sexo, Telefone]
  "1111111" : ["Tony Honesto Jefferson", "tonyhonesto@email.com", "especial", 15, 'M', "(84) 9 1111-1111"],
  "2222222" : ["Vanessa Scott", "vanessascott@email.com", "especial", 18, 'F', "(84) 9 2222-2222"],
  "3333333" : ["Calvin Scott", "calvinscott@email.com", "especial", 35, 'M', "(84) 9 3333-3333"],
  "4444444" : ["Jasmine Scott", "jasminescott@email.com", "especial", 35, 'F', "(84) 9 4444-4444"],
  "5555555" : ["Franklin Mumford", "franklinmumford@email.com", "especial", 6, 'M', "(84) 9 5555-5555"]
}

consultas = {
  # CÓDIGO: [Dia, Horário, Paciente(email), Médico(CRM)]
  "111" : ["segunda-feira", "7:00", "kylejr@email.com", "2222222"],
  "222" : ["terca-feira", "7:00", "michaelkyle@email.com", "3333333"],
  "333" : ["quarta-feira", "7:00", "jaykyle@email.com", "2222222"],
  "444" : ["quinta-feira", "7:00", "kadyklye@email.com", "5555555"],
  "555" : ["sexta-feira", "7:00", "clairekyle@email.com", "1111111"]
}

opc = ''

while opc != '0':
  os.system("cls" if os.name == "nt" else "clear")
  
  print("""+======================================+
| [PyMedical]                          |
|                                      |
| [1] Pacientes                        |
| [2] Médicos                          |
| [3] Consultas                        |
| [4] Relatório                        |
| [5] Sobre o Sistema                  |
| [0] Sair                             |
|                                      |
+======================================+
""")

  opc = input("Qual seção deseja acessar? ")

  if opc == '0':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+=================================================+
|                                                 |
| Programa encerrado com sucesso.                 |
| Obrigado por utilizar nossos serviços! :)       |
|                                                 |
+=================================================+
""")

  elif opc == '1':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [PACIENTES]                                       |
|                                                   |
| [1] Cadastrar novo Paciente                       |
| [2] Ver dados de um Paciente                      |
| [3] Alterar dados de um Paciente                  |
| [4] Excluir um Paciente                           |
| [0] Voltar ao Menu Principal                      |
|                                                   |
+===================================================+
""")
    opc_paciente = input("Qual seção deseja acessar? ")

    if opc_paciente == '1':
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

    elif opc_paciente == '2':
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

    elif opc_paciente == '3':
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

    elif opc_paciente == '4':
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

  elif opc == '2':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [MÉDICOS]                                         |
|                                                   |
| [1] Cadastrar novo Médico                         |
| [2] Ver dados de um Médico                        |
| [3] Alterar dados de um Médico                    |
| [4] Excluir um Médico                             |
| [0] Voltar ao Menu Principal                      |
|                                                   |
+===================================================+
""")
    opc_medico = input("Qual seção deseja acessar? ")

    if opc_medico == '1':
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

    elif opc_medico == '2':
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


    elif opc_medico == '3':
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

    elif opc_medico == '4':
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

  elif opc == '3':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [CONSULTAS]                                       |
|                                                   |
| [1] Cadastrar uma nova Consulta                   |
| [2] Ver dados de uma Consulta                     |
| [3] Alterar dados de uma Consulta                 |
| [4] Excluir uma Consulta                          |
| [0] Voltar ao Menu Principal                      |
|                                                   |
+===================================================+
""")
    opc_consulta = input("Qual seção deseja acessar? ")

    if opc_consulta == '1':
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

    elif opc_consulta == '2':
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

    elif opc_consulta == '3':
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

    elif opc_consulta == '4':
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

  elif opc == '4':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [RELATÓRIOS]                                      |
|                                                   |
| [1] Listar todos os Pacientes                     |
| [2] Listar todos os Médicos                       |
| [3] Listar todas as Consultas                     |
| [4] Listar Consultas por Pacientes                |
| [5] Listar Pacientes por Médicos                  |
| [0] Voltar ao Menu Principal                      |
|                                                   |
+===================================================+
""")
    opc_relatorio = input("Qual seção deseja acessar? ")

    os.system("cls" if os.name == "nt" else "clear")
    print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '5':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [SOBRE O SISTEMA]                                 |
|                                                   |
| Sistema de gestão para clínicas médicas.          |
|                                                   |
| Equipe de Desenvolvimento:                        |
| x Rafael Araújo @rafael-araujo1                   |
|                                                   |
| Licença: GNU GPLv3                                |
| www.gnu.org/licenses/gpl.html                     |
|                                                   |
+===================================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  else:
    os.system("cls" if os.name == "nt" else "clear")
    print("""+========================================================+
|                                                        |
| [ERRO]                                                 |
| Opção Inválida! Por favor, insira uma opção válida     |
|                                                        |
+========================================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")


for email in pacientes:
  nome = pacientes[email][0]
  idade = pacientes[email][1]
  sexo = pacientes[email][2]
  telefone = pacientes[email][3]
  arq_pacientes.write(f"{email}, {nome}, {idade}, {sexo}, {telefone}\n")
arq_pacientes.close()

for crm in medicos:
  nome = medicos[crm][0]
  email = medicos[crm][1]
  especializacao = medicos[crm][2]
  idade = medicos[crm][3]
  sexo = medicos[crm][4]
  telefone = medicos[crm][5]
  arq_medicos.write(f"{crm}, {nome}, {email}, {especializacao}, {idade}, {sexo}, {telefone}\n")
arq_medicos.close()


for codigo in consultas:
  dia = consultas[codigo][0]
  horario = consultas[codigo][1]
  paciente = consultas[codigo][2]
  medico = consultas[codigo][3]
  arq_consultas.write(f"{codigo}, {dia}, {horario}, {paciente}, {medico}\n")
arq_consultas.close()
