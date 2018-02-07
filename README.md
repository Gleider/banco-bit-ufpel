# banco-bit-ufpel
Trabalho da disciplina de Redes. Criação de um banco fictício onde há interação entre cliente e servidor. O projeto está sendo feito em Python.

# Como executar no Linux
Para executar em ambiente linux, é só ir na raíz do projeto e digitar:

       >> sh exec.sh

Isso executará o script.

# O que precisa para rodar?

<ul>
<li> Python3</li>
<li>TKinter para python3. Caso não tenha digitar:</li>

       >> apt-get install python3-tk
              
<li><li>Bcrypt para python3. Caso não tenha instalar pelo pip:</li></li>

       >> pip install bcrypt
       
<li><li>Para Debian e o Ubuntu, o seguinte comando garante que as dependências necessárias do Bcrypt estão instaladas:</li></li>
       
              >> apt-get install build-essential libffi-dev python-dev

<li><li>Caso não tenha o pip (gerenciador de pacotes do Python):</li></li>

              >> apt-get install python3-pip

<li>Sqlite3 (apenas para o lado do servidor). Para instalar:</li>

       >> apt-get install libsqlite3-dev
</ul>
