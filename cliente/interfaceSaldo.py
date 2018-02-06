from interfaceConfig import *

# classe de saque
class Saque(object):
    def __init__(self, janela, usuario):
        self.janela = janela

        # armazena o texto para colocar no label referente ao saldo disponível
        self.dispo = 'Valor disponível: R$ {:.2f}'.format(float(self.valorDisponivel))

        # pega informações do usuário e salva nas variáveis da classe
        self.valorDisponivel = usuario['saldo']
        self.user = usuario['nome'] + ' ' + usuario['sobrenome']
        self.cpf = usuario['cpf']
        self.agencia = usuario['agencia']
        self.conta = usuario['conta']

        # define o label principal do topo
        self.lbt = Label(janela, text='Saldo', bg=corFundo, fg=corLetraNome, font=("Verdana", 20))
        self.lbt.place(x=350, y=10)

        # define o label Nome
        self.lbtNome = Label(janela, text='Nome: ' + self.user, bg=corFundo, fg=corLetra, font=('Vernada', 20))
        self.lbtNome.place(x=200, y=125)

        # define o label CPF
        self.lbtCpf = Label(janela, text='CPF: ' + self.cpf, bg=corFundo, fg=corLetra, font=('Vernada', 20))
        self.lbtCpf.place(x=200, y=175)

        # define o label Agência
        self.lbtAgencia = Label(janela, text='Agência: ' + self.agencia, bg=corFundo, fg=corLetra, font=('Vernada', 20))
        self.lbtAgencia.place(x=200, y=225)

        # define o label Conta
        self.lbtConta = Label(janela, text='Conta: ' + self.conta, bg=corFundo, fg=corLetra, font=('Vernada', 20))
        self.lbtConta.place(x=200, y=275)

        # define o label com o saldo disponível
        self.lbtDisponivel = Label(janela, text=self.dispo, bg=corFundo, fg=corLetra, font=('verdana', 20))
        self.lbtDisponivel.place(x=200, y=325)

        # define o botão  voltar
        self.btVoltar = Button(janela, text='Voltar', width='5', height='2', bg='#115', fg='white',
                               font=('verdana', 15), command=self.voltar)
        self.btVoltar.place(x=100, y=500)

        # define o botão sair
        self.btSair = Button(janela, text='Sair', width='5', height='2', bg='#115', fg='white',
                             font=('verdana', 15), command=self.exit)
        self.btSair.place(x=200, y=500)

    # define as funções de voltar para a tela de operações ou para a tela de login
    def voltar(self):
        operation[0] = '5'
        self.janela.destroy()

    def exit(self):
        messagebox.showinfo('Informação', 'Saindo...')
        operation[0] = '0'
        self.janela.destroy()

# quando cair nos casos de voltar ou sair, retornará a opção escolhida
def main(usuario):
    inicio(Saque, usuario)
    return operation[0]