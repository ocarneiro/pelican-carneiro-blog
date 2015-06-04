Title: Como instalar um ambiente de desenvolvimento Python no Windows
Date: 2014-06-17 14:53
Author: Otávio Carneiro
Slug: Como-instalar-um-ambiente-de-desenvolvimento-Python-no-Windows

Hoje eu fui desenvolver com Python no meu notebook com Windows 8 e
descobri que não tinha nem pip, nem virtualenv, nem mesmo o setuptools
instalado... E agora, José? Como é que você prepara uma máquina no
Windows para trabalhar com Django, Flask, suds e outras tantas coisas
legais que só o Python pode oferecer?

Eu tentei várias coisas, baixei scripts .py para rodar diretamente,
instalei programas e mais programas dentro e fora do Cygwin, versões
64-bit e 32-bit de uma infinidade de pacotes e nada parecia dar certo.
Então, resolvi começar de novo, explicando para vocês meu procedimento.

Primeiro de tudo, você precisa do
[Python](https://www.python.org/downloads/), lógico. A versão mais atual
é a 3.3, mas muita gente ainda usa a 2.7. Eu sou uma dessas pessoas.
Estou fazendo um curso de "[Introdução à Ciência da Computação e
Programação com
Python](https://www.edx.org/course/mitx/mitx-6-00-1x-introduction-computer-1841)"
no site [edx.org](http://edx.org/) e eles usam a versão 2.7.

Instalar o Python é fácil. Ele tem um instalador para Windows e tudo
mais... Ainda assim, você precisa atentar para as variáveis de ambiente.
Você deve ajustar o seu PATH. Algo assim:

PATH=%PATH%;C:\\Python27;C:\\Python27\\Scripts  
Agora, sim, você pode instalar o setuptools, que vai te permitir
instalar o virtualenv, o pip e os demais utilitários do Python que vão
te permitir instalar as bibliotecas e tudo mais.

Para instalar o setuptools, segui as [orientações do site
oficial](https://pypi.python.org/pypi/setuptools/#windows-8-powershell),
ou seja, usei o PowerShell. Eu nunca tinha usado isso, não sabia nem o
que era. Aparentemente, é só mais um console, como o cmd e o cygwin.
Apertei o botão do windows, escrevi "PowerShell", cliquei com o botão
direito do mouse e pedi para Executar como Administrador. No console que
se abriu, rodei o comando a seguir:

``` {.literal-block}
(Invoke-WebRequest https://bootstrap.pypa.io/ez_setup.py).Content | python -
```

Parece mágica, mas na verdade o que isso faz é baixar o arquivo
ez\_setup.py (tipo um wget ou curl) e depois executa ele com o python.

Eu já tinha colocado ali em cima a pasta Python27\\Scripts no Path, mas
é agora que isso se torna útil. O instalador do setuptools grava ali o
arquivo easy\_install.exe. Se você não incluiu a pasta no Path, inclua
agora. Depois, saia do PowerShell e abra um console com permissões de
administrador. Eu fiz assim: (Windows) cmd (botão direito) Executar como
Administrador.

Dentro desse console de administrador é que nós vamos executar o
easy\_install para instalar o pip, assim:

easy\_install pip

E agora, com o pip, você pode instalar o virtualenv:

pip install virtualenv

O virtualenv no Windows funciona um pouco diferente do Linux. Para
ativar e desativar o ambiente virtual, ele grava arquivos .bat no
diretório Scripts. Então para usar um novo ambiente virtualenv você
faria:

virtualenv venv  
cd venv  
Scripts/activate.bat

Em algumas de minhas primeiras tentativas, este ambiente não funcionava
e o erro não era claro, mas quando finalmente consegui uma mensagem
legível descobri que o problema era de permissões. Bastou executar os
comandos em um console como administrador que isso resolveu o problema.
Não é a melhor solução, mas deu certo na falta de algo melhor.

Se tiverem outras sugestões de boas práticas, sou todo ouvidos. Sempre
trabalhei com Java e sempre com outras pessoas (ou equipes) que cuidavam
da infraestrutura, então tudo isso é meio novidade para mim.

ATUALIZAÇÃO (em 18/06/2014): E o git? Pois é, instalar as ferramentas
Python sem usar o Cygwin tem essa desvantagem de te deixar fora do
ambiente Unix-like e sem essa ferramenta essencial... Mas se você
instalar o [Git para Windows](http://git-scm.com/download/win),  pode
optar por utilizá-lo no cmd (console normal do Windows) e por permitir
que ele instale também outros comandos Unix nesse ambiente, como o ls,
ssh, etc. Aí, sim, você nem vai sentir tanta falta do Cygwin...

Para instalar alguns pacotes, como o
[pandas](http://pandas.pydata.org/pandas-docs/stable/install.html), você
vai precisar instalar no Windows o [Visual C++ 2008 Express
Edition](http://go.microsoft.com/?linkid=7729279). Há algumas [perguntas
e respostas no
StackOverflow](http://stackoverflow.com/questions/3047542/building-lxml-for-python-2-7-on-windows/5122521#5122521)
sobre isso.

Abs.,  
Otávio

