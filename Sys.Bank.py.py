hud = "[d] Depositar [s] Sacar [e] Extrato [x] Sair"

d = ""
s = ""
e = ""
x = ""

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while(True):

    operacao = input(hud)

    if operacao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Sucesso, valor depositado: R$ {valor:.2f}\n"
            
        else:
            print("Deposito inválido!")
    
    elif operacao == "s":
        valor = float(input("Valor do saque: "))

        saldo_excedido = valor > saldo
        limite_execedido = valor > limite
        saques_execedidos = quantidade_saques >LIMITE_SAQUES

        if saldo_excedido:
            print("Falha! Não possui saldo suficiente")
        elif limite_execedido:
            print("Falha! Limite excedido")
        elif saques_execedidos:
            print("Você não possui mais saques a disponibilidade.")
        elif valor > 0:
            saldo += valor 
            quantidade_saques += 1
            extrato += f"Sucesso, valor sacado: R$ {valor:.2f}\n"
            
        else:
            print("Saque inválido!")

    elif operacao == "e":
        print("\n==========EXTRATO==========")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===========================")

    elif operacao == "x":
        break
    else:
        print("Falha!")