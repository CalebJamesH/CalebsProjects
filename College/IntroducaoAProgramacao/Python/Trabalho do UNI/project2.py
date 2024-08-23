# VARIAVEIS GLOBAIS
totalValor = 0  # VALOR TOTAL DAS COPMRAS QUE SERA O PRINT() NO FINAL

# FAZENDO O MENU/CARDAPIO
print("------------ Bem vindos a loja do Caleb James Hall. ------------") 
print("-"*27, "Cardapio", "-"*27)
print("-"*64)
print('---|  Tamanho  | Bife Acebolado(BA)  |  File de Frango(FF)  |---')
print('---|     P     |      R$ 16.00       |       R$ 15.00       |---')
print('---|     M     |      R$ 18.00       |       R$ 17.00       |---')
print('---|     G     |      R$ 22.00       |       R$ 21.00       |---')
print("-"*64)

# COMPRANDO AS CARNES
while True: 
    
    while True:  # VERIFICAR QUE E SABOR E TAMANHO E VALIDA
        
        # VERIFICAR SABOR VALIDO
        sabor = input("Sabor desejado: (BA/FF) ")
        if sabor.upper() == "BA" or sabor.upper() == "FF":
            sabor = sabor.upper()
        else:
            print("Sabor invalido, seleciona (BA/FF)\n")
            continue

        # VERIFICAR TAMNAHO VALIDO 
        tamanho = input("Tamanho desejado: (P/M/G) ")
        if tamanho.upper() == "P" or tamanho.upper() == "M" or tamanho.upper() == "G":
            tamanho = tamanho.upper()
            break
        else:
            print("Tamanho invalido. Seleciona (P/M/G)\n")
            continue

    if sabor.upper() == 'BA':  # PRECO PARA BIFE ACEBOLADO BASEADO NO TAMANHO
        sabor = "Bife Acebolado"
        if tamanho == "P":
            totalValor += 16.00
            valorUnitario = 16.00
        elif tamanho == "M":
            totalValor += 18.00
            valorUnitario = 18.00
        else:
            totalValor += 22.00
            valorUnitario = 22.00
    else:  # PRECO PARA FILE DE FRANGO BASEADO NO TAMANHO
        sabor = "File de Frango"
        if tamanho.upper() == "P":
            totalValor += 15.00
            valorUnitario = 15.00
        elif tamanho.upper() == "M":
            totalValor += 17.00
            valorUnitario = 17.00
        else:
            totalValor += 21.00
            valorUnitario = 21.00
    
    print(f"Voce comprou {sabor} do tamanho {tamanho.upper()}: {valorUnitario}")
    
    # VER SE QUISER COMPRAR MAIS COISAS
    continuarComprando = input("\nDeseja comprar mais algo? (S/N) \n")
    if continuarComprando.upper() == "S":
        continue
    else:
        break

# O VALOR DEPOIS DAS COPMRAS
print(f"O total foi R${totalValor}")