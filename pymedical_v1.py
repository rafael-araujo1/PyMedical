# PyMedical [V1]

import os

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
    print("""+==============================================+
| Boas-Vindas à Seção [PACIENTES]              |
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '2':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+==============================================+
| Boas-Vindas à Seção [MÉDICOS]                |
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '3':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+==============================================+
| Boas-Vindas à Seção [CONSULTAS]              |
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '4':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+===============================================+
| Boas-Vindas à Seção [RELATÓRIOS]              |
|                                               |
| x Esta seção ainda não foi finalizada.        |
|                                               |
+==============================================+
""")
    input("Pressione [ENTER] para voltar ao menu principal... ")

  elif opc == '5':
    os.system("cls" if os.name == "nt" else "clear")
    print("""+==============================================+
| [SOBRE O SISTEMA]                            |
|                                              |
| x Esta seção ainda não foi finalizada.       |
|                                              |
+==============================================+
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
