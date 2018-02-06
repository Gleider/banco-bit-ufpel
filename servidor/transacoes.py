import sqlite3

conectar = sqlite3.connect('bancoBitUFPEL.db')
c = conectar.cursor()

class operacoes(object):
    def saque(self, numConta, valor):
        try:         
            c.execute('Select saldo from Cliente where numConta = ?', (numConta,))
            saldoConta = c.fetchone()
            saldoConta = saldoConta[0]
            
            if saldoConta >= valor:
                temp = valor % 5
                if temp == 0:
                    saldoConta = saldoConta - valor
                    c.execute('Update Cliente set saldo = ? Where numConta = ?', (saldoConta, numConta,))
                    conectar.commit()
                    print('Saque realizado com sucesso')
                else:
                    print('Não é possível sacar este valor com as notas disponíveis')
                    raise
            else:
                print('Não há saldo suficiente para saque')
                raise
        except:
            print('Saque não realizado')

    def deposito(self, numConta, valor):
        try:
            c.execute('Select saldo from Cliente where numConta = ?', (numConta,))
            saldoConta = c.fetchone()
            saldoConta = saldoConta[0]
            saldoConta = saldoConta + valor
            c.execute('Update Cliente set saldo = ? Where numConta = ?', (saldoConta, numConta,))
            conectar.commit()
            print('Deposito realizado com sucesso')
        except:
            print('Depósito não realizado')

    def transferencia(self, numContaRem, numContaDest, valor):
        try:
            if(numContaRem != numContaDest):
                c.execute('Select saldo from Cliente where numConta = ?', (numContaRem,))
                saldoRemetente = c.fetchone()
                saldoRemetente = saldoRemetente[0]
                c.execute('Select saldo from Cliente where numConta = ?', (numContaDest,))
                saldoDestino = c.fetchone()
                saldoDestino = saldoDestino[0]

                if(saldoRemetente >= valor):
                    saldoDestino = saldoDestino + valor
                    saldoRemetente = saldoRemetente - valor
                    c.execute('Update Cliente set saldo = ? Where numConta = ?', (saldoRemetente, numContaRem))
                    c.execute('Update Cliente set saldo = ? Where numConta = ?', (saldoDestino, numContaDest))
                    conectar.commit()
                    print('Transferencia realizada com sucesso')
                else:
                    print('Erro: Não há saldo suficiente para transferência')
                    raise
            else:
                print('Erro: Conta de origem e destino é mesma');
                raise
        except:
            print('Transferência não realizada')
