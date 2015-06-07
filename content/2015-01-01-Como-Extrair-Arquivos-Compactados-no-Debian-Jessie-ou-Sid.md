Title: Como Extrair Arquivos Compactados no Debian Jessie ou Sid
Date: 2015-01-01 11:43
Author: Otávio Carneiro
Slug: Como-Extrair-Arquivos-Compactados-no-Debian-Jessie-ou-Sid
Tags: debian, linux, xfce, jessie, tutorial

Hoje baixei um arquivo zip da internet e fiz o que seria natural, fui lá
na pasta, cliquei no arquivo com o botão direito e depois em "Extrair
aqui".

![]({filename}/images/thunar_extrair_aqui.png)

O que aconteceu? Nada! Uma mensagem de erro: "Falha ao extrair os
arquivos. Nenhum gerenciador de arquivos compactados localizado". Então
dei uma procurada na internet e encontrei esta solução.

![]({filename}/images/erro_nenhum_gerenciador_de_arquivos_compactados_localizado.png)

Como vocês sabem, estou utilizando o Debian Jessie (que um dia será o
Debian 8), que eu <span id="goog_2116862161"></span>[deixei mais
"bonitinho"<span
id="goog_2116862162"></span>](http://carneiro.blog.br/um/Deixando-o-Debian-XFCE-bonito-e-utiliz%C3%A1vel.html).
Se você estiver utilizando o Debian 7 (wheezy) na versão XFCE ou outra
distribuição que utilize o Thunar como gerenciador de arquivos (o
equivalente ao Windows Explorer), estas dicas também devem funcionar
para você.

Aparentemente, o tal "gerenciador de arquivos compactados" que eu
preciso é o pacote "file-roller". A dica para isso você encontra
procurando "thunar archive" no Gerenciador de Pacotes (synaptic).

[<img src="{filename}/images/thunar-archive-plugin.png" width="400">]({filename}/images/thunar-archive-plugin.png)

A descrição do thunar-archive-plugin diz claramente: "Este plugin
permite a extração e criação de arquivamentos de dentro do gerenciador
de arquivos Thunar. No momento ele usa o file-roller mas vai usar o
xarchiver no futuro."

Por alguma razão o file-roller não estava instalado no meu Linux. Eu
fuço tanto os pacotes que devo tê-lo desinstalado em algum momento.

Então, se você estiver tendo problemas para descompactar seus arquivos,
verifique se o pacote file-roller está instalado.

O pacote file-roller também explica bem claramente sua função:

[<img src="{filename}/images/file_roller-descricao.png" width="400">]({filename}/images/file_roller-descricao.png)

"File-roller é um gerenciador de arquivos para o ambiente GNOME. Com ele você pode:

 \* Criar e modificar conjuntos de arquivamentos.  
 \* Ver o conteúdo de um conjunto de arquivamentos.  
 \* Ver um arquivo contido em um conjunto de arquivamentos.  
 \* Extrair arquivos do conjunto de arquivamentos.

O file-roller suporta os seguintes formatos:  
 \* arquivamentos tar (.tar), incluindo aqueles comprimidos com gzip  
   (.tar.gz, .tgz), bzip (.tar.bz, .tbz), bzip2 (.tar.bz2, .tbz2),  
   compress (.tar.Z, .taz), lzip (.tar.lz, .tlz), lzop (.tar.lzo,
.tzo),  
   lzma (.tar.lzma) e xz (.tar.xz)  
 \* arquivamentos zip (.zip)  
 \* arquivamentos jar (.jar, .ear, .war)  
 \* arquivamentos 7z (.7z)  
 \* imagens de CD iso9660 (.iso)  
 \* arquivamentos lha (.lzh)  
 \* arquivamentos Archiver (.ar)  
 \* arquivamentos Comic book ("gibi") (.cbz)  
 \* arquivos individuais compactados com gzip (.gz), bzip (.bz), bzip2  
   (.bz2), compress (.Z), lzip (.lz), lzop (.lzo), lzma (.lzma) and xz  
   (.xz)

File-roller pode extrair os seguintes formatos:  
 \* arquivamentos Cabinet (.cab)  
 \* pacotes binários Debian (.deb)  
 \* arquivamentos Xar (.xar)

File-roller não realiza operações de compactação por si só, confiando em
ferramentas padrão para isto."

Esta última informação é importante. O file-roller descompacta todos
estes tipos de arquivo, desde que você tenha o descompactador apropriado
para eles. Então, se quiser descompactar um arquivo .zip, você tem que
ter o unzip, se quiser um .rar, tem que ter o unrar e por aí vai.

Se tiverem problemas de descompactação não mencionadas aqui, deixem um
comentário que tento complementar o post.

Abs!  
Otávio


