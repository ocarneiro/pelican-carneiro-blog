Title: LCD Nokia 5110 com Arduino #sucesso
Date: 2014-01-16 18:35
Author: Otávio Carneiro
Slug: 2014-01-16-LCD-Nokia-5110-com-Arduino-sucesso
Tags: arduino, diy, olho_de_lcd, projetos, robótica, tutorial

No meu [post
anterior](http://carneiro.blog.br/um/2014-01-07-Olho-de-LCD-com-Arduino-e-Nokia-5110-fail.html)
eu falei que comprei um display LCD Nokia 5110 no
[MercadoLivre](http://lista.mercadolivre.com.br/_CustId_63284628) e,
inicialmente não consegui fazê-lo funcionar... Depois eu atualizei o
post dizendo que ele funcionou e fiquei de dar mais detalhes depois.
Bom, aqui estão os detalhes!

[<img src="{filename}/images/old/datasheet_display.jpg" width="480">]({filename}/images/old/datasheet_display.jpg)

Apesar de todo mundo se referir ao display como Nokia 5110, a parte
importante para conhecer é o controlador que ele tem dentro, que na
verdade é feito pela Philips! O controlador/driver é um Philips PCD8544.

O
[datasheet](https://www.sparkfun.com/datasheets/LCD/Monochrome/Nokia5110.pdf)dele
é bem extenso (32 páginas), mas você não precisa se preocupar, está numa
linguagem bem acessível e tem até um exemplo de como desenhar uma
palavra na tela, mostrando o que você deve enviar, bit a bit (página
22).

[<img src="{filename}/images/old/workspace.jpg" width="480">]({filename}/images/old/workspace.jpg)

Para tentar entender o funcionamento do módulo, imprimi as páginas 14 e
22 e ainda montei uma "cola" para anotar o que [cada byte representava
em
bits](http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html).

[<img src="{filename}/images/old/Contraste600.gif" width="480">]({filename}/images/old/Contraste600.gif) O
problema que eu estava tendo com este módulo parecia estar na definição
do contraste, então criei o código abaixo para vocês testarem o módulo
de vocês. O que ele faz é desenhar uma barra que vai crescendo a medida
que o contraste vai aumentando.

Este gif animado dá uma ideia do resultado. O contraste ideal é aquele
em que a barra fica bem escura sobre um fundo claro. Se o fundo do seu
LCD escurecer, é porque você passou da conta e deve diminuir um
pouquinho.


    //Controlador de Display LCD Nokia 5110 (84x48 pixels)
    //em 13 de janeiro de 2014
    //Mais informacoes: umcarneiro.blogspot.com
    //Licenca: MIT (use como quiser!)

    //Pinos utilizados no arduino
    #define PIN_SCE   7  //pino 2 do display
    #define PIN_RESET 6  //pino 1 do display
    #define PIN_DC    5  //pino 3 do display
    #define PIN_SDIN  4  //pino 4 do display
    #define PIN_SCLK  3  //pino 5 do display

    //Tamanho do LCD em pixels:
    #define LCD_X     84
    #define LCD_Y     48

    //Estas variaveis restringem o menor e o maior contraste a ser 
    // testado
    //Se sua tela estiver muito escura desde o inicio do teste, 
    // diminua este valor
    const int MIN_CONTRAST = 175; //tem que ser maior que 128
    //Se sua tela estiver muito clara no fim do teste, 
    // aumente este valor
    const int MAX_CONTRAST = 200; //tem que ser menor que 255


    void setup(void)
    {
      pinMode(PIN_SCE, OUTPUT);   // Inicializa os pinos...
      pinMode(PIN_RESET, OUTPUT);
      pinMode(PIN_DC, OUTPUT);
      pinMode(PIN_SDIN, OUTPUT);
      pinMode(PIN_SCLK, OUTPUT);
      digitalWrite(PIN_RESET, LOW); //RESET no controlador
      digitalWrite(PIN_RESET, HIGH);
      LcdWrite(LOW, 0x21 );  // Function set: PD=0 (On); 
                             // V=0 (Horizontal); 
                             // H=1 (Extended instruction set)
      LcdWrite(LOW, 0xBA );  // Define o LCD Vop (Contraste). 
                             //XXXXXXXXXXXXXXX
      LcdWrite(LOW, 0x04 );  // Define o coeficiente de 
                             //  temperatura (??)
      LcdWrite(LOW, 0x14 );  // LCD bias mode 1:48  (??)
      LcdWrite(LOW, 0x20 );  // Function set: PD=0 (On); 
                             // V=0 (Horizontal); 
                             // H=0 (Basic instruction set)
      LcdWrite(LOW, 0x0C );  // Display control = 10 (Normal)
      
      //Clear - apaga todas as posicoes
      for (int index = 0; index < LCD_X * LCD_Y / 8; index++)
      {
        LcdWrite(HIGH, 0x00); //bit 0 em todo mundo!
      }

    }

    //Cuida da burocracia: 
    //envia o comando ou dado seguindo 
    // o protocolo do chip
    void LcdWrite(byte dc, byte data)
    {
      //define se vai mandar dado ou comando
      digitalWrite(PIN_DC, dc); 
      //ativa o chip para receber dados
      digitalWrite(PIN_SCE, LOW); 
      //envia um bit de cada vez, comecando pela esquerda
      shiftOut(PIN_SDIN, PIN_SCLK, MSBFIRST, data); 
      //desativa o envio de dados
      digitalWrite(PIN_SCE, HIGH); 
    }

    //desenha uma barra repetindo o byte informado
    void desenhaBarra(int largura, byte caracter)  
    {
      //Coloca o cursor no local correto
      LcdWrite( 0, 0x80 | 0);  // Coluna 0
      LcdWrite( 0, 0x40 | 2);  // Linha 2

      //barra horizontal
      for (int index = 0; index < largura; index++)
      {
        LcdWrite(HIGH, caracter);
      }
    }

    void loop(void)
    {  
      //dentro dos limites que estabelecemos, 
      // define o contraste a mostrar
      for (int contrast = MIN_CONTRAST; 
               contrast < MAX_CONTRAST; 
               contrast++)
      {  
        // Function set: PD=0 (On); 
        //               V=0 (Horizontal); 
        //               H=1 (Extended instruction set)
        LcdWrite(LOW, 0x21 );  
        // Define o contraste (VOP)
        LcdWrite(LOW, contrast );  
        
        //define a largura da barra 
        // proporcional ao contraste
        int largura = map(contrast, MIN_CONTRAST, 
                          MAX_CONTRAST, 0, LCD_X); 

        // Function set: PD=0 (On); 
        //  V=0 (Horizontal); 
        //  H=0 (Basic instruction set)
        LcdWrite(LOW, 0x20 );  
        // Display control = 10
        LcdWrite(LOW, 0x0C );  
      
        //desenha a barra horizontal 
        // na largura que definimos
        desenhaBarra(largura, 0x7f);
        //dah um tempo para podermos 
        // ver o resultado
        delay(350); 
      }
      
      //desenha uma barra invisivel 
      // da largura da tela
      // ou seja, apaga a barra!
      desenhaBarra(LCD_X, 0x00); 
    }

Juro que este foi o código mais simples que eu consegui fazer! Enchi de
comentários para ver se conseguia torná-lo inteligível. Defini o
contraste usando números decimais de propósito, para facilitar a
leitura.  Tem um ótimo conversor de números entre binário, decimal e
hexa [nesta
página](http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html).
Eu usei um bocado para tentar entender o que estava acontecendo.

O circuito ficou assim:

[<img src="{filename}/images/old/Nokia5110contraste_bb.png" width="480">]({filename}/images/old/Nokia5110contraste_bb.png)

  ------------------ ------------------ ------------------ ------------------
  Pino LCD           1-RST              2-CE               3-DC
  Resistor           10k                10k                10k
  Arduino            Pino 6             Pino 7             Pino 5
  Cor                Vermelho           Azul               Amarelo
  ------------------ ------------------ ------------------ ------------------

O código que eu tinha usado [da outra
vez](http://carneiro.blog.br/um/2014-01-07-Olho-de-LCD-com-Arduino-e-Nokia-5110-fail.html)
usava, obrigatoriamente os pinos 11 e 13, mas este é mais simples e não
tem essa exigência.

Repare também que o backlight (pino 7 do LCD) foi para o GND. Confesso
que não entendi bem a lógica disso, já que o backlight se acende quando
colocamos +3V direto no pino 7 e GND no pino 8.

[<img src="{filename}/images/old/foto_circuito_completo_nokia5110.jpg" width="480">]({filename}/images/old/foto_circuito_completo_nokia5110.jpg)

O desenho do módulo de LCD no Fritzing eu fiz por conta própria. Se
quiser o arquivo ou aprender a fazer você mesmo, leia [este outro
post](http://carneiro.blog.br/um/2014-01-10-como-criar-um-componente-para-o-fritzing.html).

Espero que vocês consigam colocar as suas telinhas para funcionar!

Quem sabe em um próximo post a minha já terá virado um olho de
brinquedo?

Aguardem!

UPDATE (em 27/01/2014): Desenhei o olho para colocar no LCD. Vejam
[neste outro
post](http://carneiro.blog.br/um/2014-01-27-Criando-um-bitmap-para-LCD-Grafico.html).

Você pode ver todas as etapas deste projeto usando [este
link](http://carneiro.blog.br/um/tag/olho_de_lcd.html), ou
clicando na tag "[olho\_de\_lcd](http://carneiro.blog.br/um/tag/olho_de_lcd.html)",
abaixo.

