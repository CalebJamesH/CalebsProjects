# =============================== IMPORTS ==================================
from pprint import pprint
# ============================== VARIAVEIS =================================
listar_funcionarios = []
id_global = 5016927

# =============================== FUNCOES ==================================
# funcao para cadastra um funcionario
def cadastrar_funcionario(id):
    print("---------- MENU DE CADASTRAR FUNCIONARIOS ---------")
    print(f"Id do funcionario: {id}")
    nome = input("Nome do funcionario: ")  
    setor = input("Nome do setor: ")
    while True:
        # try para confirmar que seja um input valido
        try:
            salario = float(input("Salario do funcionario: "))
            break
        except ValueError:
            print("Error. Try again")

    # Colocando os dados dentro de um Dicionario 
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    # Colocando um dicionario dentro de uma lista, EXIGENCIA 7??
    listar_funcionarios.append(funcionario.copy())
       
def consultar_funcionarios():
    print("------------- CONSULATR FUNCIONARIOS -------------")
    while True:
        # try para confirmar que seja um input valido
        try:
            option = int(input("Qual opção deseja?\n - 1. Consultar Todos\n - 2. Consultar por Id\n - 3. Consultar por Setor\n - 4. Retornar ao menu\n >> "))
            if option in (1, 2, 3, 4):
                
                # CONSULTAR TODOS  
                if option == 1:
                    pprint(listar_funcionarios)
                
                # CONSULTAR POR ID
                elif option == 2:
                    while True:
                        # try para confirmar que seja um ID valido
                        try:
                            funcionario_id = int(input("Entre o ID do funcionario: "))
                            found = False
                            # loop para ver se o ID exisite
                            for funcionario in listar_funcionarios:
                                if funcionario["id"] == funcionario_id:
                                    pprint(funcionario)
                                    found = True
                                    break
                                
                            # Caso ID nao existe vai informar.
                            if not found: 
                                print("Id doesn't exists. Try a different one.")
                            # Caso existe vai sair do loop
                            else:
                                break
                        except ValueError:
                            print("Id invalida, tenta de novo.")
                        
                         
                # CONSULTAR POR SETOR   
                elif option == 3:
                    while True:
                        try:
                            funcionario_setor = input("Entre o setor do funcionário: ")
                            found = False
                            # Loop through the list to find all employees in the specified sector
                            for funcionario in listar_funcionarios:
                                if funcionario["setor"] == funcionario_setor:
                                    pprint(funcionario)
                                    found = True
                            
                            # If no employees are found in the sector, inform the user
                            if not found:
                                print("Setor não existe. Tente de novo.")
                            else:
                                break  # Exit the loop after printing all employees in the sector
                                
                        except ValueError:
                            print("Setor inválido, tente de novo.")


                # sair da da funcao
                elif option == 4:
                    return
            else: 
                print("Not a valid option.")
        except ValueError:
            print("opcao invalida, tenta de novo.")

def remover_funcionario():
    print("--------------- REMOVER FUNCIONARIO --------------")
    while True:
        # try para confirmar que seja um input valido
        try:
            funcionario_id = int(input("Digite o ID do funcionario que deseja excluir: "))
            # loop para encontrar o funcionario com o mesmo id
            for funcionario in listar_funcionarios:
                # se o funcionario com o ID existe sera removido.
                if funcionario["id"] == funcionario_id:
                    listar_funcionarios.remove(funcionario)
                    print(f"Funcionario com id {funcionario_id} foi removido.")
                    # sair da funcao
                    return
            # caso nao existe, vai pedir pra fazer novamente
            print("Id invalido. Tente novamente")
        # caso nao existe, vai pedir pra fazer novemente
        except ValueError:
            print("Id invalido. Tente novamente.")



# ========================== PROGRAMA PRINCIPAL ============================
print("Bem vindos a empresa do Caleb Hall!")
print("-----------------------------------")


while True:
    print("=========== MENU PRINCIPAL =========")
    # try pra confirmar que seja input valido
    try:
        option = int(input("Qual opção deseja\n - 1. Cadastrar Funcionário\n - 2. Consultar Funcionário\n - 3. Remover Funcionário\n - 4. Encerrar Programa\n >>"))
        if option == 1:
            # chamar funcao
            id_global += 1
            cadastrar_funcionario(id_global)
        elif option == 2:
            # chamar funcao
            consultar_funcionarios()
        elif option == 3:
            # chamar funcao
            remover_funcionario()
        else:
            # sair
            break
            
    except ValueError:
        print("Invalid option. Try again.")