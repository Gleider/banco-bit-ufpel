from tkinter import *
from tkinter import messagebox

# módulo contendo as configurações padrões

# define a opção inicial para todas as telas
operation = ['0']

# definição das cores usadas
corFundo = '#005'
corLetra = 'white'
corLetraNome = '#AAA'

# função de inicialização em todas as telas
def inicio(object, usuario=None):
    # inicializa janela principal
    janela = Tk()

    # define o título da janela
    janela.title('Banco Bit-Ufpel')

    # faz com que a janela não seja redimensionável
    janela.resizable(False, False)

    # adiciona cor de fundo na janela
    janela.configure(background=corFundo)  # define cor de fundo da janela

    # define as dimensões da janela, centralizando no monitor independente do tamanho da tela
    w = 800
    h = 600
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('{}x{}+{}+{}'.format(int(w), int(h), int(x), int(y)))  # define tamanho da janela

    # envia qual a classe será iniciada
    object(janela, usuario)

    # faz com a janela apareça na tela
    janela.mainloop()

