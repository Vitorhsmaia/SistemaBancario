
usuarios = []
contas = []
numero_conta_sequencial = 1
AGENCIA = "0001"


def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado com esse CPF.")
            return

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")


def criar_conta_corrente(cpf):
    global numero_conta_sequencial

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    nova_conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta_sequencial,
        "usuario": usuario_encontrado,
        "saldo": 0,
        "extrato": ""
    }
    contas.append(nova_conta)
    numero_conta_sequencial += 1
    print(f"Conta criada com sucesso! Número da conta: {nova_conta['numero_conta']}")


def depositar(valor, /, conta):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(*, valor, conta, limite, numero_saques, limite_saques):
    if valor > conta["saldo"]:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")
    return numero_saques


def exibir_extrato(conta, /, *, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def encontrar_conta_por_cpf(cpf):
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            return conta
    print("Conta não encontrada.")
    return None


def listar_contas():
    if contas:
        print("\n========= LISTA DE CONTAS =========")
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {usuario['nome']} (CPF: {usuario['cpf']})")
        print("===================================")
    else:
        print("Nenhuma conta cadastrada.")


menu = """
[n] Novo Usuário
[c] Nova Conta
[l] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

numero_saques = 0
LIMITE_SAQUES = 3
limite = 500

while True:
    opcao = input(menu)

    if opcao == "n":
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (Logradouro, número - Bairro - Cidade/UF): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta_corrente(cpf)

    elif opcao == "l":
        listar_contas()

    elif opcao == "d":
        cpf = input("Informe o CPF do titular da conta: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor, conta)

    elif opcao == "s":
        cpf = input("Informe o CPF do titular da conta: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            numero_saques = sacar(valor=valor, conta=conta, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        cpf = input("Informe o CPF do titular da conta: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            exibir_extrato(conta, saldo=conta["saldo"])

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente.")
