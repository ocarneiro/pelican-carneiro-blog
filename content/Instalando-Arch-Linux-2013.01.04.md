Title: Instalando Arch Linux 2013.01.04
Date: 2013-02-07 11:49
Author: Otávio Carneiro
Slug: Instalando-Arch-Linux-2013.01.04

**UPDATE: **Parti para outra. Instalei o Ubuntu no desktop e o Manjaro
no meu netbook. Se estiver procurando uma distribuição leve, compatível
com o Arch Linux e que já vem com uma interface gráfica, olhe meu post
abaixo:  
<http://umcarneiro.blogspot.com.br/2013/08/manjaro-um-arch-linux-para-iniciantes.html>

Hoje resolvi fazer mais uma instalação do Arch Linux, desta vez em um
desktop.

Na verdade, minha intenção inicial era instalar o [Linux Mint XFCE 14
64bits](http://blog.linuxmint.com/?p=2263), mas ele travou na tela
"Autobooting in 10 seconds" e não saia disso. Então, parti para o Arch
Linux, a distribuição "faça você mesmo".

Baixei a versão 2013.01.04, fresquinha do site. Eu tinha acabado de
colocar o DVD de instalação do Linux Mint 14 no meu notebook (para ver
se o problema era na mídia), então acabei baixando o Arch por lá, usando
o "Transmission", que é um cliente de torrent que estava ali disponível.

Essa instalação, então, vai ser diferente da [outra que eu
fiz](http://umcarneiro.blogspot.com.br/2012/09/como-instalar-o-arch-linux-versao.html),
então o nome completo desse post poderia ser:

**Instalando Arch Linux 2013.01.04 em um Desktop usando o Linux Mint
xfce 14 como apoio**.

<ol>
<li>
Baixe o Arch Linux do endereco: <https://www.archlinux.org/download/>

</li>
-   O link aponta para um arquivo .torrent, que você pode abrir
    diretamente no Transmission (programa padrão que o Mint indicou)
-   No Transmission, defina o diretório de destino e aguarde o download
    completar.

<li>
Coloque um pendrive (1 GB serve) no computador e verifique que
dispositivo ele está usando:

</li>
<ul>
<li>
abra um terminal (Menu -\> Terminal Emulator)

</li>
<li>
digite lsblk (enter)

</li>
<li>
O Mint (como o Ubuntu e outros) monta automaticamente o pendrive em uma
pasta com o nome /media/mint/LABEL, onde LABEL é o nome que você deu ao
pendrive quando o formatou.

</li>
<li>
Na lista gerada pelo comando lsblk, procure a linha com o nome do seu
pendrive e repare à esquerda qual o dispositivo (algo como sdx1).

</li>
<li>
No meu, tinha uma linha assim:

</li>
-   |- sdb1    8:17   1  963.6M   0  part  /media/mint/BRANCO
-   Isso quer dizer que o meu pendrive, que chamei de BRANCO, está na
    particao 1 do dispositivo "sdb".

</ul>
<li>
Copie o arquivo .iso do Arch para o pendrive utilizando o comando dd:

</li>
-   ATENÇÃO! Cuidado com o comando "dd"! Preste atenção principalmente
    no que você digita no parametro "of="
-   sudo dd bs=4M if=/caminho/arquivo.iso of=/dev/sdx
-   O "sudo" te dá poder para executar o dd. O "dd" copia dados de um
    dispositivo para outro. "bs=4M" serve para acelerar a cópia. "if="
    indica o arquivo de origem. Se você baixou o arquivo na pasta
    default de downloads do Mint, fica
    "if=/home/mint/Downloads/archlinux-2013.01.04-dual.iso". "of="
    indica o destino. Se seu pendrive é o dispositivo sdb (como o meu),
    fica "of=/dev/sdb".
-   A cópia pode demorar uns 5 minutos (dependendo da velocidade do
    pendrive, principalmente).

<li>
Coloque o pendrive na maquina em que quer instalar o Arch e inicie o
computador por ele.

</li>
-   Algumas máquinas são mais fáceis de dar boot pelo pendrive que
    outras. Na minha, tive que entrar no setup da BIOS (apertando DEL
    durante a inicialização) e mudar primeiro a ordem de prioridade dos
    HDs (minha máquina entendeu o pendrive como um HD) e depois a ordem
    do boot. 
-   em algumas máquinas, basta voce apertar Esc no inicio e escolher em
    um menu a opção de ordem de boot. 

<li>
No menu de inicialização do Arch, escolha a opção padrão "Boot Arch
Linux (x86\_64)" .

</li>
<li>
Carregue a configuração de teclado brasileiro:

</li>
-   `loadkeys br-abnt2 `

<li>
Identifique o HD em que deseja instalar o Arch:

</li>
-   lsblk
-   Você vai ver uma linha que contem "/run/archiso/bootmnt". Este é o
    seu pendrive agora (no meu ele ficou na sdb1 de novo). No meu caso,
    o HD da maquina eu vi que era a sda pelo tamanho das particoes. Meu
    HD tem 250GB. O único dispositivo com tamanho parecido ("232.9G") é
    o sda, então sda é o HD.

<li>
Particione o seu HD usando o cfdisk

</li>
-   cfdisk /dev/sdx
-   (no meu caso, /dev/sda)
-   Dessa vez, criei uma partição só para os 250GB, com o tipo 82
    (Linux)

<li>
Formate o HD

</li>
-   mkfs.ext4 /dev/sda1
-   Se quiser dar um nome para o HD, você pode usar a opção -L no mkfs
    ou o comando e2label:
-   e2label /dev/sda1 ARCH\_HD
-   (isso chama a primeira partição do dispositivo sda de "ARCH\_HD")

<li>
Monte a sua partição

</li>
-   mount /dev/sda1 /mnt/

<li>
Conecte-se à internet:

</li>
-   minha maquina tem uma placa wireless, então me conectei por ela:
-   wifi-menu

<li>
Instale a base do sistema operacional:

</li>
-   pacstrap /mnt base
-   Esse passo é o mais demorado (pode levar 30 minutos ou mais)

<li>
Instale o gerenciador de boot:

</li>
-   pacstrap /mnt syslinux
-   Acho que dava para ter instalado junto com o passo anterior, em um
    comando só, mas é rapidinho.

<li>
Instale os pacotes necessários para o uso da rede wi-fi:

</li>
-   pacstrap /mnt wireless\_tools wpa\_supplicant wpa\_actiond dialog

<li>
Configure a montagem automática dos seus discos:

</li>
-   genfstab -p -L /mnt \>\> /mnt/etc/fstab
-   Isso só cria o arquivo que vai ser /etc/fstab que você pode criar de
    outra forma, se souber como formatar o arquivo

<li>
Acesse seu novo sistema operacional:

</li>
-   arch-chroot /mnt

<li>
Dê um nome para seu computador:

</li>
-   echo ARCH\_SERVER \>\> /etc/hostname

<li>
Ajuste o fuso horário:

</li>
-   ln -s /usr/share/zoneinfo/America/Sao\_Paulo /etc/localtime

<li>
Ajuste o idioma:

</li>
<ul>
<li>
Guarde o arquivo original de configuração:

</li>
<li>
cp /etc/locale.gen /etc/locale.gen.old

</li>
<li>
Para inglês, use:

</li>
-   echo LANG=\\"en\_US.UTF-8\\" \>\> /etc/locale.conf

<li>
Para português, use:

</li>
-   echo LANG=\\"pt\_BR.UTF-8\\" \>\> /etc/locale.conf

<li>
Para as duas línguas, execute também o seguinte:

</li>
-   echo pt\_BR.UTF-8 UTF-8 \>\> /etc/locale.gen
-   echo en\_US.UTF-8 UTF-8 \>\> /etc/locale.gen
-   locale-gen
-   Você deve ver o computador gerando duas configurações de localidade
    (locale): pt\_BR.UTF-8 (português do Brasil) e en\_US.UTF-8 (inglês
    dos Estados Unidos) .

</ul>
<li>
Crie a imagem inicial do sistema:

</li>
-   mkinitcpio -p linux

<li>
Configure o syslinux (gerenciador de boot):

</li>
-   nano /boot/syslinux/syslinux.cfg
-   Altere a primeira linha que tem um APPEND para:
-   APPEND root=/dev/sda1 ro
-   Se você criou mais de uma partição, coloque o nome da partição root
    (/) 

<li>
Instale o syslinux na partição inicial do HD:

</li>
-   syslinux-install\_update -iam

<li>
Defina a senha de root:

</li>
-   passwd

<li>
Saia do chroot

</li>
-   exit

<li>
Desligue o computador

</li>
-   halt
-   O meu computador não quis desligar, então forcei o desligamento
    segurando o botão On/Off por alguns segundos

<li>
Tire o pendrive e ligue de novo o computador

</li>
<li>
Escolha a primeira opcao do boot (arch) e entre com o usuario root e a
senha que você definiu.

</li>
</ol>
Eu achei essa instalação inicial (crua) mais fácil de fazer com a versão
2013.01.04 do que [com a
2012.09.07](http://umcarneiro.blogspot.com.br/2012/09/como-instalar-o-arch-linux-versao.html).

<div>

</div>

<div>

Uma coisa que facilitou foi não ter precisado configurar o syslinux
inicialmente. Isso se deve mais por eu ter usado o dd no Linux Mint ao
invés do UNetBootin no Windows para copiar a imagem no pendrive.

</div>

<div>

</div>

<div>

Outra coisa que eu simplifiquei da outra vez para essa foi o
particionamento. Dessa vez eu coloquei uma partição só para tudo. No
Windows a gente costuma criar os drives C: (para o Sistema Operacional)
e D: (para nossos dados), mas no Linux você pode separar inclusive as
partições usadas pelo Sistema e já vi todo tipo de recomendação. A
máquina que eu estava montando não ia ter muitos dados pessoais, era
mais para trabalho usando um repositório de arquivos centralizado, então
achei melhor jogar tudo em uma partição só e simplificar a instalação.

</div>

<div>

</div>

<div>

Ainda não consegui ir muito mais longe do que isso, então aguardem novos
posts sobre o assunto.

</div>

<div>

</div>

<div>

Att.,

</div>

<div>

</div>

<div>

Otávio
<div>

**UPDATE: **Instalei o Manjaro no meu netbook. Se estiver procurando uma
distribuição leve, compatível com o Arch Linux e que já vem com uma
interface gráfica, olhe meu post abaixo:  
<http://umcarneiro.blogspot.com.br/2013/08/manjaro-um-arch-linux-para-iniciantes.html>

</div>

</div>

<div>

</div>
