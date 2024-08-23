# PROGRAMA PRINCIPAL: CALCULANDO PARCELAS
print("Bem vindo a loja do Caleb James Hall!") 

# Usando loops para garantir que os dados recebidos sao validos 
while True: 
    try: 
        valorDoPedido = float(input("Qual é o valor do seu pedido? "))  # deve ser um NUMERO
        if (valorDoPedido > 0):  # NUMERO deve ser maior que zero
            break  # se for NUMERO maior que zero, break.
        else: 
            print("Tem que ser um valor maior que 0") 
    except ValueError: 
        print("Por favor, insira um número válido. (acima de 0)")  
while True:
    try:
        qtdDeParcelas = int(input("Em quantas vezes quer parcelar? "))  # deve ser um NUMERO
        if (qtdDeParcelas > 0):  # NUMERO deve ser maior que zero
            break  # se for NUMERO maior que zero, break.
        else:
            print("Por favor, insira um número válido. (acima de 0)") 
    except ValueError:
        print("Por favor, insira um número válido. (acima de 0)")

# Calculando os juros baseado no numero de parcelas
juros = 0
if (qtdDeParcelas < 4):
    juros = 1
elif (qtdDeParcelas >= 4 and qtdDeParcelas < 6):
    juros = 1.04
elif (qtdDeParcelas >= 6 and qtdDeParcelas < 9):
    juros = 1.08
elif (qtdDeParcelas >= 9 and qtdDeParcelas < 13):
    juros = 1.16
else: 
    juros = 1.32 
    
# Calculando o valor de cada parcela e o total a pagar
valorTotalParcelado = valorDoPedido * juros # total a pagar
valorDaParcela = valorTotalParcelado / qtdDeParcelas # total a pagar POR PARCELA

print(f"Valor de cada parcela:R$ {round(valorDaParcela, 2)}")
print(f"Valor total Parcelado:R$ {round(valorTotalParcelado, 2)}")


    