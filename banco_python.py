import textwrap

def menu():

    menu = """
    ###############################################################
    #                Bem vindo ao Banco Python                    #
    ###############################################################

    Digite um numero correspondente a operação que deseja realizar:

    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
    
    """
    return input(textwrap.dedent(menu))


def depositar(saldo, extrato):

    v =  input("Digite o valor do Depósito : ")
    
    if v.isdigit(): # testa se o input é um numero
        valor = float(v) # converte para float

        if valor > 0 :            
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            # 1;32 : exibir texto em negrito e verde
            print(f"\n\033[1;32m****** Deposito de R$ {valor:.2f} realizado com sucesso. ********\033[m\n")      
        
    else:
        # 1;31 : exibir texto em negrito e vermelho
        print("\n\033[1;31m=====>>>> Digite um valor válido. <<<<======\033[m")

    return saldo, extrato
    
    
def sacar(saldo, extrato, numero_saques):
    
    LIMITE_POR_SAQUE = 500
    LIMITE_SAQUES_DIARIO = 3

    valor =  float(input("Digite o valor do Saque : "))
            
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_POR_SAQUE
    excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIO

    # 1;31 : exibir texto em negrito e vermelho
    if excedeu_saldo:
        print("\033[1;31mVocê não tem saldo suficiente.\033[m")
        
    elif excedeu_limite:
        print("\033[1;31mO valor do saque excede o limite por saque.\033[m")

    elif excedeu_saques:
        print("\033[1;31mNúmero máximo de saques diários excedido.\033[m")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        # 1;32 : exibir texto em negrito e verde
        print(f"\n\033[1;32m******* Saque de R$ {valor:.2f} realizado com sucesso. ********\033[m\n")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    # 1;33 : exibir texto em negrito e amarelo
    print("\n\033[1;33m-------------- Extrato --------------\033[m\n")  
    if extrato == '':
        print("\n\033[1;33m=====>>>> Não foram realizadas operações. <<<<======\033[m")
    else :
        print(f"\033[1;33m{extrato}\033[m")
    print(f"\n\033[1;33mSaldo: R$ {saldo:.2f}\033[m") 
    print("\n\033[1;33m--------------------------------------\033[m")

def encerrar():
    print("\033[1;32m********* Obrigado por usar o Banco Python. ***********\033[m\n")


def erro():
    # "\033[0;30;41m mensagem \033[m" fundo vermelho e letra branca 
    print("\n\033[1;30;41m===>>>> Digite um numero válido para operação desejada. <<<<===\033[m")
    
   

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0    

    while True:
        operacao = menu()

        if operacao == '1':
            saldo, extrato = depositar(saldo, extrato)

        elif operacao == '2':
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)            

        elif operacao == '3':
            exibir_extrato(saldo, extrato)      
                
        elif operacao == '0':
            encerrar()
            break

        else:
            erro()


main()