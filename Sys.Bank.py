def criar_usuario():         
    usuario = {
        "nome": input("Digite seu nome: "),
        "data_nascimento": input("Digite sua data de nascimento: "),
        "cpf": input("Digite seu CPF: "),
        "endereco": {
            "logradouro": input("Digite seu logradouro: "),
            "numero": input("Digite o número da casa: "),
            "bairro": input("Digite seu bairro: "),
            "cidade_estado": input("Digite sua cidade/estado: ")
        }
    }
    return usuario
def filtro(lista_usuarios,usuario):
    primeira_lista = []
    for valores in lista_usuarios:
        cpf = valores['cpf']
        primeira_lista.append(cpf)
    if usuario['cpf'] in primeira_lista:
        print("Usuário já cadastrado!")
    else:
        lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    return lista_usuarios
def criar_conta(lista_usuarios,AGENCIA, numero_conta):
    seu_usuario = input("Digite seu cpf: ")
    lista_cpfs = []     
    for i in lista_usuarios:
        cpf = i["cpf"]
        lista_cpfs.append(cpf)
    if seu_usuario in lista_cpfs:
        print("conta cadastrada com sucesso!")  
        return {"agencia": AGENCIA, "numero": numero_conta, "usuario": seu_usuario} 
    print("Usuário não encontrado!")
    return None
def deposito(saldo,valor, extrato):            
    valor = float(input("Valor do depóstio: "))
    if valor > 0:
        saldo += valor
        extrato += f"Sucesso, valor depositado: R$ {valor:.2f}\n"
    else:
        print("Depóstio inválido!")
    return saldo, extrato        
def saque(*, saldo,valor,extrato,limite,numero_saques,limite_saques):
    valor = float(input("Valor de saque: "))
    saldo_excedido = valor > saldo
    limite_execedido = valor > limite
    saques_execedidos = numero_saques > limite_saques
    quantidade_saques = numero_saques
    if saldo_excedido:
        print("Falha! Não possui saldo suficiente")
    elif limite_execedido:
        print("Falha! Limite excedido")
    elif saques_execedidos:
        print("Você não possui mais saques a disponibilidade.")
    elif valor > 0:
        saldo -= valor 
        quantidade_saques += 1
        extrato += f"Sucesso, valor sacado: R$ {valor:.2f}\n"
    else:
        print("Saque inválido!")          
    return saldo, extrato, quantidade_saques
def historico(saldo, /, extrato):
    print("\n==========EXTRATO==========")
    print("Nenhuma movimentação registrada." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n===========================")
    return saldo, extrato
    
def main():

    hud = "[d] Depositar [s] Sacar [e] Extrato [p] Sair [x] Criar usuário [y] Criar conta\n"
    saldo = 0
    valor = 0
    limite = 500
    extrato = ""
    quantidade_saques = 1
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    lista_usuarios = []
    lista_contas = []
    numero_conta = len(lista_contas) + 1    

    while(True):

        operacao = input(hud)

        if operacao == "x":
            usuario = criar_usuario()
            lista_usuarios = filtro(lista_usuarios,usuario)

        elif operacao == "y":
            conta = criar_conta(lista_usuarios,AGENCIA, numero_conta)
            if conta:
                lista_contas.append(conta)
                  
        elif operacao == "d":

            saldo, extrato = deposito(saldo,valor, extrato)

        elif operacao == "s":
            
            saldo, extrato, quantidade_saques = saque(saldo=saldo, valor=valor, extrato = extrato, limite=limite, numero_saques=quantidade_saques, limite_saques=LIMITE_SAQUES)

        elif operacao == "e":

            saldo, extrato = historico(saldo, extrato= extrato)

        elif operacao == "p":
            
            break
        
        else:
            print("Falha")
main()
