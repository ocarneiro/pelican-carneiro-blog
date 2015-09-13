Title: Criando um bitmap para LCD Gráfico
Date: 2014-01-27 16:23
Author: Otávio Carneiro
Slug: Criando-um-bitmap-para-LCD-Gráfico
Tags: arduino, diy, eletrônica, gimp, olho_de_lcd, projetos, tutorial


Há algum tempo comecei um projeto para fazer um olho de brinquedo usando
um LCD Gráfico Nokia 5110. A [primeira tentativa
falhou](http://umcarneiro.blogspot.com/2014/01/olho-de-lcd-com-arduino-e-nokia-5110.html),
mas depois entendi [como o display
funciona](http://umcarneiro.blogspot.com/2014/01/lcd-nokia-5110-com-arduino-sucesso.html).
Resta agora colocar o meu desenho nele.

Mas que desenho?

Pois bem, como é que você desenha algo para ficar bem em determinada
resolução? Eu tive que testar imprimindo uma grade na resolução do
display (84x48) para rabiscar em cima.  
[<img src="{filename}/images/old/shihtzu.jpg" width="140">]({filename}/images/old/shihtzu.jpg)
Claro que eu poderia criar uma imagem de 84 por 48 pixels e rabiscar no
computador, mas de que jeito minha filha e nossa cachorrinha
participariam do projeto?

<div align="center">

<iframe allowfullscreen frameborder="0" height="315" src="//www.youtube.com/embed/4Qzy9h_f8uA" width="560"></iframe>

</div>

Então, para permitir mais participação, criei a grade no computador e
imprimi para desenhar. Minha primeira escolha de software seria o
Inkscape, mas achei mais fácil fazer no Gimp.

A primeira coisa que descobri é que uma grade de 24 por 24 pixels
permite você numerar os quadrados numa boa, então usei esse tamanho.
Assim, minha imagem tinha que ter 24 vezes 84 de altura e 24 vezes 48 de
largura, o que dá 1152 x 2016 pixels.

[<img src="{filename}/images/old/gimp_filtro.png" width="480">]({filename}/images/old/gimp_filtro.png)
Com
a imagem no tamanho certo, basta criar a grade. Vá em:  
Filtros -\> Renderizar -\> Padrão -\> Grade

Achou o caminho estranho? Pois é, eu também achei...

Nas opções da grade você só precisa alterar os campos  de "Espaçamento".
O padrão é 16x16, mas eu usei 24x24, como mencionei acima.

[<img src="{filename}/images/old/foto_olho_grid.jpg" width="480">]({filename}/images/old/foto_olho_grid.jpg)
Salvei
um arquivo PNG e mandei imprimir a partir do visualizador de imagens.
Não sei se dava para imprimir direto do Gimp. Estou tão acostumado a
fazer desse jeito que nem tentei...

O resultado final está aí do lado. Talvez, se eu tivesse usado um
scanner, daria para pegar a imagem direto e redimensionar para 48x84 e
já jogar em um conversor de bitmap para bytes e partir para o abraço,
mas...

Não tenho um scanner e o [conversor de bitmaps indicado pela
Sparkfun](https://learn.sparkfun.com/tutorials/graphic-lcd-hookup-guide/example-code-2-drawing-bitmaps)
está fora do ar... Isso quer dizer que ainda terei mais algum trabalho
com esse projeto e que teremos mais posts no blog sobre o assunto.

Nos vemos em breve!

Você pode ver todas as etapas deste projeto usando [este
link](http://carneiro.blog.br/um/tag/olho_de_lcd.html), ou
clicando na tag "[olho\_de\_lcd](http://carneiro.blog.br/um/tag/olho_de_lcd.html)",
abaixo.

