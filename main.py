import os
from pacientes import *
from medicos import *
from consultas import *


carregar_pacientes()
carregar_medicos()
carregar_consultas()


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
        cadastrar_paciente()

    elif opc_paciente == '2':
        buscar_paciente()

    elif opc_paciente == '3':
        atualizar_paciente()

    elif opc_paciente == '4':
        excluir_paciente()

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
        cadastrar_medico()

    elif opc_medico == '2':
        buscar_medico()

    elif opc_medico == '3':
        atualizar_medico()

    elif opc_medico == '4':
        excluir_medico()

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
        cadastrar_consulta()

    elif opc_consulta == '2':
        buscar_consulta()

    elif opc_consulta == '3':
        atualizar_consulta()

    elif opc_consulta == '4':
        excluir_consulta()

  elif opc == '4':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===================================================+
| [RELATÓRIOS]                                      |
|                                                   |
| [1] Listar todos os Pacientes                     |
| [2] Listar todos os Médicos                       |
| [3] Listar todas as Consultas                     |
| [4] Listar Consultas por Pacientes                |
| [5] Listar Consultas por Médicos                  |
| [0] Voltar ao Menu Principal                      |
|                                                   |
+===================================================+
""")
    opc_relatorio = input("Qual seção deseja acessar? ")

    if opc_relatorio == '1':
        listar_pacientes()
    
    elif opc_relatorio == '2':
        listar_medicos()

    elif opc_relatorio == '3':
        listar_consultas()

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


salvar_pacientes()
salvar_medicos()
salvar_consultas()
