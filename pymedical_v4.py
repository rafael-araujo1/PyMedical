# PyMedical [V4]

from os import system

opc = ''

while opc != '0':
  system("clear")
  # No Windows: system("cls") 

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
    system("clear")
    print("""+=================================================+
|                                                 |
| Programa encerrado com sucesso.                 |
| Obrigado por utilizar nossos serviços! :)       |
|                                                 |
+=================================================+
""")
    
  elif opc == '1':
    system("clear")
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
      system("clear")
      print("[CADASTRAR PACIENTE]\n")
      paciente_nome = input("Insira o nome do paciente: ")
      paciente_email = input("Insira o email do paciente: ")
      paciente_idade = input("Insira a idade do paciente: ")
      paciente_sexo = input("Insira o sexo do paciente: ")
      paciente_telefone = input("Insira o telefone do paciente: ")

      print("""
+==============================================+
|                                              |
| x Paciente cadastrado com sucesso            |
|                                              |
+==============================================+
""")
      input("Aperte [ENTER] para continuar")

      system("clear")
      print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")

    elif opc_paciente == '2':
      system("clear")
      print("[BUSCAR PACIENTE]\n")
      paciente_email = input("Insira o email do paciente: ")

      system("clear")
      print(f"""x Nome: Chico Lopes
x Email: {paciente_email}
x Idade: 35
x Sexo: Masculino
x Telefone: (84) 94002-8922
      
+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")

    elif opc_paciente == '3':
      system("clear")
      print("[ALTERAR DADOS DO PACIENTE]\n")
      paciente_nome = input("Insira o nome do paciente: ")
      paciente_email = input("Insira o email do paciente: ")
      paciente_idade = input("Insira a idade do paciente: ")
      paciente_sexo = input("Insira o sexo do paciente: ")
      paciente_telefone = input("Insira o telefone do paciente: ")

      print("""
+==============================================+
|                                              |
| x Paciente alterado com sucesso              |
|                                              |
+==============================================+
""")
      input("Aperte [ENTER] para continuar")

      system("clear")
      print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")

    elif opc_paciente == '4':
      system("clear")
      print("[EXCLUIR PACIENTE]\n")
      paciente_email = input("Insira o email do paciente: ")

      print("""
+==============================================+
|                                              |
| x Paciente excluído com sucesso              |
|                                              |
+==============================================+
""")
      input("Aperte [ENTER] para continuar")

      system("clear")
      print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")

    input("Pressione [ENTER] para voltar")

  elif opc == '2':
    system("clear")
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
      system("clear")
      print("[CADASTRAR MÉDICO]\n")
      medico_nome = input("Insira o nome do médico: ")
      medico_email = input("Insira o email do médico: ")
      medico_especializacao = input("Insira a especialização do médico: ")
      medico_crm = input("Insira o CRM do médico: ")
      medico_idade = input("Insira a idade do médico: ")
      medico_sexo = input("Insira o sexo do médico: ")
      medico_telefone = input("Insira o telefone do médico: ")

      print("""
+==============================================+
|                                              |
| x Médico cadastrado com sucesso              |
|                                              |
+==============================================+
""")
      input("Aperte [ENTER] para continuar")

      system("clear")
      print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
      
    elif opc_medico == '2':
      system("clear")
      print("[BUSCAR MÉDICO]\n")
      medico_crm = input("Insira o CRM do médico: ")

      system("clear")
      print(f"""x Nome: Chico Lopes
x Email: chicolopes@gmail.com
x Especialização: Especial
x CRM: {medico_crm}
x Idade: 35
x Sexo: Masculino
x Telefone: (84) 94002-8922
      
+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")

    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '3':
    system("clear")
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
  
    system("clear")
    print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '4':
    system("clear")
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
  
    system("clear")
    print("""+==============================================+
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '5':
    system("clear")
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
    system("clear")
    print("""+========================================================+
|                                                        |
| [ERRO]                                                 |
| Opção Inválida! Por favor, insira uma opção válida     |
|                                                        |
+========================================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")
