Title: Como se faz um robô
Date: 2013-05-07 20:43
Author: Otávio Carneiro
Slug: Como-se-faz-um-robô

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-RY06qMRE1ko/UtWZqSYO6dI/AAAAAAAABpo/PG6LMOZM9TI/s320/WalkingBreadboard_bb.png)](http://2.bp.blogspot.com/-RY06qMRE1ko/UtWZqSYO6dI/AAAAAAAABpo/PG6LMOZM9TI/s1600/WalkingBreadboard_bb.png)

</div>

Você sabe o que é uma protoboard? Pois é, até uns dez dias atrás, eu
também não sabia. Quando descobri, achei que era algo tão legal que quis
arrumar um jeito de fazê-la andar... Esse post explica como eu consegui.

Uma protoboard é uma plaquinha de plástico, cheia de furinhos. O que a
torna importante é o que ela tem por dentro. Filosófico, não?

Dentro da protoboard, há ligações elétricas entre os buraquinhos do
meio, na vertical, e entre os buraquinhos das extremidades, na
horizontal, como nesse desenho:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------
  [![](http://4.bp.blogspot.com/-YMAdysNyEZs/UYm3sqrHcrI/AAAAAAAABQg/ZQ9faW1tn8o/s320/breadboard_bb.png)](http://4.bp.blogspot.com/-YMAdysNyEZs/UYm3sqrHcrI/AAAAAAAABQg/ZQ9faW1tn8o/s1600/breadboard_bb.png)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------

A vantagem disso é que, quando você quer fazer testes com componentes
eletrônicos ("**protó**tipos"), você não precisa ficar soldando ou
enroscando um fio no outro, basta plugá-los na sua placa ("**board**").

Ficou claro, então, que a protoboard, sozinha, não faz nada. Você
precisa ter um monte de componentes eletrônicos para fazer coisas
interessantes, como isso aqui:  

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------
  [![](http://3.bp.blogspot.com/-oqlwfnejzwY/UYm42Z3Ce-I/AAAAAAAABQs/5HOwCOzD02s/s320/DSC00688.JPG)](http://3.bp.blogspot.com/-oqlwfnejzwY/UYm42Z3Ce-I/AAAAAAAABQs/5HOwCOzD02s/s1600/DSC00688.JPG)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------

Neste meu robozinho, eu usei:

1.  Uma protoboard;
2.  Um Arduino Uno (uma plaquinha programável);
3.  Quatro (4) servo motores de 9g;
4.  Dois suportes para duas pilhas AA;
5.  Três pilhas AA;
6.  Vários jumpers (fios com conectores) coloridos;
7.  Vários pedaços de fio flexível;
8.  Fita isolante;
9.  Fita crepe.

<div>

</div>

<div>

Se vocês quiserem ver o robô em movimento, aqui está um vídeo:

</div>

<iframe allowfullscreen frameborder="0" height="315" src="http://www.youtube.com/embed/l9yK9NJLLkg" width="560"></iframe>

<div>

</div>

Para fazer isso tudo funcionar, vocês precisam conectar todos os
componentes de forma que o controlador do Arduino consiga dizer a todos
os motores como e quando se mexer. Eu usei servo motores, que são
motores muito usados em aeromodelismo. Em um motor comum, enquanto
houver energia, haverá movimento. Um servo motor pode ser controlado
para se mover de forma mais específica. Você pode dizer em que posição
ele deve ficar. No caso do meu robô, eu digo para cada perna ficar 90°
em relação ao chão e depois vou dizendo para cada uma delas ficar
paralela ao chão e depois perpendicular de novo, movimentando o robô.

Os servo motores que eu usei, no entanto, só giram 180°. Ou seja, cada
perna não pode dar uma volta completa, então cada perna tem que ir e
voltar. Para o robô não ficar indo e voltando sem sair do lugar, eu tive
que fazer um pé para ele. Cortei uma embalagem de plástico e dobrei para
ficar como um joelho. Ela dobra para trás para sair do caminho, mas fica
firme na frente para dar propulsão ao robô quando o motor desce. Prendi
essa pecinha com um arame que acabou ajudando mais ainda na propulsão. É
como se o robô estivesse de salto alto, tocando o salto primeiro no
chão. As analogias que eu tinha em mente eram muito mais másculas.
Pensei num elefante, ficou uma galinha. Funcionou melhor, na verdade.

Eu pluguei os servos de trás nos pinos 9 (esquerda) e 10 (direita) e os
da frente nos pinos 6 (esquerda) e 5 (direita). Estes pinos transmitem
um sinal modularizado. Eu ainda não sei bem o que é isso, mas o fato é
que esse sinal não é suficiente para energizar os motores. O arduino tem
saídas de 5V e 3,3V que até poderiam energizar os motores, mas são só
duas. Além disso, os motores usam muito energia e, ligados nessas
portas, fazem o arduino que ficar desligando por falta de força. Então
tive que colocar uma fonte extra de energia.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------
  [![](http://3.bp.blogspot.com/-vwrHWAAKV4I/UYnBAjjtSII/AAAAAAAABQ4/68z5QjORQ-A/s320/DSC00692.JPG)](http://3.bp.blogspot.com/-vwrHWAAKV4I/UYnBAjjtSII/AAAAAAAABQ4/68z5QjORQ-A/s1600/DSC00692.JPG)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------

Eu tinha aqui 3 pilhas novas e dois suportes para 2 pilhas AA cada. Até
pensei em sair para comprar mais pilhas, mas resolvi usar só as três
mesmo. Se até 3,3V já movem o motor, 4,5V devia funcionar, pensei. E
funcionou. Um dos suportes ficou capenga, com uma pilha só, então
enrolei um fio no negativo dessa ~~filha~~ pilha única e liguei direto
na protoboard.

De forma bem esquemática, as ligações ficaram assim:  

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------
  [![](http://2.bp.blogspot.com/-RY06qMRE1ko/UtWZqSYO6dI/AAAAAAAABpo/PG6LMOZM9TI/s320/WalkingBreadboard_bb.png)](http://2.bp.blogspot.com/-RY06qMRE1ko/UtWZqSYO6dI/AAAAAAAABpo/PG6LMOZM9TI/s1600/WalkingBreadboard_bb.png)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------

O Fritzing, programa que usei para desenhar, não tem um desenhinho de
suporte de pilha capenga, mas você pode usar três ou quatro pilhas.

Uma coisa importante a se notar é que, mesmo não usando o Arduino como
fonte de energia, você precisa conectar o negativo das suas pilhas ao
negativo dele, pois só assim a corrente elétrica pode sair dele e chegar
até os motores.

Espero ter conseguido explicar em linhas gerais como conectar múltiplos
servo motores ao Arduino. Se tiverem mais dúvidas, deixem nos
comentários que eu vou tentando explicar.

Quem leu até aqui pode se interessar em saber que não precisava ter lido
nada, pois eu fiz um segundo vídeo explicando essas mesmas coisas...

<iframe allowfullscreen frameborder="0" height="315" src="http://www.youtube.com/embed/lPyDKXwFK4U" width="560"></iframe>
E quem resolver tentar fazer em casa, vai precisar do código para rodar
no Arduino, então vou colá-lo aqui embaixo. Fiquem à vontade para usar o
código, os desenhos, os vídeos e as fotos desse post como quiserem, só
não me responsabilizem pelo que vier a dar errado.

Abraços,

Otávio

``` {style="background-color: #eeeeee; border: 1px dashed #999999; color: black; font-family: Andale Mono, Lucida Console, Monaco, fixed, monospace; font-size: 12px; line-height: 14px; overflow: auto; padding: 5px; width: 100%;"}
// Walking Breadboard / Protoboard Ambulante// by Otavio Carneiro dos Santos // based on Sweep, by BARRAGAN (example in Arduino)// This code is in the public domain.#include   Servo pataEsquerdaTras;Servo pataEsquerdaFrente;Servo pataDireitaTras;Servo pataDireitaFrente;int pos = 0;    //variavel temporaria                //guarda a posicao atual do servo void setup() {   pataEsquerdaTras.attach(9);  pataDireitaTras.attach(10);  pataEsquerdaFrente.attach(6);  pataDireitaFrente.attach(5);}   void loop() {   movePataEsquerdaParaFrente(pataEsquerdaTras);  movePataEsquerdaParaTras(pataEsquerdaTras);  delay(1000);  movePataDireitaParaFrente(pataDireitaFrente);  movePataDireitaParaTras(pataDireitaFrente);  delay(1000);  movePataEsquerdaParaFrente(pataEsquerdaFrente);  movePataEsquerdaParaTras(pataEsquerdaFrente);  delay(1000);  movePataDireitaParaFrente(pataDireitaTras);  movePataDireitaParaTras(pataDireitaTras);  delay(1000);} //move o servo esquerdo informado para frente//nota: os servos do lado esquerdo ficam espelhados em relacao//      aos do lado direito, por isso ha metodos distintos//      para cada lado.void movePataEsquerdaParaTras(Servo servoToMove){  int posInicial = 1;  int posFinal = 90;   for(pos = posInicial; pos < posFinal; pos += 1)   {                                      servoToMove.write(pos);              delay(15);  } }void movePataEsquerdaParaFrente(Servo servoToMove){  int posInicial = 1;  int posFinal = 90;   for(pos = posFinal; pos>=posInicial; pos-=1)   {                                    servoToMove.write(pos);    delay(15);  } }void movePataDireitaParaTras(Servo servoToMove){  int posInicial = 90;  int posFinal = 180;   for(pos = posFinal; pos>=posInicial; pos-=1)  {                                    servoToMove.write(pos);    delay(15);  } }void movePataDireitaParaFrente(Servo servoToMove){  int posInicial = 90;  int posFinal = 180;   for(pos = posInicial; pos < posFinal; pos += 1)  {                                      servoToMove.write(pos);    delay(15);  } }
```

<div class="separator" style="clear: both; text-align: center;">

</div>
