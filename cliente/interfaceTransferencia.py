from interfaceConfig import *
from testeUsuarios import *

# classe para as opções de transferência
class Transferencia(object):
    def __init__(self, janela, usuario):
        self.usuario = usuario
        self.janela = janela

        # pega o saldo disponível do usuário
        self.valorDisponivel = float(usuario['saldo'])

        # armazena o texto para colocar no label referente ao saldo disponível
        self.dispo = 'Valor disponível para transferência: R$ {:.2f}'.format(float(usuario['saldo']))

        # define a mensagem do topo
        self.lbt = Label(janela, text='Transferência', bg=corFundo, fg=corLetraNome,
                         font=("Verdana", 20))
        self.lbt.place(x=350, y=10)

        # define a mensagem sobre o valor disponível
        self.lbtDisponivel = Label(janela, text=self.dispo, bg=corFundo, fg=corLetra, font=('verdana', 15))
        self.lbtDisponivel.place(x=100, y=100)

        # define o label com o texto Agencia
        self.lbtAgencia = Label(janela, text='Agência: ', bg=corFundo, fg=corLetra, font=('verdana', 15))
        self.lbtAgencia.place(x=100, y=250)

        # define o campo de texto de Agencia
        self.entAgencia = Entry(janela, width='10', font=('verdana', 13))
        self.entAgencia.place(x=485, y=250)

        # define o label com o texto Conta
        self.lbtConta = Label(janela, text='Conta: ', bg=corFundo, fg=corLetra, font=('verdana', 15))
        self.lbtConta.place(x=100, y=300)

        # define o campo de texto Conta
        self.entConta = Entry(janela, width='10', font=('verdana', 13))
        self.entConta.place(x=485, y=300)

        # define o label com o texto sobre o valor da transferencia
        self.lbtInfo = Label(janela, text='Informe o valor de transferência:  R$', bg=corFundo, fg=corLetra, font=('verdana', 15))
        self.lbtInfo.place(x=100, y=350)

        # define o campo de texto referente ao valor a ser digitado
        self.entValor = Entry(janela, width='10', font=('verdana', 13))
        self.entValor.place(x=485, y=350)

        # define o botão Transferir
        self.btTransferir = Button(janela, text='Transferir', width='10', height='3', bg='#115', fg='white',
                              font=('verdana', 15), command=self.transferir)
        self.btTransferir.place(x=300, y=400)

        #define o botão Voltar
        self.btVoltar = Button(janela, text='Voltar', width='5', height='2', bg='#115', fg='white',
                               font=('verdana', 15), command=self.voltar)
        self.btVoltar.place(x=100, y=500)

        #define o botão Sair
        self.btSair = Button(janela, text='Sair', width='5', height='2', bg='#115', fg='white', font=('verdana', 15),
                             command=self.exit)
        self.btSair.place(x=200, y=500)

    # função para transferir dinheiro para outra conta
    def transferir(self):
        # pegando os valores que estão nos campos
        valorDigitado = str(self.entValor.get())
        agenciaDigitada = str(self.entAgencia.get())
        contaDigitada = str(self.entConta.get())

        # informar um alerta caso um dos campos não esteja preenchido
        if len(valorDigitado) == 0 or len(agenciaDigitada) == 0 or len(contaDigitada) == 0:
            messagebox.showinfo('Informação', 'Todos os campos precisam ser preenchidos')

        # caso todos os campos estejam preenchidos
        else:
            # caso seja digitado um valor maior que tem na conta
            if float(valorDigitado) > self.valorDisponivel:
                messagebox.showinfo('Informação', 'Saldo indisponível')
                self.limparCampo()
            # caso seja digitado um valor disponível
            else:
                # variável usada como flag
                existeConta = False

                # analisa todos os usuários registrados
                for usuario in usuarios:
                    # caso encontre uma conta registrada
                    if usuario['agencia'] == agenciaDigitada and usuario['conta'] == contaDigitada:
                        existeConta = True

                        # pergunta se o usuário quer fazer a transferência mesmo, mostrando os dados do destinatário
                        op = messagebox.askquestion('Informação', 'Deseja fazer a transferência para:\nNome: ' + usuario['nome'] +
                                                    ' ' + usuario['sobrenome'] + '\nAgência: ' + usuario['agencia'] + '\nConta: ' +
                                                    usuario['conta'] + '\nCPF: ' + usuario['cpf'] + '\nValor: ' + valorDigitado + ' R$')

                        # caso o usuário queira seguir com a transferência
                        if op == 'yes':
                            messagebox.showinfo('Informação', 'Transferência realizada com sucesso.\nPor favor retire o comprovante')

                            # desconta o valor da conta atual
                            self.valorDisponivel -= float(valorDigitado)
                            self.usuario['saldo'] = self.valorDisponivel

                            # adiciona o valor na conta destino
                            valorDestino = float(usuario['saldo'])
                            valorDestino += float(valorDigitado)
                            usuario['saldo'] = str(valorDestino)

                            # atualiza label com o valor disponível
                            self.lbtDisponivel['text'] = 'Valor disponível para saque: R$ {:.2f}'.format(float(self.valorDisponivel))

                            # limpa os campos de texto
                            self.limparCampo()

                        # caso o usuário não queira seguir com a transferência
                        else:
                            messagebox.showinfo('Informação', 'Transferência não realizada')
                            self.limparCampo()

                # caso a conta não seja encontrada
                if not existeConta:
                    messagebox.showinfo('Informação', 'Conta não encontrada')
                    self.limparCampo()

    # funções de voltar para a tela de operações ou de voltar para a tela de login
    def voltar(self):
        operation[0] = '5'
        self.janela.destroy()

    def exit(self):
        messagebox.showinfo('Informação', 'Saindo...')
        operation[0] = '0'
        self.janela.destroy()

    # função que limpa os campos de texto
    def limparCampo(self):
        self.entValor.delete(0, END)
        self.entValor.insert(0, '')
        self.entAgencia.delete(0, END)
        self.entAgencia.insert(0, '')
        self.entConta.delete(0, END)
        self.entConta.insert(0, '')

# quando cair nos casos de voltar ou sair, retornará a opção escolhida
def main(usuario):
    inicio(Transferencia, usuario)
    return operation[0]