import time
import os


def sacar(saldo, numero_saques):
    valor_saque = float(input("Valor a sacar: ").replace(',','.'))
    if (saldo - valor_saque < 0):
        print("Não é possível sacar esse valor, saldo insuficiente")
        return (saldo, numero_saques, 0)
    elif(valor_saque > 500):
        print("O limite máximo por saque é de R$500,00")
        return (saldo, numero_saques, 0)
    elif(valor_saque < 0):
        print("Valor inválido")
        return (saldo, numero_saques, 0)
    else:
        saldo -= valor_saque
        numero_saques += 1
        print(f"Valor retirado: R${valor_saque:.2f}")
        print(f"Saldo atual: {saldo:.2f}")
        print()
        return (saldo, numero_saques, valor_saque)




def depositar(saldo):
    valor_deposito = float(input("Valor a depositar: ").replace(',','.')) # converte imputs (padrão string) para int 
    if(valor_deposito < 0 ):
        print("Valor inválido")
        return (saldo, 0)
    else:
        saldo += valor_deposito
        print(f"Valor depositado: R${valor_deposito:.2f} ")
        print(f"Saldo atual: R${saldo:.2f}") 
        print()
        return (saldo, valor_deposito)




def extrato(saldo, operacoes): 
    print(f"Saldo atual: {saldo}")
    print()
    print("HISTORICO:")
    print(operacoes)
    print()



saldo = 0
numero_saques = 0
operacoes = ''

while(1):

    print("Operação desejada:")
    print("S - Saque")
    print("D - Depósito")
    print("E - Extrato")
    print("X - Sair")
    operacao = input()
    operacao = operacao.upper() #converte para caixa alta


    if (operacao == 'S'):
        if(numero_saques >= 3):
            print("Limite diário de saques atingido")
        else:
            valor = 0
            saldo, numero_saques, valor = sacar(saldo, numero_saques)
            print(f"Numero de saques diários: {numero_saques}")
            hora = time.asctime()
            if(valor != 0):
                resultado = ("Operação: SAQUE" + " Valor: R$" + str(valor) + " Data: " + str(hora))
                print(resultado)
                print()
                operacoes = operacoes + resultado + os.linesep

    elif(operacao == 'D'):
      saldo, valor = depositar(saldo)
      
      if(valor != 0):
        hora = time.asctime()
        resultado = ("Operação: DEPÓSITO" + " Valor: R$" + str(valor) + " Data: " + str(hora))
        print(resultado)
        print()
        operacoes = operacoes + resultado + os.linesep

    elif(operacao == 'E'):
        if(operacoes == ''):
            print("Não foram realizadas movimentações")
            print()
        else:
            extrato(saldo, operacoes) 



    elif(operacao == 'X'):
        exit() #fecha aplicação
    else:
        print("Operação inválida!")


