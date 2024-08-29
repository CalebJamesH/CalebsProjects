# FUNCOES
# ======================== PRIMEIRA FUNCAO - MODELO =========================
def escolha_modelo():
    print("Qual eh o modelo desejado?")
    print("MCS - Manga Curta Simples: R$ 1.80")
    print("MLS - Manga Longa Simples: R$ 2.10")
    print("MCE - Manga Curta Com Estampa: R$ 2.90")
    print("MLE - Manga Longa Com Estampa: R$ 3.20")
    # loop para confirmar que seja um modelo valido
    while True:
        modelo = input(">> ")
        
        # confirmar que eh um modelo valido
        if modelo.upper() in ("MCS", "MLS", "MCE", "MLE"):  
            
            # Definindo o valor do modelo
            if modelo.upper() == "MCS":  
                valor_modelo = 1.80
            elif modelo.upper() == "MLS":
                valor_modelo = 2.10
            elif modelo.upper() == "MCE":
                valor_modelo = 2.90
            elif modelo.upper() == "MLE":
                valor_modelo = 3.20 
            break      
        
        else: 
            print("Seleciona um modelo valido.\n")
            
    # retornar o valor do modelo
    return valor_modelo 


# =================== SEGUNDA FUNCAO - NUMERO DE CAMISAS ====================
def num_camiseta():
    # Loop para confirmar que seja um numero valido
    while True:
        
        # Try o numero de camisetas, deve ser entre 0 e 20,000
        try: 
            camisetas = int(input("Entre com o numero de camisetas (0-20,000): "))

            # if para confirmar o valor esta certo
            if camisetas > 0 and camisetas <= 20000:  

                # if para calcular desconto baseado no numero de camisas compradas
                if camisetas < 20:  
                    camisetas *= 1
                elif camisetas >= 20 and camisetas < 200:
                    camisetas *= 0.95
                elif camisetas >= 200 and camisetas < 2000:
                    camisetas *= 0.93
                elif camisetas >= 2000 and camisetas <= 20000:
                    camisetas *= 0.88
                break
            
            else: 
                print("Entrar com numero valido.\n")
                
        # pegar o error caso for error valor
        except ValueError:   
            print("Precisa Entrar com numero. \n ")
            
    # retornar o numero de camisas COM DESCONTO
    return camisetas  


# ======================== TERCEIRA FUNCAO - FRETE ========================
def escolha_frete():
    print("Escolha o tipo de frete:")
    print("0 - Retirar na fabrica - R$ 0.00")
    print("1 - Frete por transportadora - R$ 100.00")
    print("2 - Frete por Sedex - R$ 200.00")
    # Loop para confirmar que seja um frete valido
    while True:
        
        # Try o valor do input, deve ser entre 0 e 2
        try:
            frete = int(input(">> "))
            
            # calcular o valor do frete beseado no input 'frete'
            if frete in (0, 1, 2):
                if frete == 0:
                    valor_frete = 0.00
                elif frete == 1:
                    valor_frete = 100.00
                else:
                    valor_frete = 200.00
                break
            else: 
                print("Escolha um tipo valido.\n")
        
        # pegar o error case for error valor
        except ValueError:
            print("Escolha um tipo valido.\n")
    return valor_frete

        
#=========================== PROGRAMA PRINCIPAL =============================
print("Bem vindos a Fabrica de Camisas do Caleb Hall!")

# Chamando as funcoes e colocando os valores retornados num variavel
valor_modelo = escolha_modelo()
camisetas = num_camiseta()
frete = escolha_frete()

# calcular total
total = (valor_modelo * camisetas) + frete

# fazer print do total e mostrar o calculo de todos os valores
print(f"Valor total: {total} (Modelo: {valor_modelo} * Quantidade(com desconto): {camisetas}) + frete: {frete})")
