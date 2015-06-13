Title: Instalando Pelican no Python 3
Date: 2015-06-04 10:30
Author: Otávio Carneiro
Slug: Instalando-Pelican-no-Python3
Tags: python, pelican, virtualenv

Montei todo meu ambiente pelican para poder publicar meu blog estaticamente e joguei meu código no github para facilitar a vida.

A ideia era poder editar a partir do meu notebook ou do desktop indistintamente, sem nenhum problema. O procedimento seria:

1) Baixar o projeto do github:

    :::bash
    git clone https://github.com/ocarneiro/pelican-carneiro-blog.git  
    cd pelican-carneiro-blog  

2) Montar e ativar um ambiente python3:  

    :::bash
    sudo apt-get install python3-pip  
    sudo pip3 install virtualenv  
    virtualenv env  
   
3) Ativar o ambiente    

    :::bash
    source env/bin/activate  

4) Instalar as dependências:  

    :::bash
    pip3 install -r requirements.txt  

Só que neste último passo, o pip falhou...

A mensagem de erro era enorme, mas o final era assim:  

    :::bash
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

A [internet](http://stackoverflow.com/questions/29778715/pip-install-reportlab-error-command-x86-64-linux-gnu-gcc-failed-with-exit-sta) dizia que o problema poderia ser a falta do pacote python-dev. Então tentei:  

    :::bash
    sudo apt-get install python3-dev  
    sudo apt-get install python-dev  
    
Só que ambos estavam instalados. Fui olhar melhor a mensagem de erro e estava, bem claro:  
\*\* make sure the development packages of **libxml2** and **libxslt** are installed \*\*

Bingo?!:  
    
    :::bash
    sudo apt-get install libxml2 libxslt  

Não... Não achei o libxslt... Mas existe um libxslt1-dev que depende de um libxml2-dev. Parecia promissor:  
    
    :::bash
    sudo apt-get install libxslt1-dev  
    
Pronto! Agora sim:  
    
    :::bash
    pip3 install -r requirements.txt  
    
Já posso publicar este blog de onde eu quiser!  

Abs.,  
Otávio
