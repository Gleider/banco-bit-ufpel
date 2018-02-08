from tkinter import messagebox

import interfaceDeposito
import interfaceLogin
import interfaceOperacoes
import interfacePagamento
import interfaceSaldo
import interfaceSaque
import interfaceTransferencia
from testeUsuarios import *
from interfaceConfig import *


# importa as classes referente as opções do terminal e a tela de login
# programa começa aqui, ele fica rodando até ser uma opção de login inválida
while True:
    
    # pega informações digitadas na tela de login, retorna um dicionário referente ao usuário
    login = interfaceLogin.main(usuarios)

    # caso o usuário seja válido
    if login != None:
        # entra no terminal de operações, vai retornar uma das opções escolhidas
        op = interfaceOperacoes.main(login)

        # enquanto a opção não seja de voltar para o login, ficará rodando em uma das opções do terminal
        while op != '0':
            # caso a opção seja de saque
            if op == '1':
                op = interfaceSaque.main(login)

            # caso a opção seja de depósito
            if op == '2':
                op = interfaceDeposito.main(login)

            # caso a opção seja de saldo
            if op == '3':
                op = interfaceSaldo.main(login)

            # caso a opção seja de transferência
            if op == '4':
                op = interfaceTransferencia.main(login)

            # caso a opção seja de pagamento
            if op == '6':
                op = interfacePagamento.main(login)

            # caso a opção dentro de uma das operações seja voltar, isso fará ir para as operações novamente
            if op == '5':
                op = interfaceOperacoes.main(login)
    # caso a opção seja não especificada ou decida sair, encerra o programa
    else:
        break

# mensagem de saida
messagebox.showinfo('Informação', 'Saindo...')
