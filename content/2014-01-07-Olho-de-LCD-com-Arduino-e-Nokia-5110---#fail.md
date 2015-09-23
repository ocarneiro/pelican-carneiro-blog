Title: Olho de LCD com Arduino e Nokia 5110 - #fail
Date: 2014-01-07 19:54
Author: Otávio Carneiro
Slug: 2014-01-07-Olho-de-LCD-com-Arduino-e-Nokia-5110-fail
Tags: arduino, diy, olho_de_lcd, projetos, robótica, tutorial

Minha filha tem um brinquedo com olhos muito expressivos feitos de LCD,
vejam:

[<img src="{filename}/images/old/olhos.jpg" width="480">]({filename}/images/old/olhos.jpg)

Eu fiquei tão fascinado por estes olhos que quis reproduzí-los com o
Arduino, então comprei um display LCD Nokia 5110.

Para este projeto, contei com a colaboração da dona do brinquedo:

[<img src="{filename}/images/old/lcd_2carneiros.gif" width="480">]({filename}/images/old/lcd_2carneiros.gif)

ATENÇÃO: Se você é fã dos
[2Carneiros](http://carneiro.blog.br/2/)
e esperava encontrar aqui um vídeo nosso montando o projeto, você não
precisa ler mais nada. Vá direto aos comentários e peça um vídeo, aqui
eu só postei esse gif animado. Se isso não resolver, se inscreva no blog
e no canal do YouTube, peça pelo Facebook, me aborde na rua ou xingue
muito no Twitter. O resto deste post é para as pessoas interessadas em
Arduino e afins.

 O [display que
comprei](http://produto.mercadolivre.com.br/MLB-532916208-modulo-arduino-display-lcd-grafico-84x48-nokia-5110-pic-avr-_JM?redirectedFromParent=MLB521625799)
vem em um mini kit feito de uma tela de LCD com uma moldura que o fixa
em uma placa de circuito (breakout board). Esta placa tem furos
identificados de 1 a 8 na frente e por suas funções, no verso. Nestes
furos você pode soldar uma barra de pinos (fornecida no kit).

[<img src="{filename}/images/old/produto_lcd_nokia.jpg" width="480">]({filename}/images/old/produto_lcd_nokia.jpg)

[<img src="{filename}/images/old/verso.jpg" width="480">]({filename}/images/old/verso.jpg)

[<img src="{filename}/images/old/terceira_mao.jpg" width="480">]({filename}/images/old/terceira_mao.jpg)

Para soldar os pinos na placa eu usei um conector jacaré para segurá-los
no lugar e uma terceira mão para manter uma altura confortável. Depois
de soldar os pinos no lugar, você já pode encaixar o seu display na
breadboard.

Como as indicações das funções dos pinos ficam no verso, recomendo você
anotar em um papel para deixar à mão. Isso vai te poupar de ficar
virando o display de um lado para o outro enquanto monta o circuito.

[<img src="{filename}/images/old/breadboard.jpg" width="480">]({filename}/images/old/breadboard.jpg)

Existem muitas referências na internet de como utilizar esse display de
LCD. Eu utilizei as orientações da página da
[Sparkfun](https://learn.sparkfun.com/tutorials/graphic-lcd-hookup-guide/hardware-assembly--hookup).

Se for utilizar a mesma referência, você deve ficar atento para a
localização dos pinos. O produto que você comprou pode ter pinos em
locais diferentes do que os do produto da Sparkfun.

No meu caso, fazendo as devidas substituições, ficou assim:

[<img src="{filename}/images/old/arduino-foto.jpg" width="480">]({filename}/images/old/arduino-foto.jpg)

[<img src="{filename}/images/old/breadboard-foto.jpg" width="480">]({filename}/images/old/breadboard-foto.jpg)

[<img src="{filename}/images/old/nokia_lcd_bb.png" width="480">]({filename}/images/old/nokia_lcd_bb.png)

  ------------------ ------------------ ------------------ ------------------
  Pino LCD           1-RST              2-CE               3-DC
  Resistor           10k                1k                 10k
  Arduino            Pino 6             Pino 7             Pino 5
  Cor                Vermelho           Azul               Amarelo
  ------------------ ------------------ ------------------ ------------------

Indiquei as cores só para facilitar o entendimento da foto e do esquema
que desenhei no Fritzing. Se for fazer em casa, use a cor que quiser.

Baixei o [código
sugerido](https://dlnmh9ip6v2uc.cloudfront.net/tutorialimages/GraphicLCDNokia3310/nokia_5100_r03.zip)
na página da Sparkfun, compilei, subi para o arduino e... nada!

Mentira, o backlight acendeu. E para minha surpresa, ele era azul! Não
sei por que, mas achei que seria branco.

O display de LCD deveria ter mostrado várias animações bacanas e até uma
chargezinha, mas não vi nada disso.

E aí, desisto?

Ainda não, estou conversando sobre garantia com o fornecedor da peça. Se
eu conseguir uma reposição, posto aqui o resultado. Se não, vou recorrer
aos chineses...

Aguardem cenas do próximo episódio!

**UPDATE** (em 10/01/2014): O fornecedor do display ([EletroKits, no
MercadoLivre](http://lista.mercadolivre.com.br/_CustId_63284628)) foi
muito atencioso e me mandou uma foto do circuito que ele fez para testar
a peça e até um código de teste personalizado, que me permitiu fazer a
peça funcionar. Vejam:

[<img src="{filename}/images/old/funciona.jpg" width="480">]({filename}/images/old/funciona.jpg)

UPDATE (em 16/01/2014) Documentei melhor para mostrar para vocês [neste
post](http://carneiro.blog.br/um/2014-01-16-LCD-Nokia-5110-com-Arduino-sucesso.html).

UPDATE (em 27/01/2014): Desenhei o olho para colocar no LCD. Vejam
[neste outro
post]((http://carneiro.blog.br/um/2014-01-27-Criando-um-bitmap-para-LCD-Grafico.html).

Você pode ver todas as etapas deste projeto usando [este
link](http://carneiro.blog.br/um/tag/olho_de_lcd.html), ou
clicando na tag "[olho\_de\_lcd](http://carneiro.blog.br/um/tag/olho_de_lcd.html)",
abaixo.

