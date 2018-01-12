import pickle

from socket import *
serverName='192.168.1.38'
serverPort= 1024
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    vetor = [None, None, None, None, None] # operacao, numContaRem, numContaDest, valor, senha
    
    print('Saque')
    vetor = [1, 1, None, 500, None]
    s = pickle.dumps(vetor)
    clientSocket.sendall(s)
    msg = clientSocket.recv(1024)
    msg = pickle.loads(msg)
    print(msg)

    print('\nDeposito')
    vetor = [2, 1, None, 1000, None]
    s = pickle.dumps(vetor)
    clientSocket.sendall(s)
    msg = clientSocket.recv(1024)
    msg = pickle.loads(msg)
    print(msg)

    print('\nTransferencia - Etapa 1')
    vetor = [3, 1, 2, 1000, None]
    s = pickle.dumps(vetor)
    clientSocket.sendall(s)
    msg = clientSocket.recv(1024)
    msg = pickle.loads(msg)
    print(msg)

    print('\nTransferencia - Etapa 2')
    vetor = [4, 1, 2, 1000, None]
    s = pickle.dumps(vetor)
    clientSocket.sendall(s)
    msg = clientSocket.recv(1024)
    msg = pickle.loads(msg)
    print(msg)

    print('\nInformações Cadastrais')
    vetor = [5, 1, None, None, None]
    s = pickle.dumps(vetor)
    clientSocket.sendall(s)
    msg = clientSocket.recv(1024)
    msg = pickle.loads(msg)
    print(msg)
    
    break
clientSocket.close()
