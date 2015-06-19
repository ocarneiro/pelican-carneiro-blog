Title: Como iniciar um script em Python 3
Date: 2015-06-12 23:52
Author: Otávio Carneiro
Slug: Como-iniciar-um-script-em-Python-3
Tags: python

    Spoiler alert! 
    #! /usr/bin/env python3

Para escrever um script python, você pode abrir um arquivo texto e sair escrevendo o código, sem nenhuma preocupação adicional. 

Ok, então para que estou escrevendo este post?

É que para que seu script rode usando o Python 3, você tem que usar uma anotação especial no início do código.

Muita gente já escreveu sobre a diferença entre Python 2 e Python 3. Talvez eu escreva sobre isso um dia e coloque um link aqui, mas por enquanto vou deixar vocês procurarem na internet.

Quando você grava um arquivo .py, o torna executável (chmod +x) e coloca ele no path, você pode rodá-lo simplesmente clicando duas vezes sobre ele ou chamando-o pelo nome. 

O meu problema até aqui é que, ao fazer isso, o código roda com o interpretador padrão do computador, que é quase sempre o Python 2. 

Eu quero ser um cara moderninho e aprender Python já na versão 3. Então quero que meus scripts rodem nesta versão. 

Ok, me convenceu! #comofas?!

Para seu script ser executado pelo interpretador Python 3 você tem que colocar uma anotação especial no começo do arquivo, conhecida como shebang. 

Tipo aquela música do Ricky Martin? ("She bangs, she bangs!") 

É, tipo isso.

Shebang é uma forma "carinhosa" de se chamar a junção do caracter cerquilha (ou hash, "#") e uma exclamação (bang, "!"). Hashbang é a junção dos dois nomes, mas o termo evoluiu para shebang, que é mais fácil de pronunciar.

Pois bem, o shebang que você vai usar para o Python 3 é o seguinte:

    :::python
    #! /usr/bin/env python3

Você mesmo pode experimentar o que isso faz. Escreva aí no seu terminal linux:

    env python
    
Você vai ver que o computador iniciou o ambiente Python 2:

    Python 2.7.9 (default, Mar  1 2015, 12:57:24) 
    [GCC 4.9.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Agora tente o mesmo com Python 3:

    env python3
    
    Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
    [GCC 4.9.1] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

O shebang (#!) indica para o computador que aquela linha (a primeira) vai dizer com que programa interpretar o script.

O /usr/bin/env é o comando para dizer ao computador que ele deve procurar um executável com o nome que virá a seguir.

E python3 é o interpretador que você quer.

Não foi fácil?

Abraço!  
Otávio
