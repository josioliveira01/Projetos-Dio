def depositar(usuarios, usuario_id):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        usuarios[usuario_id]['saldo'] += valor
        usuarios[usuario_id]['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        print(f"Saldo Atualizado: R$ {usuarios[usuario_id]['saldo']:.2f}")
    else:
        print("Valor inválido para depósito.")

def sacar(usuarios, usuario_id):
    valor = float(input("Informe o valor do saque: "))
    if valor > 0 and valor <= usuarios[usuario_id]['saldo']:
        usuarios[usuario_id]['saldo'] -= valor
        usuarios[usuario_id]['extrato'] += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
        print(f"Saldo Atualizado: R$ {usuarios[usuario_id]['saldo']:.2f}")
    else:
        print("Saldo insuficiente para saque.")

def mostrar_extrato(usuarios, usuario_id):
    print("\n================ EXTRATO DAS TRANSAÇÕES ================")
    print(usuarios[usuario_id]['extrato'] or "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {usuarios[usuario_id]['saldo']:.2f}")
    print("=======================================================")

def nova_conta(usuarios):
    usuario_id = input("Informe o CPF do usuário: ")
    if usuario_id in usuarios:
        print("Este CPF já possui uma conta.")
    else:
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço: ")
        usuarios[usuario_id] = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'saldo': 0.0,
            'extrato': ""
        }
        print("Nova conta criada com sucesso!")

def listar_contas(usuarios):
    print("\nLista de todas as contas:")
    for usuario_id, info in usuarios.items():
        print(f"CPF: {usuario_id}, Nome: {info['nome']}, Saldo: R$ {info['saldo']:.2f}")

def novo_usuario(usuarios):
    usuario_id = input("Informe o CPF para o novo usuário: ")
    if usuario_id in usuarios:
        print("Este CPF já está registrado no sistema.")
    else:
        nome = input("Informe o nome completo do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço: ")
        usuarios[usuario_id] = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'saldo': 0.0,
            'extrato': ""
        }
        print("Novo usuário registrado com sucesso!")

def executar_sistema_bancario():
    usuarios = {}
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Sair

    Escolha uma opção: """

    while True:
        opcao = input(menu)
        if opcao == "1" or opcao == "2" or opcao == "3":
            usuario_id = input("Informe o CPF do usuário: ")
            if usuario_id not in usuarios:
                print("CPF não encontrado.")
                continue

        if opcao == "1":
            depositar(usuarios, usuario_id)
        elif opcao == "2":
            sacar(usuarios, usuario_id)
        elif opcao == "3":
            mostrar_extrato(usuarios, usuario_id)
        elif opcao == "4":
            nova_conta(usuarios)
        elif opcao == "5":
            listar_contas(usuarios)
        elif opcao == "6":
            novo_usuario(usuarios)
        elif opcao == "7":
            print("Obrigado por usar o nosso sistema.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Para iniciar o sistema
executar_sistema_bancario()

