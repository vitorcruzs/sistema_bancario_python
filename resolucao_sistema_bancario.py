menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
movimentacoes = []

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Opção escolhida: Depósito\n")
        
        deposito = float(input("Insira o valor que deseja depositar: \n"))
        
        saldo += deposito
        movimentacoes.append(f"Depósito: R$ {deposito:.2f}")
        
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso. Saldo de R$ {saldo:.2f}")
    
    elif opcao == "s":
        print("Opção escolhida: Saque\n")
        saque = float(input(f"Insira o valor para saque. Saldo disponível de {saldo:.2f}\n"))
        
        if saque > saldo or saque <= 0 and saque <= 500:
            print("Saldo insuficiente ou valor inválido para saque.")
            
        else:
            if numero_saques <= 3:
                saldo -= saque
                numero_saques += 1
                movimentacoes.append(f"Saque: R$ {saque:.2f}")
                print(f"Saque de R$ {saque:.2f} realizado com sucesso. Saldo de R$ {saldo:.2f}")
                
            else:
                print("""
                  Você atingiu o limite de 3 saques diários.
                  Por favor, aguarde 24 horas para realizar o próximo saque ou entre em contato com o seu gerente.
                  """)
    
    elif opcao == "e":
        print("Extrato")
        if not movimentacoes:
            print("Não foram realizadas movimentações")
        else:
            print(movimentacoes)
        
        print(f"O seu saldo bancário é de R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("Atendimento finalizado. Até logo!")
        break
    
    else:
        print("Opção inválida. Insira novamente a opção desejada.")