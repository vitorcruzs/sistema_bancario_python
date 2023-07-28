import textwrap

def menu():
    menu = """\n
          ============= MENU =============
          [d]\tDepositar
          [s]\tSacar
          [e]\tExtrato
          [nu]\tNovo Usuário
          [nc]\tNova conta
          [lc]\tListar contas
          [q]\tSair
          => """
    return input(textwrap.dedent(menu))

def exibir_extrato(saldo, /, *, extrato):
    print("\n----------EXTRATO----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"O seu saldo bancário é de R$ {saldo:.2f}")
    print("=============================")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
       saldo += valor
       extrato += f"Depósito: R$ {valor:.2f}"
       print("=== Depósito de R$ realizado com sucesso. ===")
       
    else:
       print("@@@ Operação falhou. Valor inválido. @@@ ")
       
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    float(input(f"Insira o valor para saque. Saldo disponível de {saldo:.2f}\n"))
    
    if excedeu_saldo:
        print("Saldo insuficiente.")
        
    elif excedeu_limite:
        print("Valor muito alto para a operação.")
        
    elif excedeu_saques:
        print("Você atingiu o limite de saques diários.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"=== Saque realizado com sucesso! ===")
        
    else:
        print("@@@ Operação falhou. Valor inválido. @@@")
        
    return saldo, extrato

def criar_usuarios(usuarios):
    cpf = input("Informe o CPF(somente o número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe um usuário com este cpf. @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=== Usuário criado com sucesso ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n @@@ Usuário não encontrado. Cadastro de conta encerrado. @@@")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("Informe o valor de depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input("Informe o valor para saque."))
            
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato,
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao =='nu':
            criar_usuarios(usuarios)
            
        elif opcao =='nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == "q":
            
            print("Atendimento finalizado. Até logo!")
            break
        
        else:
            print("Opção inválida. Insira novamente a opção desejada.")       

main()