from interfaceConfig import *

# classe para a opção de saque
class Saque(object):
    def __init__(self, janela, usuario):
        self.janela = janela
        self.usuario = usuario

        # armazena o texto para colocar no label referente ao saldo disponível
        dispo = 'Valor disponível para saque: R$ {:.2f}'.format(float(usuario['saldo']))

        # pega o saldo do usuário
        self.valorDisponivel = float(usuario['saldo'])

        # define label principal do topo
        self.lbt = Label(janela, text='Saque', bg=corFundo, fg=corLetraNome, font=("Verdana", 20))
        self.lbt.place(x=350, y=10)

        # define label informando saldo disponível
        self.lbtDisponivel = Label(janela, text=dispo, bg=corFundo, fg=corLetra, font=('verdana', 15))
        self.lbtDisponivel.place(x=100, y=100)

        # define label pedindo o valor de saque
        self.lbtInfo = Label(janela, text='Informe o valor de saque:  R$', bg=corFundo, fg=corLetra, font=('verdana', 20))
        self.lbtInfo.place(x=100, y=200)

        # define a caixa de texto do valor de saque
        self.entSaque = Entry(janela, width='10', font=('verdana', 18))
        self.entSaque.place(x=510, y=200)

        # define o botão de saque
        self.btSaque = Button(janela, text='Sacar', width='10', height='3', bg='#115', fg='white',
                              font=('verdana', 15), command=self.sacar)
        self.btSaque.place(x=300, y=300)

        # define os botões de voltar a tela de operações ou voltar para a tela de login
        self.btVoltar = Button(janela, text='Voltar', width='5', height='2', bg='#115', fg='white',
                               font=('verdana', 15), command=self.voltar)
        self.btVoltar.place(x=100, y=500)

        self.btSair = Button(janela, text='Sair', width='5', height='2', bg='#115', fg='white', font=('verdana', 15),
                             command=self.exit)
        self.btSair.place(x=200, y=500)

    # função de sacar
    def sacar(self):

        #pega o valor digitado na caixa de texto de valor de saque
        valorDigitado = str(self.entSaque.get())

        # caso a caixa esteja vazia
        if not valorDigitado.isalnum():
            messagebox.showinfo('Informação', 'O campo de saque precisa ser preenchido')

        # caso a caixa não esteja vazia
        else:
            # caso o valor de saque esteja indisponível
            if float(valorDigitado) > self.valorDisponivel:
                messagebox.showinfo('Informação', 'Saldo indisponível')

                # apaga as informações dos campos
                self.entSaque.delete(0, END)
                self.entSaque.insert(0, '')

            # caso o valor de saque esteja disponível
            else:
                messagebox.showinfo('Informação', 'Saque realizado com sucesso.\nPor favor retire o dinheiro')

                # desconta o valor de saque do valor total na conta
                self.valorDisponivel -= float(valorDigitado)
                self.usuario['saldo'] = str(self.valorDisponivel)
                self.lbtDisponivel['text'] = 'Valor disponível para saque: R$ {:.2f}'.format(float(self.valorDisponivel))

                # apaga as informações dos campos
                self.entSaque.delete(0, END)
                self.entSaque.insert(0, '')

    # funções de voltar para a tela de operações ou voltar para a tela de login
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