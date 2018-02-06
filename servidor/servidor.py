import socket, pickle, transacoes
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

#criptografar mensagem
def criptografar(conteudo):
    chave = '0123456789ABCDEF'
    aes = AES.new(chave, AES.MODE_ECB)
    cript = aes.encrypt(conteudo * 16)
    return b64encode(cript)

#decriptografar mensagem
def decriptografar(conteudo):
    chave = '0123456789ABCDEF'
    aes = AES.new(chave, AES.MODE_ECB)
    cript = aes.decrypt(b64decode(conteudo * 16))
    return cript

host = "192.168.1.38" #IP SERVIDOR
port = 1024 #PORTA USADA
mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)

print ('Servidor Banco bitUFPEL')
while True:
    conn, addr = mySocket.accept()
    print ("Conectado por: " + str(addr))

    try:
        #operações feitas no servidor
        while True:
            try:
                msg = conn.recv(2048) #recebendo mensagem
                msgRetorno = [None, None, None, None, None, None, None, None, None, None, None] #msgRetorno [result, nome, cpf, logradouro, complemento, bairro, cidade, uf, saldo, nomeFavorecido]
                msg = decriptografar(msg) #decriptografando mensagem
                msg = pickle.loads(msg) #msg [operacao, numContaRem, numContaDest, valor, senha]
            except:
                break
            
            #LOGIN
            if (msg[0]==0):
                print('\nLOGIN')
                operacoes = transacoes.operacoes()
                result = operacoes.login(msg[1], msg[4])
                if(result!=-1):
                    msgRetorno[0]=0
                    msgRetorno[1]=result[0] #nome
                    msgRetorno[2]=result[1] #cpf
                    msgRetorno[9]=result[2] #saldo
                else:
                    msgRetorno[0]=1
                msgRetorno = pickle.dumps(msgRetorno) #transformando objeto em sequencia de bytes
                msgRetorno = criptografar(msgRetorno) #criptografando mensagem
                conn.send(msgRetorno) #enviando mensagem
                pass
            
            #SAQUE
            if(msg[0]==1):
                print('\nSAQUE')
                operacoes = transacoes.operacoes()
                result = operacoes.saque(msg[1], msg[3]) #numContaRem, valorSaque
                if(result>=0):
                    msgRetorno[0]=0 #Deposito realizado
                    msgRetorno[9]=result
                elif(result==-1):
                    msgRetorno[0]=1 #Erro não foi possível sacar o valor com as notas disponíveis
                elif(result==-2):
                    msgRetorno[0]=2 #Erro não há saldo suficiente para saque
                else:
                    msgRetorno[0]=3 #Erro saque não realizado
                msgRetorno = pickle.dumps(msgRetorno) #transformando objeto em sequencia de bytes
                msgRetorno = criptografar(msgRetorno) #criptografando mensagem
                conn.send(msgRetorno) #enviando mensagem
                pass
            
            #DEPOSITO
            elif(msg[0]==2):
                print('\nDEPÓSITO')
                operacoes = transacoes.operacoes()
                result = operacoes.deposito(msg[1], msg[3]) #numContaRem, valorDeposito
                if(result>=0):
                    msgRetorno[0]=0 #Deposito realizado com sucesso
                    msgRetorno[9]=result
                else:
                    msgRetorno[0]=1 #Erro depoósito não realizado
                msgRetorno = pickle.dumps(msgRetorno)
                msgRetorno = criptografar(msgRetorno) #criptografando mensagem
                conn.send(msgRetorno)
                pass
            
            #TRANSFERENCIA ETAPA 1
            elif(msg[0]==3):
                print('\nTRANSF ETP 1')
                operacoes = transacoes.operacoes()
                result = operacoes.transferencia(msg[1], msg[2], msg[3]) #numContaRem, valorDeposito
                if(result == '-1'):
                    msgRetorno[0]=1 #Erro conta de destino inexistente
                elif(result == '-2'):
                    msgRetorno[0]=2 #Erro nao ha saldo suficiente para transferencia
                elif(result == '-3'):
                    msgRetorno[0]=3 #Erro conta de origem e destino sao as mesmas
                else:
                    msgRetorno[0]=0 #Ok
                    msgRetorno[10]=result #Retorna nome do favorecido na transferencia
                msgRetorno = pickle.dumps(msgRetorno)
                msgRetorno = criptografar(msgRetorno)
                conn.send(msgRetorno)
                pass
            
            #TRANSFERENCIA ETAPA 2
            elif(msg[0]==4):
                print('\nTRANSF ETP 2')
                operacoes = transacoes.operacoes()
                result = operacoes.transferencia2(msg[1], msg[2], msg[3]) #numContaRem, valorDeposito
                if(result == '-1'):
                    msgRetorno[0]=1 #erro transferencia nao realizada
                else:
                    msgRetorno[0]=0 #transferencia realizada com sucesso
                    msgRetorno[9]=result #saldoAtualizado
                msgRetorno = pickle.dumps(msgRetorno)
                msgRetorno = criptografar(msgRetorno)
                conn.send(msgRetorno)
                pass
            
            #INFORMACOES CADASTRAIS 
            elif(msg[0]==5):
                print('\nINFO CADASTRAIS')
                operacoes = transacoes.operacoes()
                result = operacoes.infoCadastrais(msg[1]) #numContaRem, valorDeposito
                if(result!=-1):
                    msgRetorno[0]=0
                    msgRetorno[1]=result[0] #nome
                    msgRetorno[2]=result[1] #cpf
                    msgRetorno[3]=result[2] #logradouro
                    msgRetorno[4]=result[3] #complemento
                    msgRetorno[5]=result[4] #bairro
                    msgRetorno[6]=result[5] #cidade
                    msgRetorno[7]=result[6] #uf
                    msgRetorno[8]=result[7] #cep
                    msgRetorno[9]=result[8] #saldo
                else:
                    msgRetorno[0]=1 #erro nao foi possivel consultar informacaoes cadastrais
                msgRetorno = pickle.dumps(msgRetorno)
                msgRetorno = criptografar(msgRetorno)
                conn.send(msgRetorno)
                pass
    finally:
        print('Conexao Encerrada\n')
        conn.close()
transacoes.conectar.close()
