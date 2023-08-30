import os
import time
#from tabulate import tabulate
agenda = []

while True:
    print("=====LISTAS DE OPÇÃO======")
    print("NOVO CONTATO===========[1]")
    print("LISTA DE CONTATOS======[2]")
    print("EDITAR CONTATO=========[3]")
    print("EXCLUIR CONTATO========[4]")
    print("SAIR DO PROGRAMA=======[5]")
    print("==========================")
    op =  input("")
    os.system('cls')
    if op == "1":
        vet_aux = []
        nome = input("Digite o nome do novo contato: ")
        vet_aux.append(nome)
        telefone = input("Digite o telefone do contato: ")
        vet_aux.append(telefone)
        agenda.append(vet_aux)
        print("CONTATO ADICIONADO COM SUCESSO!")

    elif op == "2":
        print("LISTA DE CONTATOS")
        for contato in agenda:
            print(f'NOME: {contato[0]}\tTELEFONE: {contato[1]}')
    
    elif op == "3":
        nome = input("Qual o nome do contato que deseja editar: ")
        for i in range(len(agenda)):
            if (nome == agenda[i][0]):
                nome_novo = input("Qual o nome novo: ")
                telefone_novo = input("Qual o telefone novo: ")
                agenda[i][0] = nome_novo
                agenda[i][1] = telefone_novo
                print("CONTATO ALTERADO COM SUCESSO!")

                break
            if (i == (len(agenda) -1)):
                print("CONTATO NÃO ENCONTRADO!")
 
    elif op == "5":
        break
    else:
        print("COMANDO INVÁLIDO!!!")

    time.sleep(2)
    os.system('cls')
print("PROGRAMA FINALIZADO!")    