# variables
cadastro = {'nome':[], 'sexo':[], 'ano':[]}
cadastros = 0
total_age = 0
women_under_30 = 0
men_under_30 = 0

#function to get the people under thiry years old
def male_or_female_under_thirty(cadastro):
    global men_under_30, women_under_30
    for i in range(len(cadastro['sexo'])):
        gender = cadastro['sexo'][i]
        age = 2024 - cadastro['ano'][i]
        if (gender == 'M' and age < 30):
            men_under_30 += 1
        elif (gender == 'F' and age < 30):
            women_under_30 += 1

# function to get the sum of all ages
def get_age(cadastro):
    global total_age
    for birth_year in cadastro['ano']:
        total_age += 2024 - birth_year   

# MAIN PROGRAM
while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NAO')
        continue
    
    nome = input('Qual o nome? ')
    while True: # make sure it's a valid sexo
        sexo = input("Qual o sexo? ")
        if (sexo.lower() in 'fm'):
            break
        else: 
            print("Qual o sexo. (F - Feminino/M - Masculino)")
    ano = int(input("Qual o ano do nascimento? "))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)
    cadastros += 1
    
male_or_female_under_thirty(cadastro) # Function to find the women and men younger than thirty
get_age(cadastro) #Function to find the average age of the people cadastradas

print(cadastro) # number of people cadastradas
print(f"Numero de pessoas cadastrados: {cadastros}")
print(f'Numero de Mulheres com menos de 30 anos: {women_under_30}')
print(f'Numero de Homens com menos de 30 anos: {men_under_30}')

if cadastros > 0: # prevent division by zero
    average_age = total_age / cadastros # Get the average age of the people cadastradas
    print(f"Idade media das pessoas: {average_age}")
else: 
    print("Ninguem foi cadastrada.")