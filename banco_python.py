
menu = """
################## Bem vindo ao Banco Python ##################

Digite um numero correspondente a operação que deseja realizar :

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_POR_SAQUE = 500
LIMITE_SAQUES_DIARIO = 3

while True:
    operacao = input(menu)

    if operacao == '1':
        valor =  float(input("Digite o valor do Depósito : ")) 
        if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\n=====>>>> Digite um valor válido. <<<<======")

    elif operacao == '2':
        valor =  float(input("Digite o valor do Saque : "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_POR_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIO

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite por saque.")

        elif excedeu_saques:
            print("Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif operacao == '3':
        print("\n-------------- Extrato --------------\n")  
        if extrato == '':
            print("\n=====>>>> Não foram realizadas operações. <<<<======")
        else :
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("\n--------------------------------------")      
            
    elif operacao == '0':
        print("********* Obrigado por usar o Banco Python. ***********\n")
        break

    else:
        print("\n=====>>>> Digite um numero válido para operação desejada. <<<<======")

