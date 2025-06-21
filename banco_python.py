
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
num_saques = 0
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

    elif operacao == '3':
        print("\n-------------- Extrato --------------")  
        if extrato == '':
            print("\n=====>>>> Não foram realizadas operações. <<<<======")
        else :
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("\n--------------------------------------")      
            
    elif operacao == '0':
        print("********* Obrigado por usar o Banco Python. ***********\n")
        break