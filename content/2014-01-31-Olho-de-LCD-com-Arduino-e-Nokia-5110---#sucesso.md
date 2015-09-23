Title: Olho de LCD com Arduino e Nokia 5110 - #sucesso
Date: 2014-01-31 17:26
Author: Otávio Carneiro
Slug: 2014-01-31-Olho-de-LCD-com-Arduino-e-Nokia-5110-sucesso
Tags: arduino, diy, olho_de_lcd, projetos, robótica, tutorial

E... voilá!!

[<img src="{filename}/images/old/DSC02797.JPG" width="480">]({filename}/images/old/DSC02797.JPG)



Consegui fazer o Olho de LCD usando um [display Nokia
5110](http://carneiro.blog.br/um/2014-01-16-LCD-Nokia-5110-com-Arduino-sucesso.html).
e o Arduino!!!







[<img src="{filename}/images/old/DSC02796.JPG" width="480">]({filename}/images/old/DSC02796.JPG)



De início eu havia pensado em gerar um arquivo bitmap (BMP) e
convertê-lo depois em código usando uma ferramenta automatizada. Ou pelo
menos foi o que eu escrevi que ia fazer [no meu último
post](http://umcarneiro.blogspot.com/2014/01/criando-um-bitmap-para-lcd-grafico.html)...

Acabei fazendo uma coisa bem <span
style="font-family: inherit;">dif</span>erente... Foi um trabalho mais
braçal, mas deu certo.

[<img src="{filename}/images/old/DSC02794.JPG" width="480">]({filename}/images/old/DSC02794.JPG)Primeiro,
marquei com uma canetinha vermelha as divisas das linhas do display, a
cada 8 quadradinhos. O display recebe os dados a exibir na forma de
bytes. Cada byte contém oito bits, então os dados chegam ao display na
forma de linhas com oito bits de espessura. Foram essas linhas que
marquei.

Para cada um<span style="font-size: small;"><span
style="font-family: Times,&quot;Times New Roman&quot;,serif;">a
das</span></span> 6 linhas, montei uma sequência de bytes. Para ficar
bem claro no código, escrevi os bytes usando o sistema binário, assim:

    :::arduino
    0b00000000 //uma linha em branco
    0b11111111 //uma linha preta

O "0b" no início diz ao Arduino que estou usando o sistema binário, ou
seja, só zeros e uns.<span style="font-size: small;"><span
style="font-family: Georgia,&quot;Times New Roman&quot;,serif;">  
</span></span>Tive que escrever o correspondente de 0 ou 1 para cada
quadradinho da grade que forma o display. Ou seja, 84 x 48 = 4032. Claro
que usei um bocado de Ctrl + C, Ctrl + V e escrevi em linhas de 8 bits,
então foram apenas 504 linhas de código para descrever o desenho... ;)O
código inteiro está aí embaixo, usem à vontade!



[<img src="{filename}/images/old/DSC02793.JPG" width="480">]({filename}/images/old/DSC02793.JPG)



Se fizerem melhorias para ele olhar para os lados, piscar, etc, por
favor compartilhem! Eu quero fazer isso também, mas se forem mais
rápidos que eu, vai me poupar um bocado de trabalho!

Abraços!

    :::arduino
    //Olho de LCD - v1
    //Controlador de Display LCD Nokia 5110 (84x48 pixels)
    //em 31 de janeiro de 2014
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

    byte linhaUm[84] = {
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //5
          0b00000000,
          0b00000001,
          0b00000010,
          0b00000100,
          0b00000100,  //10
          0b00001000,
          0b00001000,
          0b00010000,
          0b00100000,
          0b00100000,  //15
          0b00100000,
          0b01000000,
          0b01000000,
          0b01000000,
          0b01000000,  //20
          0b01000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //25
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //30
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //35
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //40
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //45
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //50
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //55
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,  //60
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b01000000,  //65
          0b01000000,
          0b00100000,
          0b00100000,
          0b00010000,
          0b00010000,  //70
          0b00001000,
          0b00001000,
          0b00000100,
          0b00000010,
          0b00000010,  //75
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //80
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000
    };

    byte linhaDois[84] = {
          0b00000000,
          0b00000011,
          0b00001100,
          0b00110000,
          0b01000000,  //5
          0b10000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //10
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //15
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //20
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //25
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //30
          0b00000000,
          0b00000000,
          0b00000001,
          0b00000011,
          0b00000111,  //35
          0b00000111,
          0b00001111,
          0b00001111,
          0b00001110,
          0b00011110,  //40
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,  //45
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,  //50
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,
          0b00011111,  //55
          0b00011111,
          0b00011111,
          0b00011111,
          0b00001111,
          0b00001111,  //60
          0b00001111,
          0b00001111,
          0b00001111,
          0b00001111,
          0b00000111,  //65
          0b00000111,
          0b00000011,
          0b00000001,
          0b00000000,
          0b00000000,  //70
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //75
          0b00000000,
          0b10000000,
          0b01000000,
          0b00100000,
          0b00010000,  //80
          0b00001000,
          0b00000110,
          0b00000001,
          0b00000000
    };

    byte linhaTres[84] = {
          0b11111111,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //5
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //10
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //15
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //20
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //25
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00001111,  //30
          0b00111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //35
          0b10001111,
          0b00000111,
          0b00000111,
          0b00000011,
          0b00000011,  //40
          0b00000011,
          0b00000111,
          0b00001111,
          0b11111111,
          0b11111111,  //45
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //50
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //55
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //60
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //65
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b00111111,  //70
          0b00001111,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //75
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //80
          0b00000000,
          0b00000000,
          0b10000000,
          0b01111111
    };

    byte linhaQuatro[84] = {
          0b11111000,
          0b00000110,
          0b00000001,
          0b00000000,
          0b00000000,  //5
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //10
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //15
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //20
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //25
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b11100000,  //30
          0b11111000,
          0b11111100,
          0b11111111,
          0b11111111,
          0b11111111,  //35
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //40
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //45
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //50
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //55
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,  //60
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111001,
          0b11111001,  //65
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111110,  //70
          0111111000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //75
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //80
          0b00000000,
          0b00000000,
          0b00001111,
          0b11110000
    };

    byte linhaCinco[84] = {
          0b00000000,
          0b00000000,
          0b00000000,
          0b11000000,
          0b00110000,  //5
          0b00001100,
          0b00000010,
          0b00000001,
          0b00000000,
          0b00000000,  //10
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //15
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //20
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //25
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //30
          0b00000000,
          0b00000000,
          0b00000000,
          0b10000000,
          0b11000000,  //35
          0b11000000,
          0b11100000,
          0b11100000,
          0b11110000,
          0b11110000,  //40
          0b11110000,
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,  //45
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,  //50
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,  //55
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,
          0b11111000,  //60
          0b11110000,
          0b11110000,
          0b11110000,
          0b11110000,
          0b11100000,  //65
          0b11100000,
          0b11000000,
          0b11000000,
          0b10000000,
          0b00000000,  //70      
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //75
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000011,
          0b00000100,  //80
          0b00011000,
          0b01100000,
          0b10000000,
          0b00000000
    };

    byte linhaSeis[84] = {
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,  //5
          0b00000000,
          0b00000000,
          0b00000000,
          0b10000000,
          0b01000000,  //10
          0b00100000,
          0b00010000,
          0b00010000,
          0b00001000,
          0b00001000,  //15
          0b00001000,
          0b00000100,
          0b00000100,
          0b00000100,
          0b00000010,  //20
          0b00000010,
          0b00000010,
          0b00000010,
          0b00000010,
          0b00000001,  //25
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //30
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //35
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //40
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //45
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //50
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //55
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000001,  //60
          0b00000001,
          0b00000001,
          0b00000001,
          0b00000010,
          0b00000010,  //65
          0b00000010,
          0b00000010,
          0b00000010,
          0b00000010,
          0b00000100,  //70
          0b00000100,
          0b00000100,
          0b00001000,
          0b00010000,
          0b00100000,  //75
          0b00100000,
          0b01000000,
          0b10000000,
          0b00000000,
          0b00000000,  //80
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000
    };

    void setup(void)
    {
      pinMode(PIN_SCE, OUTPUT);   // Inicializa os pinos...
      pinMode(PIN_RESET, OUTPUT);
      pinMode(PIN_DC, OUTPUT);
      pinMode(PIN_SDIN, OUTPUT);
      pinMode(PIN_SCLK, OUTPUT);
      digitalWrite(PIN_RESET, LOW); //RESET no controlador
      digitalWrite(PIN_RESET, HIGH);
      LcdWrite(LOW, 0x21 );  // Function set: PD=0 (On); V=0 (Horizontal); H=1 (Extended instruction set)
      LcdWrite(LOW, 0xBA );  // Define o LCD Vop (Contraste). //XXXXXXXXXXXXXXX
      LcdWrite(LOW, 0x04 );  // Define o coeficiente de temperatura (??)
      LcdWrite(LOW, 0x14 );  // LCD bias mode 1:48  (??)
      LcdWrite(LOW, 0x20 );  // Function set: PD=0 (On); V=0 (Horizontal); H=0 (Basic instruction set)
      LcdWrite(LOW, 0x0C );  // Display control = 10 (Normal)
      
      limpaTela();
      
      desenhaLinha(linhaSeis);
      desenhaLinha(linhaCinco);
      desenhaLinha(linhaQuatro);
      desenhaLinha(linhaTres);
      desenhaLinha(linhaDois);
      desenhaLinha(linhaUm);   
    }
      
    void limpaTela(void) {
      //Percorre todas as posicoes
      for (int index = 0; index < LCD_X * LCD_Y / 8; index++)
      {
        LcdWrite(HIGH, 0);
      }
    }

    void desenhaLinha(byte linha[]) {
      //Percorre as colunas
      for (int coluna = 0; coluna < LCD_X; coluna++)
      {
        LcdWrite(HIGH, linha[coluna]);
      }
    }


    //Cuida da burocracia: envia o comando ou dado seguindo o protocolo do chip
    void LcdWrite(byte dc, byte data)
    {
      digitalWrite(PIN_DC, dc); //define se vai mandar dado ou comando
      digitalWrite(PIN_SCE, LOW); //ativa o chip para receber dados
      shiftOut(PIN_SDIN, PIN_SCLK, MSBFIRST, data); //envia um bit de cada vez, comecando pela esquerda
      digitalWrite(PIN_SCE, HIGH); //desativa o envio de dados
    }

    void loop(void)
    {  
      //nada
    }


Você pode ver todas as etapas deste projeto usando [este
link](http://carneiro.blog.br/um/tag/olho_de_lcd.html), ou
clicando na tag "[olho\_de\_lcd](http://carneiro.blog.br/um/tag/olho_de_lcd.html)",
abaixo.

