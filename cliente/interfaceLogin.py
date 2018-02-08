from interfaceConfig import *

login = ['0']

# classe para o login
class Login(object):
    def __init__(self, janela, usuarios):
        self.usuarios = usuarios
        self.janela = janela

        # armazena o texto para colocar no label referente ao texto superior
        self.lbt = Label(janela, text='Tela de Login', bg=corFundo, fg=corLetra, font=("Verdana", 24))
        self.lbt.place(x=300, y=50)

        # define o campo de texto referente ao número da conta
        self.entLogin = Entry(janela, width='18', font=('verdana', 18))
        self.entLogin.place(x=300, y=200)

        # define o campo de texto referente a senha
        self.entSenha = Entry(janela, show="*", width='18', font=('verdana', 18))
        self.entSenha.place(x=300, y=300)

        # define a label com o texto Login
        self.lbLogin = Label(janela, text="Login", bg=corFundo, fg=corLetra, font=('verdana', 20))
        self.lbLogin.place(x=200, y=200)

        # define a label com o texto senha
        self.lbSenha = Label(janela, text="Senha", bg=corFundo, fg=corLetra, font=('verdana', 20))
        self.lbSenha.place(x=200, y=300)

        # define o botão entrar
        self.btEntrar = Button(janela, text="Entrar", bg="#115", fg="white", width='8', height='3',
                               font=('verdana', 20), command=self.entrar)
        self.btEntrar.place(x=350, y=400)

        # define o botão sair
        self.btSair = Button(janela, text="Sair", bg="#115", fg="white", width='10', height='3', command=self.exit)
        self.btSair.place(x=50, y=450)

    # função para solicitar acesso de usuário no servidor
    def entrar(self):
        logSucc = False
        log = str(self.entLogin.get())
        senha = str(self.entSenha.get())
        for usuario in self.usuarios:
            if usuario['login'] == log and usuario['senha'] == senha:
                messagebox.showinfo('Informação', 'Login executado com sucesso')
                login[0] = usuario
                self.janela.destroy()
                logSucc = True
        if not logSucc:
            messagebox.showinfo('Informação', 'Não foi possível realizar login')

    # função para encerrar a aplicação
    def exit(self):
        messagebox.showinfo('Informação', 'Saindo...')
        exit()

# quando finalizar a loop da interface, retornará opção definida
def main(usuarios):
    inicio(Login, usuarios)
    return login[0]



