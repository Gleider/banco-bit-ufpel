import socket, pickle, transacoes

host = "192.168.1.38"
port = 1024
     
mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
print ('Servidor Banco bitUFPEL')

conn, addr = mySocket.accept()
print ("Connection from: " + str(addr))
while True:
    msg = conn.recv(1024)
    if not msg:
        break
    msg = pickle.loads(msg) #msg [operacao, numContaRem, numContaDest, valor, senha]
    msgRetorno = [None, None, None, None, None, None, None, None, None, None, None] #msgRetorno [result, nome, cpf, logradouro, complemento, bairro, cidade, uf, saldo, nomeFavorecido]

    #LOGIN
    if (msg[0]==0):
        print('\nLOGIN')
        pass
    
    #SAQUE
    elif(msg[0]==1):
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
        msgRetorno = pickle.dumps(msgRetorno)
        conn.send(msgRetorno)
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
        conn.send(msgRetorno)
        pass

print('Conexao Encerrada')
transacoes.conectar.close()
conn.close()
