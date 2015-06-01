Title: Instalando o Debian XFCE no Ultrabook Asus S46C
Date: 2014-11-16 15:07
Author: Otávio Carneiro
Slug: Instalando-o-Debian-XFCE-no-Ultrabook-Asus-S46C

RESUMO PARA QUEM ESTÁ COM PRESSA: Se seu notebook é novo, instale o
Debian 8 (Jessie). Esqueça o Wheezy (Debian 7) e poupe dores de cabeça.

Voltamos à programação normal:

Esta semana comprei um notebook novo para poder fazer atividades de
edição de vídeo no [Calango Hacker Clube](http://calango.club/).

O computador, um Ultrabook Asus S46C, é muito bom, mas vem com Windows 8
e eu queria usar Linux nele.

Antes de qualquer coisa, liguei a máquina, coloquei ela na rede e deixei
o Windows 8 de fábrica fazer as mais de 100 atualizações. Só isso levou
um dia inteiro, reiniciando o computador várias vezes. Acho que foi bom
dar uma brincada com o notebook antes de detonar o sistema operacional,
mas dispensaria essas atualizações se fosse fazer tudo de novo hoje.

Depois de ter certeza de que não queria usar o Windows 8, era hora de
instalar o Linux. Ainda assim, sou medroso e não gosto de tomar atitudes
irreversíveis. Assim, resolvi fazer uma cópia de backup das partições de
recuperação que vieram no notebook, para o caso de um dia eu querer
reinstalar o Windows 8. Vai que o notebook tinha algum recurso que só
funciona no Windows?

Para essa tarefa, usei o [Clonezilla](http://clonezilla.org/).Clonezilla
é uma distribuição Linux que permite você copiar partições inteiras. É
como o Norton Ghost e outros programas do gênero. Você dá boot com ele e
segue as instruções na tela. Tudo muito simples. Para o HD.

O notebook vem também com um drive SSD de 24GB. Esse eu achei que o
Clonezilla ia copiar mais facilmente ainda, tão pequeno... Só que não.
Tive que usar o bom e velho "dd", um comando conhecido como "destruidor
de dados". O comando exato que usei foi esse aqui embaixo, mas eu
estudaria bem o que isso faz antes de sair usando:  
`sudo dd if=/dev/sdb bs=4096 | gzip > dd-sdb.gz `

Agora, sim. Gravei as cópias das partições em um HD externo e fiquei
livre para começar a destruição!

Meu netbook está rodando o manjaro e meu desktop roda Ubuntu, mas desta
vez optei pelo Debian. A versão estável dele é a 7.7 (Wheezy), então fui
com ela.

Instalar o Debian 7.7 (Wheezy) foi muito tranquilo. Ele já dá umas
sugestões de particionamento do disco e tudo. Dei uma estudada e decidi
colocar as partições que gravam mais no HD, deixando o SSD com as
partições mais "estáveis". Deixei a /home no HD também. Como nessa
partição vão morar meus dados, é melhor que ela seja mais fácil de
recuperar. Dizem que recuperar dados de um SSD beira o impossível.

Se alguém quiser uma sugestão de partições para usar o linux em um
computador com HD e SSD, a minha ficou assim:  
/ (root) = SSD = 1 GB (o Debian sugeriu 350MB);  
/var = HD = 3 GB;  
/tmp = HD = 400MB (essa poderia viver na memória RAM. Vou fazer isso um
dia);  
/swap = HD = 12 GB (essa não pode ficar no SSD de jeito algum);  
/home = HD = todo o resto do HD (quase 1 TB);  
/usr = SSD = 8.4 GB (essa partição é praticamente somente leitura);  
(livre) = SSD = 6,5 GB (dizem que é bom deixar de 7 a 30% do SSD não
particionado).  
Sobrou um pouco de espaço no SSD, então criei uma partição "/ssd" para o
caso de eu resolver usar depois.

O restante da instalação foi bem tranquila. Usei a versão XFCE do
Debian. Eu ia com a LXDE, que é a mais leve de todas, mas não fui com a
cara dela. É sempre bom experimentar versões "live" (que rodam direto do
pendrive) antes de escolher.

A única coisa que não funcionou após a instalação inicial foi  o suporte
à placa de vídeo Nvidia. De início, nem notei. Minha filha jogou
Minecraft um dia inteiro usando só a placa de vídeo intel integrada.

Ahn?!

É isso mesmo! O notebook tem, na realidade, duas placas de vídeo: uma
intel integrada e uma Nvidia GEForce de 2GB. E o que é melhor: usa um
sistema que permite que a placa da Nvidia só seja utilizada quando é
necessária (ou solicitada), o que permite uma economia de energia muito
grande.

O problema desse recurso, chamado Optimus, é que ele é novo e precisa de
softwares específicos para funcionar. Descobri que a melhor companhia
para o Optimus é o Bumblebee. Óbvio! Nos Transformers e no Linux eles
são os melhores amigos. Então eu fui à luta para tentar instalar o
bumblebee. Se quiser ler mais sobre isso, pule para o epílogo deste
post.

Depois de muito ralar, descobri que o problema não era com os drivers da
Nvidia, mas sim com o suporte à placa da Intel. O que acontece é que a
placa mãe do notebook só tem suporte no Debian Jessie (Debian 8) e por
isso o Bumblebee não funciona no Debian 7 (Wheezy).

Eu já tinha configurado algumas coisas no notebook. Já tinha colocado um
tema nas janelas (usei o redmondXP, que parece o Windows XP), tinha
colocado um controle de volume e várias outras coisas sugeridas para se
[fazer depois de instalar o
XFCE](http://dontsurfinthenude.blogspot.com.br/2013/06/10-things-to-do-after-installing-debian.html),
inclusive [instalar o
Firefox](http://www.whaleblubber.ca/install-firefox-debian/). Assim,
preferi atualizar a distribuição ao invés de instalar tudo de novo.

Atualizar do Wheezy para o Jessie foi bem fácil. Você só precisa editar
o arquivo "/etc/apt/sources.list" e trocar tudo que diz "wheezy" para
"jessie". Isso vai trocar os repositórios. Aí é só atualizar o sistema
com os comandos:

`sudo apt-get update `  
`sudo apt-get --download-only dist-upgrade `  
`sudo apt-get dist-upgrade `

Achei muito tranquilo. Toda hora que precisava tomar uma decisão, o
sistema deu explicações muito fáceis sobre o que tinha que ser feito. E
em dois momentos ele deu erro mas sugeriu o comando a executar para
consertar. Foi muito fácil.

Depois de atualizar para o Debian Jessie, o computador ficou muito
rápido! Eu já tinha achado ele rápido com o Debian Wheezy, mas dei
crédito ao i7 (meu desktop é um i5). Com o Jessie, ele ficou muito mais
rápido.

Ah, sim, para usar a placa de vídeo nvidia, você precisa rodar os
comandos com um "optirun" antes. Então, para jogar minecraft, meu
comando agora é:

`optirun java -Xmx1024M -Xms512M -cp minecraft.jar net.minecraft.bootstrap.Bootstrap `

Parece muita coisa para rodar um joguinho, mas é só colocar [tudo isso
num
atalho](http://askubuntu.com/questions/34408/how-to-add-minecraft-to-the-unity-launcher)
ou botão para colocar seu Minecraft no desktop.

Outra coisa boa a se fazer com o sistema instalado é colocar os
caracteres "/" e "?" num lugar acessível. Afinal, quem usa linux sem a
barra? Ou escreve sem interrogação? Para colocar a tecla "/?" entre o
alt e o ctrl do lado direito (no lugar do botão estranho com uma lista),
o comando é o seguinte:

`xmodmap -e "keycode 135 = slash question"`

E para fazer o XFCE rodar isto sempre que iniciar, você [altera o script
de inicialização dele](https://wiki.archlinux.org/index.php/xfce).
Basicamente, é copiar o arquivo /etc/xdg/xfce4/xinitrc para
\~/.config/xfce4/ e colocar esse comando no começo dele.

Outra coisa que achei útil foi colocar o botão F9 para desligar o
trackpad. O trackpad desse notebook é grande e fica atrapalhando quando
digito. Então fui na configuração de teclado e associei um script para
[ligar e desligar o
trackpad](https://wiki.archlinux.org/index.php/Touchpad_Synaptics#Software_toggle)
a esta tecla.

Bom proveito!

----------------------------------------------------------------------------------------------------

Epilogo

Se você acha que consegue fazer o bumblebee rodar no wheezy e precisa
ver mais motivos (com telas e log) para te convencer, continue lendo.

Esta foi minha odisséia em busca de colocar o bumblebee funcionando no
wheezy:

Encontrei referência a um pacote "bumblebee-nvidia" e o google me disse
que ele estava no repositório "contrib" em wheezy-backports:

    https://packages.debian.org/wheezy-backports/utils/bumblebee-nvidia

Então adicionei esse repositório no meu synaptic:

    deb http://http.debian.net/debian wheezy-backports main contrib

Depois de recarregar, o pacote bumblebee-nvidia ficou disponível, com
suas inúmeras dependências:

Instalei e reiniciei. Para testar, tentei rodar "glxspheres", mas ele
não existia:

    otavio@otavio-note:~$ glxspheresbash: glxspheres: comando não encontrado

Li que ele pertencia ao pacote mesa-utils, então instalei, mas não tinha
também... Tinha um glxgears, no entanto:

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-fAcOFCHnDiI/VGkuoYEnCAI/AAAAAAAACW0/PLTP2Bp6gKE/s1600/glxgears.png)](http://1.bp.blogspot.com/-fAcOFCHnDiI/VGkuoYEnCAI/AAAAAAAACW0/PLTP2Bp6gKE/s1600/glxgears.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

Então rodei outro teste:

    optirun

e o resultado foi:

    [ERROR]You've no permission to communicate with the Bumblebee daemon. 

    Try adding yourself to the 'bumblebee' group

Então eu fiz isso: `sudo usermod -a -G bumblebee otavio`  
E confirmei se eu estava mesmo no grupo: `groups otavio`  
E reiniciei o bumblebee:  
`sudo service bumblebeed restart`

Recebi um ok, mas o resultado do optirun foi o mesmo...

Na falta de coisa melhor para fazer, reiniciei o computador...

Depois de reiniciar, consegui algum avanço:

    otavio@otavio-note:~$ optirun glxgears[   28.735500] [ERROR]Cannot access secondary GPU - error: 

    [XORG] (EE) NVIDIA(0): Failed to initialize the NVIDIA GPU at PCI:1:0:0.  Please[   28.735560] [ERROR]Aborting because fallback start is disabled.

Depois disso, o notebook ficou louco! Ligou o cooler e ficou mostrando
mensagens sobre a bateria até desligar, uns dois minutos depois.

Ligando o computador de novo, fiz o seguinte:

    sudo grep bumblebeed /var/log/syslog Nov 15 17:56:59 otavio-note bumblebeed[2924]: /usr/sbin/bumblebeed 3.2.1 startedNov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0): Failed to initialize the NVIDIA GPU at PCI:1:0:0.  PleaseNov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0):     check your system's kernel log for additional errorNov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0):     messages and refer to Chapter 8: Common Problems in theNov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0):     README for additional information.Nov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0): Failed to initialize the NVIDIA graphics device!Nov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) NVIDIA(0): Failing initialization of X screen 0Nov 15 17:57:18 otavio-note bumblebeed[2932]: [XORG] (EE) Screen(s) found, but none have a usable configuration.Nov 15 17:57:18 otavio-note bumblebeed[2932]: X did not start properlyNov 15 18:00:35 otavio-note bumblebeed[2935]: /usr/sbin/bumblebeed 3.2.1 started

Descobri que o tal capítulo 8 que a mensagem referencia é do seguinte
arquivo:

    /usr/share/doc/nvidia-kernel-dkms/README.txt.gz

... mas isso não ajudou muito...

Tentei procurar mensagens no kernel:

    otavio@otavio-note:~$ sudo grep bumblebeed /var/log/kern.log otavio@otavio-note:~$ sudo grep nvidia /var/log/kern.log Nov 15 17:57:17 otavio-note kernel: [   28.104207] nvidia: module license 'NVIDIA' taints kernel.Nov 15 17:57:17 otavio-note kernel: [   28.194483] nvidia 0000:01:00.0: setting latency timer to 64

Dizem que essa história de "taints kernel" não quer dizer nada...

Então não obtive nenhuma ajuda aqui.

Começando a estudar tudo de novo, fui lá na página do Bumblebee e achei
o seguinte:  
https://wiki.debian.org/Bumblebee

**Note** wheezy-backports does *not* contain the newer
`xserver-xorg-video-intel` package that is needed by newer intel cards.
If you find yourself stuck with the fbdev or vesa driver then you'll
need to upgrade to jessie or sid. 

Ou seja, dancei! Tive que trocar a versão do meu debian! Meu notebook
deve usar uma dessas placas intel mais recentes...

O resultado eu já disse acima.

