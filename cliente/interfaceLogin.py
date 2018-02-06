from interfaceConfig import *

login = ['0']

class Login(object):
    def __init__(self, janela, usuarios):
        self.usuarios = usuarios
        self.janela = janela

        self.lbt = Label(janela, text='Tela de Login', bg=corFundo, fg=corLetra, font=("Verdana", 24))   #Define o label dentro da janela dizendo a mensagem do topo
        self.lbt.place(x=300, y=50)              #Adiciona o label na posição especificada

        self.entLogin = Entry(janela, width='18', font=('verdana', 18))        #cria a caixa de texto de login
        self.entLogin.place(x=300, y=200)     #posiciona a caixa de login

        self.entSenha = Entry(janela, show="*", width='18', font=('verdana', 18))        #cria a caixa de texto da senha
        self.entSenha.place(x=300, y=300)     #posiciona a caixa de texto da senha

        self.lbLogin = Label(janela, text="Login", bg=corFundo, fg=corLetra, font=('verdana', 20))     #cria label dizendo login
        self.lbLogin.place(x=200, y=200)      #posiciona label login

        self.lbSenha = Label(janela, text="Senha", bg=corFundo, fg=corLetra, font=('verdana', 20))     #cria label dizendo senha
        self.lbSenha.place(x=200, y=300)      #posiciona label senha

        self.btEntrar = Button(janela, text="Entrar", bg="#115", fg="white", width='8', height='3',
                               font=('verdana', 20), command=self.entrar)
        self.btEntrar.place(x=350, y=400)

        self.btSair = Button(janela, text="Sair", bg="#115", fg="white", width='10', height='3', command=self.exit)
        self.btSair.place(x=50, y=450)


    def entrar(self):
        # log e senha serão verificados no banco de dados
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

    def exit(self):
        messagebox.showinfo('Informação', 'Saindo...')
        exit()

def main(usuarios):
    inicio(Login, usuarios)
    return login[0]



