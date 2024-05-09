menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opçao= input(menu)
    
    if opçao == "1":
       valor = float(input("informe o valor do depósito: "))
       
       if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        print(f"\nSaldo Atualizado: R$ {saldo:.2f}")

       else:
        print("Operação falhou! O valor informado é inválido.")
     
    elif opçao == "2":
      valor = float(input("Informe o valor do saque: "))
      
      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= LIMITE_SAQUES
      
      if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")
        
      elif excedeu_limite:
        print("Operação falhou! Valor excede o limite de saque de R$500.")
      
      elif excedeu_saques:
        print("Operação falhou! Limite de saques diários atingido.")
      
      elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            print(f"\nSaldo Atualizado: R$ {saldo:.2f}")

      else:
            print("Operação falhou! O valor informado é inválido.")

    elif opçao == "3":
        print("\n================ EXTRATO DAS TRANSAÇÕES ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")      

    elif opçao == "4":
        print("Obrigado por usar o nosso sistema.")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    
