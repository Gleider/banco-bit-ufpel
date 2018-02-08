from cryptography.fernet import Fernet
import base64, pickle
from socket import *

key = base64.urlsafe_b64encode(b'BANCOBITUFPEL0123456789ABCDEFGHI') #chave criptografica

def criptografar(conteudo):
    result = Fernet(key)
    return result.encrypt(conteudo)

def decriptografar(conteudo):
    result = Fernet(key)
    return result.decrypt(conteudo)    

serverName='192.168.0.101'
serverPort= 1024
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    vetor = [None, None, None, None, None] # operacao, numContaRem, numContaDest, valor, senha
    print('\nTESTANDO Login')
    vetor[0] = 0 #login
    vetor[1] = int(input('Entre com a conta: ')) #numConta
    vetor[4] = str.encode(input('Entre com a senha: ')) #senha
    s = pickle.dumps(vetor) #transforma objeto em sequência de byte
    s = criptografar(s) #criptografa a mensagem
    clientSocket.sendall(s) #envia a mensagem criptografada
    msg = clientSocket.recv(2048) #recebe o retorno
    msg = decriptografar(msg) #decriptogrando mensagem
    msg = pickle.loads(msg) #transforma a sequência de byte em objeto
    print(msg) #mostre a mensagem recebida
    
    print('\nTESTANDO Saque')
    vetor = [1, 1, None, 200, None]
    s = pickle.dumps(vetor) #transforma objeto em sequência de byte
    s = criptografar(s) #criptografa a mensagem
    clientSocket.sendall(s) #envia a mensagem criptografada
    msg = clientSocket.recv(2048) #recebe o retorno
    msg = decriptografar(msg) #decriptogrando mensagem
    msg = pickle.loads(msg) #transforma a sequência de byte em objeto
    print(msg)
    
    print('\nTESTANDO Deposito')
    vetor = [2, 1, None, 100, None]
    s = pickle.dumps(vetor) #transforma objeto em sequência de byte
    s = criptografar(s) #criptografa a mensagem
    clientSocket.sendall(s) #envia a mensagem criptografada
    msg = clientSocket.recv(2048) #recebe o retorno
    msg = decriptografar(msg) #decriptogrando mensagem
    msg = pickle.loads(msg) #transforma a sequência de byte em objeto
    print(msg)

    print('\nTESTANDO Transferencia - Etapa 1')
    vetor = [3, 1, 2, 100, None]
    s = pickle.dumps(vetor)
    s = criptografar(s)
    clientSocket.sendall(s)
    msg = clientSocket.recv(2048)
    msg = decriptografar(msg)
    msg = pickle.loads(msg)
    print(msg)

    if(msg[0]==0): #Se é possível fazer o saque baseado na opção anterior
        print('\nTESTANDO Transferencia - Etapa 2')
        vetor = [4, 1, 2, 100, None]
        s = pickle.dumps(vetor)
        s = criptografar(s)
        clientSocket.sendall(s)
        msg = clientSocket.recv(2048)
        msg = decriptografar(msg)
        msg = pickle.loads(msg)
        print(msg)

    print('\nTESTANDO Informações Cadastrais')
    vetor = [5, 1, None, None, None]
    s = pickle.dumps(vetor)
    s = criptografar(s)
    clientSocket.sendall(s)
    msg = clientSocket.recv(2048)
    msg = decriptografar(msg)
    msg = pickle.loads(msg)
    print(msg)

    print('\nTESTANDO Pagamento')
    vetor = [6, 1, None, 100, None]
    s = pickle.dumps(vetor)
    s = criptografar(s)
    clientSocket.sendall(s)
    msg = clientSocket.recv(2048)
    msg = decriptografar(msg)
    msg = pickle.loads(msg)
    print(msg)
    
    break
clientSocket.close()
