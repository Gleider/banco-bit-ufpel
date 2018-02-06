import clientes
#import transacoes

def menuPrincipal():
    while True:
        print('\n')
        titulo = 'Banco bitUfpel'
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        print("[1] - Criar Banco de Dados (caso não exista)\n[2] - Cadastrar Nova Conta\n[3] - Logar\n[4] - Sair")
        op = input("Opção: ")
        if op.isdigit():
            if int(op) == 4:
                break
            elif int(op) == 1:
                criarBD()
                continue
            elif int(op) == 2:
                novaConta()
                continue
            elif int(op) == 3:
                consultarSenha()
                continue
            '''
            elif int(op) == 3:
                transacao()
                continue
            '''
        print('Opção inválida\n')

def criarBD():
    clientes.criar_db()

def novaConta():
    print('\n')
    titulo = 'Cadastrar nova conta'
    print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
    clientes.menuCadastro()
    print('')

def consultarSenha():
    print('\n')
    titulo = 'Consultar senha'
    print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
    op = input("numConta: ")
    senha = str.encode(input("senha: "))
    clientes.usuario_autenticado(op, senha)
    print('')
    
'''
def transacao():
    while True:
        print('\n')
        titulo = 'Realizar Transacoes'
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        print("[1] - Saque\n[2] - Deposito\n[3] - Transferencia\n[4] - Voltar")
        op = input("Opção: ")
        if op.isdigit():
            if int(op) == 4:
                break
            elif int(op) == 1:
                numConta = int(input("Número da Conta: "))
                valorSaque = float(input("Valor de Saque: "))
                operacoes = transacoes.operacoes()
                operacoes.saque(numConta, valorSaque)
                continue
            elif int(op) == 2:
                numConta = int(input("Número da Conta: "))
                valorDeposito = float(input("Valor de Depósito: "))
                operacoes = transacoes.operacoes()
                operacoes.deposito(numConta, valorDeposito)
                continue
            elif int(op) == 3:
                numContaRem = int(input("Número da conta origem: "))
                numContaDest = int(input("Numero da conta destino: "))
                valor = float(input("Valor da Transferência: "))
                operacoes = transacoes.operacoes()
                operacoes.transferencia(numContaRem, numContaDest, valor)
                continue
            print('Opção inválida\n')
        
'''

menuPrincipal()
clientes.conectar.close()
#transacoes.conectar.close()
