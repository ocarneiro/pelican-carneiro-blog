Title: Ambiente de desenvolvimento Python 3 no Jessie
Date: 2015-05-17 15:47
Author: Otávio Carneiro
Slug: Ambiente-de-desenvolvimento-Python-3-no-Jessie

Eu já tinha escrito sobre isso, mas o jeito que eu tinha criado o
ambiente de desenvolvimento na minha máquina era muito trabalhoso e as
versões atuais do Python (estou escrevendo em maio de 2015) tornaram a
vida mais fácil.

1\) Veja que versão de Python você tem instalada.  
    Se for a versão 3.4 ou superior, está tudo certo.  
    Se não for, instale o pacote python3.  
         Digite: sudo apt-get install python3

2\) Instale o pip do Python 3:  
     sudo apt-get install python3-pip

3\) Utilize o comando pip3 (e não pip) para instalar o virtualenv:  
    Digite: sudo pip3 install virtualenv  
    Repare no sudo! Queremos o virtualenv instalado para o computador
como um todo e não só para nosso projeto, então temos que ter permissões
para mexer na configuração geral do Python.

4\) No diretório do seu projeto, crie o ambiente virtual (virtualenv):  
     Digite: virtualenv env  
     Chamei o diretório de env, então sua pasta ficaria algo assim:  
                /qqcoisa/seuprojeto/env

5\) Ative o seu ambiente virtual:  
     Digite: . env/bin/activate  
     Repare o ponto (.) e o espaço. Eles são importantes! Você pode
trocar o ponto por source para ficar mais claro, se quiser.  
     (Alternativa): source env/bin/activate  
     Estou assumindo que você está na pasta do seu projeto, que chamei
antes de /qqcoisa/seuprojeto/.

6\) Pronto! Agora você já pode instalar módulos de python. Estou usando
Python 3, então usarei também o pip3. Faço assim:  
     Digite: pip3 install ipython  
     Esse ipython é o primeiro módulo que gosto de instalar. Ele deixa o
console do python mais amigável. Aí, ao invés de rodar "python" para
iniciar a console, uso "ipython". Teste aí!

Abraços,  
Otávio

