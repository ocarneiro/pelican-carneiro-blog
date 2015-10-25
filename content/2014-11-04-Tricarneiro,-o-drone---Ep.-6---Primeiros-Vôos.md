Title: Tricarneiro, o drone - Ep. 6 - Primeiros Vôos
Date: 2014-11-04 16:52
Author: Otávio Carneiro
Slug: Tricarneiro-o-drone-Ep-6-Primeiros-Voos
Tags: tricarneiro, drone, tutorial

Pessoal,

Depois de muita luta, finalmente consegui fazer o Tricarneiro (meu
tricóptero) voar bem! Vejam aí!

<iframe allowfullscreen frameborder="0" height="270" src="https://www.youtube.com/embed/S-g4FcGZLbM?list=UUgP9UJRSxYe687HhHYsBwYA" width="480"></iframe>  
Ver direto no YouTube:
<http://youtu.be/S-g4FcGZLbM?list=UUgP9UJRSxYe687HhHYsBwYA>

Para conseguir fazer isso, esta é a configuração que fiz na placa KK2.1:

[<img src="{filename}/images/tri6/DSC03713.JPG" width="480">]({filename}/images/tri6/DSC03713.JPG)

[<img src="{filename}/images/tri6/DSC03714.JPG" width="480">]({filename}/images/tri6/DSC03714.JPG)

###PI Editor  
    Axis: Roll (Aileron)  
    P Gain: 35  
    P Limit: 100  
    I Gain: 25  
    I Limit: 20

[<img src="{filename}/images/tri6/DSC03715.JPG" width="480">]({filename}/images/tri6/DSC03715.JPG)

###PI Editor  
    Axis: Pitch (Elevator) - Profundor(?)  
    P Gain: 35  
    P Limit: 100  
    I Gain: 25  
    I Limit: 20  

[<img src="{filename}/images/tri6/DSC03716.JPG" width="480">]({filename}/images/tri6/DSC03716.JPG)

###PI Editor  
    Axis: Yaw (Rudder) - Leme  
    P Gain: 15  
    P Limit: 80  
    I Gain: 20  
    I Limit: 20

[<img src="{filename}/images/tri6/DSC03717.JPG" width="480">]({filename}/images/tri6/DSC03717.JPG)

[<img src="{filename}/images/tri6/DSC03719.JPG" width="480">]({filename}/images/tri6/DSC03719.JPG)

###Mode Settings  
    Self-Level: AUX (Channel 5)  
    Link Roll Pitch: Yes  
    Auto Disarm: Yes  
    CPPM Enabled: No

[<img src="{filename}/images/tri6/DSC03720.JPG" width="480">]({filename}/images/tri6/DSC03720.JPG)

###Stick Scaling  
    Roll (Ail):  30  
    Pitch (Ele): 30  
    Yaw (Rud) : 25  
    Throttle: 90

[<img src="{filename}/images/tri6/DSC03721.JPG" width="480">]({filename}/images/tri6/DSC03721.JPG)

[<img src="{filename}/images/tri6/DSC03722.JPG" width="480">]({filename}/images/tri6/DSC03722.JPG)

###Misc. Settings  
    Minimum throttle: 10  
    Height Dampening: 0  
    Height D. Limit: 30  
    Alarm 1/10 volts: 105 (dispara o alarme de bateria fraca em 10,5 V)  
    Servo filter: 60  
(antes de descobrir que meu tricóptero rodava descontrolado devido à
configuração do Mixer Editor abaixo, mexi muito aqui sem nenhum sucesso)

[<img src="{filename}/images/tri6/DSC03723.JPG" width="480">]({filename}/images/tri6/DSC03723.JPG)

[<img src="{filename}/images/tri6/DSC03724.JPG" width="480">]({filename}/images/tri6/DSC03724.JPG)

###Self-level Settings  
    P Gain: 65  
    P limit: 65  
    ACC Trim Roll: 0  
    ACC Trim Pitch: 0

[<img src="{filename}/images/tri6/DSC03725.JPG" width="480">]({filename}/images/tri6/DSC03725.JPG)

[<img src="{filename}/images/tri6/DSC03726.JPG" width="480">]({filename}/images/tri6/DSC03726.JPG)

###Camera Stab Settings  
    Roll gain: 0  
    Roll offset: 50  
    Pitch gain: 0  
    Pitch offset: 50

[<img src="{filename}/images/tri6/DSC03727.JPG" width="480">]({filename}/images/tri6/DSC03727.JPG)

[<img src="{filename}/images/tri6/DSC03728.JPG" width="480">]({filename}/images/tri6/DSC03728.JPG)

###CPPM settings  
    Roll (Ail): 1  
    Pitch (Ele): 2  
    Throttle: 3  
    Yaw (Rud) : 4  
    AUX : 5 (lembra que o self level estava definido para AUX? É este canal 5)

[<img src="{filename}/images/tri6/DSC03729.JPG" width="480">]({filename}/images/tri6/DSC03729.JPG)

[<img src="{filename}/images/tri6/DSC03730.JPG" width="480">]({filename}/images/tri6/DSC03730.JPG)

###Mixer Editor  
    CH:1  
    Throttle: 100  
    Aileron: -87  
    Elevator: 50  
    Rudder: 0  
    Offset: 0  
    Type: ESC  
    Rate: High

[<img src="{filename}/images/tri6/DSC03731.JPG" width="480">]({filename}/images/tri6/DSC03731.JPG)

###Mixer Editor  
    CH:2  
    Throttle: 100  
    Aileron: 87  
    Elevator: 50  
    Rudder:-1 (acho que era para ser 0, não?)  
    Offset: 0  
    Type: ESC  
    Rate: High

[<img src="{filename}/images/tri6/DSC03732.JPG" width="480">]({filename}/images/tri6/DSC03732.JPG)

###Mixer Editor  
    CH:3  
    Throttle: 100  
    Aileron:0  
    Elevator: -100  
    Rudder: 0  
    Offset: 0  
    Type: ESC  
    Rate: High

[<img src="{filename}/images/tri6/DSC03733.JPG" width="480">]({filename}/images/tri6/DSC03733.JPG)

###Mixer Editor (esta é a configuração importante!)  
    CH:4  
    Throttle: 0  
    Aileron: 0  
    Elevator: 0  
    <span style="color: #990000;">**Rudder: -100**</span>  
    Offset:50  
    Type: Servo  
    Rate:Low

Se o seu tricóptero fica girando descontroladamente em parafuso sempre
que sai do chão, confira esta configuração.

Ao trocar o mecanismo que dá suporte ao servo (que serve de leme e faz o
movimento de yaw), tive que trocar de novo o rudder para 100 (positivo)
e entendi o que acontece. Na peça fornecida pela Flight Test (a que uso
neste vídeo), o servo fica virado para a frente, na direção da placa
KK2.1. Nesta situação, o rudder deve ficar em -100. Se seu servo fica
virado para trás (usando um servo mount do Turnigy Talon, como fiz
depois), o rudder deve ficar em 100 (positivo).

Acontece que se o servo está virado na direção oposta ao que é esperado
pela controladora, o controle dele deve ser invertido! Parece óbvio
depois que vi as duas situações, mas não fazia ideia que existiam estas
duas possibilidades... Agora você sabe!   
 

[<img src="{filename}/images/tri6/DSC03734.JPG" width="480">]({filename}/images/tri6/DSC03734.JPG)

[<img src="{filename}/images/tri6/DSC03735.JPG" width="480">]({filename}/images/tri6/DSC03735.JPG)

[<img src="{filename}/images/tri6/DSC03736.JPG" width="480">]({filename}/images/tri6/DSC03736.JPG)

[<img src="{filename}/images/tri6/DSC03737.JPG" width="480">]({filename}/images/tri6/DSC03737.JPG)

[<img src="{filename}/images/tri6/DSC03738.JPG" width="480">]({filename}/images/tri6/DSC03738.JPG)

[<img src="{filename}/images/tri6/DSC03739.JPG" width="480">]({filename}/images/tri6/DSC03739.JPG)

###Motor Layout  
    No meu layout, os motores 1 e 3 giram na direção horária e o motor 2 na
    direção anti-horária. Se você inverter o controle do rudder, a
    controladora pode se confundir e mostrar todos os motores girando
    iguais. Não se preocupe com isso.

[<img src="{filename}/images/tri6/DSC03740.JPG" width="480">]({filename}/images/tri6/DSC03740.JPG)

[<img src="{filename}/images/tri6/DSC03742.JPG" width="480">]({filename}/images/tri6/DSC03742.JPG)

[<img src="{filename}/images/tri6/DSC03743.JPG" width="480">]({filename}/images/tri6/DSC03743.JPG)

[<img src="{filename}/images/tri6/DSC03744.JPG" width="480">]({filename}/images/tri6/DSC03744.JPG)

[<img src="{filename}/images/tri6/DSC03745.JPG" width="480">]({filename}/images/tri6/DSC03745.JPG)

Meu motor 4 é o servo da cauda e os demais não foram utilizados.

[<img src="{filename}/images/tri6/DSC03746.JPG" width="480">]({filename}/images/tri6/DSC03746.JPG)

[<img src="{filename}/images/tri6/DSC03747.JPG" width="480">]({filename}/images/tri6/DSC03747.JPG)

[<img src="{filename}/images/tri6/DSC03748.JPG" width="480">]({filename}/images/tri6/DSC03748.JPG)

[<img src="{filename}/images/tri6/DSC03749.JPG" width="480">]({filename}/images/tri6/DSC03749.JPG)

Espero que este post ajude alguém que esteja com um tricóptero doido rodando / rotacionando no eixo Z sem rumo.

Desculpem pelas fotos. O tricóptero zanzou tanto pela grama e pela terra que o LCD ficou sujo por dentro... ; )

Abs!  
Otávio

Para ver todos os posts deste projeto, você pode clicar no marcador "[tricarneiro](http://carneiro.blog.br/um/tag/tricarneiro.html)".

###Transcrição do vídeo

Oi pessoal, eu sou o Otávio e o que vocês
estão vendo aí

é a primeira tentativa de vôo do Tricarneiro,
meu tricoptero.

O que eu já fiz aqui... Eu conectei os motores.
Cada motor é conectado a um ESC (electronic

speed controller), que se conecta a uma bateria
e à placa controladora do tricóptero. Esta
aqui, a KK2.1.

Uma peculiaridade aqui é que o segundo ESC,
do segundo motor, você não deve conectar

o pino do meio, pino do "power", o pino de
força.

Isso é para evitar que os reguladores de
tensão fiquem loucos. Cada ESC tem um regulador

de voltagem.

Cada um desses caras tentam transformar a
energia que vem da bateria para 5V.

Da bateria virá uns 13V, 12V, 11V e vai baixando
até ele não conseguir mais sustentar o tricóptero.

E esses 10 a 13V precisam ser convertidos
para 5V (para alimentar a controladora).

Se você deixar todos os ESCs com seus 5V
conectados, um vai tentar regular a voltagem

do outro e isso pode dar interferência na
controladora.

O que eu fiz para evitar isso foi uma espécie
de adaptador.

Eu peguei uma barra de pinos que uso com arduino
e afins. Ele tem três entradas, mas só deixei
dois pinos do outro lado.

Ele tem duas perninhas aqui e três buracos
aqui.

Eu poderia ter arrancado um fiozinho do meio
desse cabinho.

Mas eu tentei ao máximo evitar intervenções
destrutivas. Tentei evitar fazer alguma coisa
que fosse difícil desfazer.

Esse fio vem direto do ESC. Como não tenho
certeza de nada do que estou fazendo, eu prefiro
não destruir nada.

Fiz esse conectorzinho aqui e ele vai aqui.

Todos esses fios você conecta com o negativo
para fora.

Tanto os negativos do receptor quanto os negativos
dos motores ficam para o lado de fora.

Do lado de dentro fica o sinal.

Essa plaquinha é muito fácil de montar porque
ela já te mostra qual o layout dos motores.

Ela diz: motor 1, motor 2, motor 3 quem são
e em que direção eles devem girar, que o
4 é o servo.

Eu falei que o segundo motor eu tirei o positivo,
mas o motor 3 eu deixei todo conectado.

É porque é esse segundo ESC que vai energizar
o servo que fica no rabo.

Vocês vão ver que eu tive um problema que toda vez que o drone levantava vôo

ele tinha uma tendência a girar.

Fiquei achando que era porque o servo de trás
que estava com uma folga. Quebrei a perninha

de trás tentando consertar essa folga e o
problema não era esse.

Na verdade, o Canal 4 é o canal do Yaw, esse movimento. 

Ele estava com o Rudder em 100 e tinha que ficar -100.

Não sei bem porque, mas eu vou colocar todas as configurações dele no blog 
para vocês não terem problema.

Quando eu corrigi isso, ele começou a voar
bem. Então no nosso próximo vídeo vocês
vão ver ele voar direitinho.

A partir do próximo a gente já pode falar
em melhoria ou em como aprender a voar, como

balancear hélices ou como carregar a bateria...

Se tiverem um assunto que interesse mais,
coloquem nos comentários!

Obrigado, gente!



