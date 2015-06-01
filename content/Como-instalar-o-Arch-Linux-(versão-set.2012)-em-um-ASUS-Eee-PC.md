Title: Como instalar o Arch Linux (versão set.2012) em um ASUS Eee PC
Date: 2012-09-12 17:46
Author: Otávio Carneiro
Slug: Como-instalar-o-Arch-Linux-(versão-set.2012)-em-um-ASUS-Eee-PC

**UPDATE2:** Parti para outra. Depois de muita luta consegui instalar o
Manjaro neste mesmo netbook. Se estiver procurando uma distribuição
leve, compatível com o Arch Linux e que já vem com uma interface
gráfica, olhe meu post abaixo:  
<http://umcarneiro.blogspot.com.br/2013/08/manjaro-um-arch-linux-para-iniciantes.html>  
**  
UPDATE:** Escrevi de novo sobre instalação do Arch Linux neste outro
post:
 <http://umcarneiro.blogspot.com.br/2013/02/instalando-arch-linux-20130104.html>  
Nele, falo da versão 2013.01.04, instalando em um desktop e usando o
Linux Mint para baixar a imagem e gravar no pendrive. Se você está
usando Windows e/ou instalando em um netbook, continue por aqui mesmo.

**  
Ingredientes**

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-yceTPnyM8Wc/UFjbQaE-oiI/AAAAAAAAA1Q/g7FRoUf4P4k/s320/01_ingredientes_archlinux_eeepc.jpg)](http://4.bp.blogspot.com/-yceTPnyM8Wc/UFjbQaE-oiI/AAAAAAAAA1Q/g7FRoUf4P4k/s1600/01_ingredientes_archlinux_eeepc.jpg)

</div>

Você vai precisar de:

-   1 (um) Asus Eee PC (o meu é um 2g Surf, cor-de-rosa, mas você pode
    usar outro computador)
-   1 (um) outro computador qualquer para ler instruções diversas (pode
    ser um tablet)
-   1 (uma) mídia removível - pode ser um pendrive ou um cartão SD

<div>

Ingredientes opcionais:

</div>

<div>

-   1 (um) teclado USB (as teclas do meu Eee PC são bem pequenas, então
    recomendo)
-   1 (uma) mídia removível adicional (para instalar o sistema
    operacional sem estragar a instalação original)
-   1 (um) hub USB (para facilitar o troca-troca de mídias e teclado
    entre computadores)

<div>

</div>

</div>

**Motivação**

Tenho um Asus Eee PC 2g Surf. Ganhei há um tempo, de uma amiga, mas
ainda não consegui usar muito. A Asus abandonou o projeto e não libera
atualizações para ele. Com isso, os softwares dele ficaram
desatualizados. Ao tentar entrar no youtube com ele, por exemplo, vários
vídeos não podem ser vistos porque o browser está em uma versão muito
antiga.

Eu baixei e tentei instalar várias distribuições linux nele, mas como
ele só tem 2GB de espaço interno (em um drive SSD), os próprios
softwares de instalação não me permitem.

Foi aí que descobri o Arch Linux, um linux feito à moda antiga. Ele é
uma distribuição que você instala crua, sem nenhuma interface gráfica
nem nada e a partir daí vai incluindo os pacotes que lhe interessa. Por
isso, ele não precisa de enormes requisitos iniciais de hardware, como
outras distribuições. Isso faz dele a distruibuição linux perfeita para
computadores antigos e de pouca capacidade, como o meu Asuszinho Rosa
(sim, ele é cor-de-rosa!).

Meu único problema com o Xandros que vem instalado no Eee PC é sua
desatualização, por isso não quis me desfazer dele por completo. Eu acho
que ele é um sistema bem feito e foi bem instalado, permitindo restaurar
a instalação de fábrica em segundos. Eu queria preservar esta instalação
e instalar outro linux em um pendrive (ou num cartão SD, mais tarde),
então sai pesquisando.

Depois de muito estudar, tentar e errar, cheguei à seguinte fórmula para
instalação (inicial, ainda sem interface gráfica) do Arch Linux no Eee
PC:

Utilizei dois pendrives, um de 1GB (para conter a ISO e rodar o sistema
de instalação) e um de 16GB para ser o destino da instalação (eu não
quis usar o drive interno do laptop para isso e ainda não tenho um
cartão SD adequado)

**Modo de Preparo** (a receita propriamente dita)

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-7UABkpt7BDk/UFjcuaBGGOI/AAAAAAAAA1Y/ffssswPIIT0/s320/02_instalando_archlinux_eeepc.jpg)](http://3.bp.blogspot.com/-7UABkpt7BDk/UFjcuaBGGOI/AAAAAAAAA1Y/ffssswPIIT0/s1600/02_instalando_archlinux_eeepc.jpg)

</div>

1.  Baixe a mídia de instalação (usei a versão de 12 de agosto de 2012 -
    archlinux-2012.09.07-dual.iso)  
   <http://www.archlinux.org/download/>
2.  Baixe o UNetbootin (usei a versão windows-578);  
   <http://unetbootin.sourceforge.net/>
3.  Formate o Pendrive e dê a ele o nome de PENDRIVE1GB
4.  Instale a imagem iso no pendrive de 1GB usando o UNetbootin;
5.  Ajuste o arquivo syslinux.cfg gerado pelo UNetbootin. para incluir o
    label do pendrive de 1GB (ver
    <https://wiki.archlinux.org/index.php/USB_Installation_Media#UNetbootin>.
    -   Adicione uma variável archisolabel com o nome do pendrive na
        linha append, como abaixo:  
       `APPEND initrd=/ubninit ../../ archisolabel=PENDRIVE1GB `

6.  Insira o pendrive no Eee PC e dê boot por ele. No Eee PC, você tem
    que usar a entrada USB da esquerda e apertar ESC várias vezes
    enquanto ele inicia. Você vai ver um menu de inicialização do
    computador e outro recém criado pelo UNetbootin. Escolha a opção
    default de cada um deles.
    <p>
    OBS: a partir daqui o roteiro oficial de instalação do arch
    (<https://wiki.archlinux.org/index.php/Installation_Guide>) funciona
    razoavelmente bem, mas vou continuar guiando vocês.  
    
7.  se você tiver um teclado usb brasileiro, você pode conectá-lo para
    não ter que usar o tecladinho do eeepc. Para configurar o layout de
    teclado brasileiro use:   `loadkeys br-abnt2 `
8.  particione seus discos usando:  
     `cfdisk /dev/sdx  `  ATENCAO: para instalar no drive interno do
    eeepc, troque "sdx" por "sda". Se estiver fazendo como eu
    (instalando em um segundo pendrive, maior, plugado na segunda porta
    USB da direita, troque "sdx" por "sdd").  
   7.1) eu particionei meu pendrive de 16GB assim:  
   7.1.1) 100MB em uma partição ext2 chamada BOOT (bootavel)  
   7.1.2) 14GB em uma partição ext2 chamada ARCH  
   7.1.3) 2GB (o restante) em uma partição swap chamada SWAP  
   OBS: No cfdisk você não põe nome nas partições (labels). Você tem
    que fazer isso depois, ao formatá-las. Se tiver outra distribuição
    linux disponível, use o gparted ou similar, é mais fácil.

    8\) formate (e nomeie) as partições  
   8.1) para formatar partições parecidas com as que mencionei, você faria
    o seguinte (assumindo que seu pendrive de 16GB aparece como /dev/sdd):  
   8.1.1) mkfs.ext2 -L BOOT /dev/sdd1  
   8.1.2) mkfs.ext2 -L ARCH /dev/sdd2

    ATENCAO: no linux, maiúsculas e minúsculas são diferentes, então
    tenha certeza de que está usando -L (maiúsculo).

    9\) monte as suas partições  
   9.1) no meu caso, fiz assim:  
   9.1.1) mount /dev/disk/by-label/ARCH /mnt/  
   9.1.2) mkdir /mnt/boot  
   9.1.3) mount /dev/disk/by-label/BOOT /mnt/boot  
   OBS: repare que parei de usar o /dev/sdd e passei a usar
    /dev/disk/by-label, agora que as partições todas têm nome.

    10\) conecte-se à rede. Eu usei a rede wi-fi de casa usando o comando
    wifi-menu, que é muito fácil.

    11\) instale o sistema básico. Esta é a parte mais demorada. Talvez meu
    pendrive de 16GB seja lento, mas em uma das vezes que fiz isso, levou
    mais de 30 minutos. O comando é o seguinte:  
      pacstrap /mnt base base-devel

    12\) instale o gerenciador de boot. Eu acho o GRUB muito complicado,
    então optei pelo syslinux (o mesmo que o UNetbootin usou para o pendrive
    de 1GB):  
      pacstrap /mnt syslinux

    13\) configure a montagem dos discos.  
   13.1) as partições boot e root (/) você consegue gerar com o genfstab:  
       genfstab -p -L /mnt \>\> /mnt/etc/fstab  
       OBS: repare no "-L" de novo, para usar os nomes das partições.

    14\) acesse seu novo sistema com o chroot do archlinux:  
       arch-chroot /mnt

    15\) dê um nome para seu laptop:  
       echo eeepc \> /etc/hostname

    16\) ajuste o fuso-horário:  
       ln -s /usr/share/zoneinfo/America/Sao\_Paulo /etc/localtime

    <p>
    17\) ajuste suas preferências de idioma:  
       nano /etc/locale.conf  
   17.1) você deve colocar uma linha neste arquivo. eu usei o seguinte:  
       LANG="en\_US.UTF-8"    
   17.2) eu deixei inglês, para facilitar a busca por mensagens de erro,
    mas você pode colocar português usando  
       LANG="pt\_BR.UTF-8"  
   17.3) depois de editar o locale.conf, você tem que gerar o locale que
    você escolheu:  
        nano /etc/locale.gen  
   17.3.1) tire o comentário (apague o \# do início da linha) das linhas
    que indicam a configuração que você escolheu:  
        \#en\_US.UTF-8      vira     en\_US.UTF-8  
    ou  \#pt\_BR.UTF-8      vira     pt\_BR.UTF-8  
        OBS: você não precisa escolher uma delas aqui. você pode ativar as
    duas linhas. Eu ativei as duas e também a linha pt\_BR ISO-8859-1  
   17.3.2) execute o gerador de locale:  
        locale-gen

<div>

<div
style="background-color: #fcfdfe; border-bottom-width: 0px; border-color: initial; border-image: initial; border-left-width: 0px; border-right-width: 0px; border-style: initial; border-top-width: 0px; color: #333333; font-family: sans-serif; font-size: 13px; line-height: 19px; padding-bottom: 7px; padding-left: 0px; padding-right: 0px; padding-top: 7px; text-align: left;">

-Install package wifi-select  
ip link set wlan0 up  
pacman -S wifi-select

</div>

  

<div
style="background-color: #fcfdfe; border-bottom-width: 0px; border-color: initial; border-image: initial; border-left-width: 0px; border-right-width: 0px; border-style: initial; border-top-width: 0px; color: #333333; font-family: sans-serif; font-size: 13px; line-height: 19px; padding-bottom: 7px; padding-left: 0px; padding-right: 0px; padding-top: 7px; text-align: left;">

-Configure Network:  
vi /etc/rc.conf  
add interface="eth0"  
add interface="wlan0"

</div>

<div
style="background-color: #fcfdfe; border-bottom-width: 0px; border-color: initial; border-image: initial; border-left-width: 0px; border-right-width: 0px; border-style: initial; border-top-width: 0px; color: #333333; font-family: sans-serif; font-size: 13px; line-height: 19px; padding-bottom: 7px; padding-left: 0px; padding-right: 0px; padding-top: 7px; text-align: left;">

<https://bbs.archlinux.org/viewtopic.php?pid=1162650>

</div>

</div>

1.  18\) configure o seu arquivo /etc/mkinitcpio.conf  
   18.1) você só precisa mexer na linha HOOKS. A minha ficou assim:  
       HOOKS="base usb udev filesystems usbinput"  
   Explicação: isso basicamente define quais as configurações vão ser
    incluídas no sistema e em que ordem. Repare que não incluí a opção
    "autodetect". Parece que ela é famosa por gerar bugs. Outro ponto digno
    de nota é que eu incluí o "usb" antes do "udev", para ter acesso logo ao
    pendrive de 16GB onde instalei o sistema.

    </p>
    19\) crie a imagem inicial do sistema:  
       mkinitcpio -p linux

    20\) configure o gerenciador de boot:  
   20.1) edite o arquivo syslinux.cfg :  
       nano /boot/syslinux/syslinux.cfg  
   20.2) a única linha que você precisa mexer é o APPEND no menu "arch"
    (como fizemos no arquivo syslinux do pendrive de 1GB no início). Ela
    deve ficar assim:  
       APPEND root=/dev/disk/by-label/ARCH ro  
       Explicação: originalmente, meu arquivo tinha root=/dev/sda3, mas é
    bem melhor fazer referência ao label.  
       OBS: repare que estamos usando a partição root, e não boot. É assim
    mesmo.  
   20.3) execute o instalador do syslinux:  
       syslinux-install\_update -iam  
       Alguém que leu com atenção perguntaria: "eu já não instalei o
    syslinux com o pacstrap lá em cima?", e eu respondo. O pacstrap instalou
    o pacote do syslinux nesta versão inicial do sistema. Este comando
    syslinux-install\_update vai tornar o pendrive "bootável" e copiar nele
    os arquivos para gerar o menu e tudo mais.

    <p>
    21\) defina uma senha de root usando passwd.

<div>

22\) saia do chroot:  
    exit
</p>
23\) desligue o laptop:  
    halt

24\) tire o pendrive de 1GB e coloque o de 16GB na entrada da esquerda.

25\) ligue o computador apertando ESC várias vezes e você entrará no seu
novo archlinux.

Depois de tudo isso, você ainda vai ter que fazer um monte de
configurações (colocar uma interface gráfica por exemplo). Eu também vou
fazer tudo isso, então aguardem um próximo artigo sobre isso.

Quem tiver dificuldades ou estiver usando esse tutorial para resolver
outro tipo de problema, pode deixar um comentário.

Abraço!

<p>
**UPDATE**: <http://umcarneiro.blogspot.com.br/2013/02/instalando-arch-linux-20130104.html>  
(versão 2013.01.04 instalando em Desktop e usando o Linux Mint como
apoio)  
**UPDATE2: **Como instalar o Manjaro (distribuição leve, compatível com
o Arch Linux e que já vem com uma interface gráfica):  
<http://umcarneiro.blogspot.com.br/2013/08/manjaro-um-arch-linux-para-iniciantes.html>

</div>
