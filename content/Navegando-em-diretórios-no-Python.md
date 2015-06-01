Title: Navegando em diretórios no Python
Date: 2015-05-17 17:39
Author: Otávio Carneiro
Slug: Navegando-em-diretórios-no-Python

Para identificar o diretório atual (pwd):  
    import os  
    os.getcwd() \# cwd = current working directory

Para mudar de diretório (cd):  
    import os  
    path = '/my/path/'  
    os.chdir(path)

Para listar o conteúdo (ls):  
    import os  
    os.listdir() \#retorna um objeto do tipo list (lista), claro!


