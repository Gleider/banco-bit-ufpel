# banco-bit-ufpel
Trabalho da disciplina de Redes. Criação de um banco fictício onde há interação entre cliente e servidor. O projeto está sendo feito em Python.

# Como executar no Linux
Para executar em ambiente linux, é só ir na raíz do projeto e digitar:

       >> sh exec.sh

Isso executará o script.

# O que precisa para rodar?
1. Python3

2. TKinter para python3. Caso não tenha digitar:

       >> apt-get install python3-tk

3. Bcrypt para python3. Para Debian e Ubuntu, o seguinte comando garante as dependências necessárias do Bcrypt sejam instaladas:
       
       >> apt-get install build-essential libffi-dev python-dev

3.1 Para instalar o Bcrypt:
       
       >> pip3 install bcrypt

3.2 Caso não tenha o pip (gerenciador de pacotes do Python):

       >> apt-get install python3-pip

4. Pacote de criptografia. Para instalar

       >> pip3 install cryptography

5. Sqlite3 (apenas para o lado do servidor). Para instalar:

       >> apt-get install libsqlite3-dev
