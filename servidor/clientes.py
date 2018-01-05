import sqlite3

conectar = sqlite3.connect('bancoBitUFPEL.db')
c = conectar.cursor()

#
#CRIA O BANCO DE DADOS
#
def criar_db():
    c.execute("""
    create table if not exists Cliente (
        numConta INT UNIQUE NOT NULL, 
        nome varchar(100) not null,
        cpf char(14) UNIQUE NOT NULL,
        logradouro varchar(100) not null,
        complemento varchar(40) default null,
        bairro varchar(60) not null,
        cidade varchar(60) not null,
        uf char(2) not null,
        cep char(9) not null,
        saldo decimal(10 , 2),
        primary key (numConta)
    );
    """)

    c.execute("""
    create table if not exists Login(
        numConta int UNIQUE not null,
        senha char(20) not null, 
        primary key(numConta),
        foreign key (numConta) references Cliente (numConta) ON DELETE CASCADE
    );
    """)

#
# CRIA UMA NOVA CONTA E INSERE O CLIENTE
#
def novaConta(nome, senha, cpf, logradouro, complemento, bairro, cidade, uf, cep, saldo):
    quantConta = 'Select max(numConta) from Login'
        
    #Verifica se tem alguma conta cadastrada no banco de dados, se tiver atribui o número de conta 1, caso contrário a nova conta será o número da maior conta cadastrada incrementado em 1
    c.execute(quantConta)
    row = c.fetchone()
    row = row[0]
    if row is None:
        numConta = 1
    else:
        numConta = row + 1

    #insere o cliente no banco de dados
    c.execute('insert into Cliente(numConta, nome, cpf, logradouro, complemento, bairro, cidade, uf, cep, saldo) values (?,?,?,?,?,?,?,?,?,?)', (numConta, nome, cpf, logradouro, complemento, bairro, cidade, uf, cep, saldo))
    c.execute('insert into Login(numConta, senha) values (?,?)', (numConta, senha))
    conectar.commit()


#
# MENU CADASTRO NOVO CLIENTE
#
def menuCadastro():
    try:
        #Lendo nome, o while eh necessario, caso contrario permite a entrada vazia, sem nenhum caracter apenas com o enter
        while True:
            nome = str.title(input('nome: '))
            if nome.istitle() == True:
                break

        #Lendo senha
        while True:
            senha = str(input('senha: '))
            if senha.isalnum() == True:
                break

        #Entrando com um cpf de 11 digitos
        while True:
            try:
                cpf=str(input('cpf: '))  #Verifica se soh tem numeros e se tem 11 digitos
                if cpf.isdigit() and len(cpf)==11:
                    cpf= "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])
                    break
                else:
                    raise
            except:
                print('CPF tem que ter 11 dígitos')

        #lendo logradouro
        while True:
            logradouro=str.title(input('logradouro: '))
            if logradouro.istitle() == True:
                break

        #lendo complemento
        complemento=str.title(input('complemento: '))
        if len(complemento) < 1:
            complemento = None

        #lendo bairro
        while True:
            bairro=str.title(input('bairro: '))
            if bairro.istitle() == True:
                break

        #lendo cidade
        while True:
            cidade=str.title(input('cidade: '))
            if cidade.istitle() == True:
                break

        #lendo UF (dois digitos)
        while True:
            try:
                uf=str.upper(input('uf: '))
                if uf.isalpha() and len(uf)==2:
                    break
                else:
                    raise
            except:
                print('uf deve ter duas letras')
        
        #lendo cep de 8 digitos
        while True:
            try:
                cep=str(input('cep: '))
                if cep.isdigit() and len(cep)==8:
                    cep= "%s-%s" % (cep[0:5], cep[5:9])
                    break
                else:
                    raise
            except:
                print('cep deve ter 8 números')
                
        #lendo saldo
        while True:
            try:
                saldo=float(input('saldo: '))
                break
            except ValueError:
                print('Valor inválido')

        #gravando no banco de dados
        try:
            novaConta(nome, senha, cpf, logradouro, complemento, bairro, cidade, uf, cep, saldo)
            print('Conta criada com sucesso')
        except:
            print('Erro ao inserir no Banco de Dados')
    except:
        print('Nao foi possivel criar a conta')

#
# DELETA CONTA
#
def deletarConta(numConta):
    deleteConta = 'Delete from Cliente Where numConta = ?'
    #ativarChave = 'PRAGMA foreign_keys=ON'
    c.execute(ativarChave)
    c.execute(deleteConta, (numConta,))
    conectar.commit()
'''
try:
    criar_db()
except:
    print('Tabelas já criadas')
'''

#menuCadastro()
#conectar.close()

'''
try:
    deletarConta(2)
except:
    print('Erro ao deletar conta')
'''
