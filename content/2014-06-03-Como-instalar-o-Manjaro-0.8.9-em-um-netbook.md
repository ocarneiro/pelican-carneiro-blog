Title: Como instalar o Manjaro 0.8.9 em um netbook
Date: 2014-06-03 19:04
Author: Otávio Carneiro
Slug: Como-instalar-o-Manjaro-0.8.9-em-um-netbook

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-woTzFcFdWMY/U22e3E3I_rI/AAAAAAAAB8E/6dVSUgdr5ic/s1600/equipamento.jpg)](http://1.bp.blogspot.com/-woTzFcFdWMY/U22e3E3I_rI/AAAAAAAAB8E/6dVSUgdr5ic/s1600/equipamento.jpg)

</div>

Quem acompanha meu blog pode ter acompanhado a minha busca pela melhor
distribuição Linux para um netbook velho que eu tinha aqui em casa.

Escolher um sistema operacional não é uma coisa muito simples, ainda
mais se você tem necessidades específicas.

Eu queria um linux que rodasse bem no meu Asus EeePC Surf 2g. Ele só tem
512MB e veio com um sistema operacional customizado pela ASUS que não
tem atualizações disponíveis há muitos anos.

Eu já tinha tentado instalar um [Puppy Linux](http://puppylinux.org/) e
outras distribuições, sem nenhum sucesso. Aí eu tentei o Arch Linux [uma
vez](http://umcarneiro.blogspot.com.br/2012/09/como-instalar-o-arch-linux-versao.html),
mas não consegui colocar uma interface gráfica. Então tentei [uma
segunda
vez](http://umcarneiro.blogspot.com.br/2013/02/instalando-arch-linux-20130104.html),
desta vez em um desktop, mas não fui muito mais longe. Por fim, larguei
de mão do [Arch Linux](https://www.archlinux.org/) puro e instalei o
[Manjaro](http://manjaro.org/get-manjaro/) no meu netbook, mas não dei
muita explicação. No meu [post sobre o
assunto](http://umcarneiro.blogspot.com.br/2013/08/manjaro-um-arch-linux-para-iniciantes.html),
falei mais sobre os problemas que encontrei no caminho.

Pois bem, depois de passar mais um tempo com ele encostado, resolvi
pegar de novo o netbook para mexer. Fui atualizá-lo e tive alguma
dificuldade com o Openbox e problemas de permissões na hora de atualizar
via console com o pacman. Achei que era uma boa oportunidade de começar
do zero e registrar aqui o passo a passo completo.

Antes de tudo, você deve entrar lá na página do
[Manjaro](http://manjaro.org/get-manjaro/) e fazer o download da versão
que você deseja instalar..

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-Thqw8t0_JWU/U22RynWYY-I/AAAAAAAAB7o/0OJCp9dFFNY/s1600/getManjaroXFCE.png) ](http://4.bp.blogspot.com/-Thqw8t0_JWU/U22RynWYY-I/AAAAAAAAB7o/0OJCp9dFFNY/s1600/getManjaroXFCE.png)

</div>

<div class="separator" style="clear: both; text-align: left;">

[![](http://3.bp.blogspot.com/-l4QOyV0kC78/U22e5x-myvI/AAAAAAAAB8M/rkbAIeftvMs/s1600/IMG_20140509_232108279.jpg)](http://3.bp.blogspot.com/-l4QOyV0kC78/U22e5x-myvI/AAAAAAAAB8M/rkbAIeftvMs/s1600/IMG_20140509_232108279.jpg)Desta
vez escolhi a versão XFCE. Na verdade, da última vez eu acho que não
tinha escolhido essa porque o pendrive que eu tinha disponível era de
1GB e o arquivo tinhas uns 70MB mais do que isso... Literalmente, foi
por muito pouco que não consegui usá-la... Desta vez apelei e formatei
um pendrive de 16GB, apesar de ter um menor em alguma gaveta... Se você
tiver um de 2GB, acho que é o tamanho ideal. Se quiser usar um pendrive
com mais que isso (como eu fiz), fique à vontade..

</div>

Lembre-se de que você vai precisar de duas mídias: um cartão SD de 6GB
(ou mais) para instalar o sistema operacional que vai rodar no netbook e
um pendrive de 2GB (ou mais) para servir de "disco de instalação". Você
pode usar dois pendrives, mas não adianta ter dois cartões SD. O meu
netbook só tem um leitor de cartão SD. Então, a não ser que você tenha
um leitor de cartões USB, você precisa de um pendrive e um cartão.

Na minha tentativa anterior, eu tinha escolhido a versão Openbox e
daquela vez o pendrive de 1GB serviu bem e o cartão de 4GB também.
Aparentemente, a edição XFCE é mais "gulosa". Para essa, você vai
precisar de um pendrive de 2GB e um cartão de 6GB.

<div class="separator" style="clear: both; text-align: left;">

</div>

<div class="separator" style="clear: both; text-align: left;">

Vamos começar pela preparação do pendrive de instalação. Toda vez que eu
mencionar pendrive agora vai ser a mídia onde está a imagem de
instalação, que prepararemos agora. Quando eu falar em cartão SD, estou
falando da mídia em que o Manjaro ficará instalado em definitivo, que
vai ficar morando dentro do netbook. Se você estiver usando mídias
diferentes, tenha isso em mente.

</div>

<div class="separator" style="clear: both; text-align: left;">

</div>

<div class="separator" style="clear: both; text-align: left;">

Sugiro que a formatação do pendrive seja feita no modo FAT32, que é o
padrão de fábrica, normalmente. Este padrão funciona bem em qualquer
sistema operacional. É bom também dar um rótulo (label) para o pendrive,
vai ajudar a identificá-lo durante a instalação.

</div>

<div class="separator" style="clear: both; text-align: left;">

</div>

<div style="clear: both; text-align: left;">

[![](http://1.bp.blogspot.com/-PLpXZRqv_TY/U22VdcZX2fI/AAAAAAAAB70/aGoSbworV70/s1600/UNetbootin-site.png)](http://1.bp.blogspot.com/-PLpXZRqv_TY/U22VdcZX2fI/AAAAAAAAB70/aGoSbworV70/s1600/UNetbootin-site.png)Para
gravar o disco de instalação no pendrive, você vai precisar do
[UNetbootin](http://unetbootin.sourceforge.net/). O que o UNetbootin faz
é gravar uma imagem ISO em um pendrive, o que corresponde a queimar um
CD, como se dizia antigamente. Uma imagem ISO é um grande arquivo
compactado que contém todo o conteúdo de um CD, DVD ou Blu-Ray. Ela
guarda os arquivos e alguma configuração do CD original, então não
adianta você simplesmente descompactá-la no pendrive, você precisa de um
programa que transforme a partição do pendrive numa cópia exata da
partição que deu origem a imagem. É isso que o UNetbootin faz.
</p>
Escolha com cuidado a letra do drive onde vai gravar a imagem, para
evitar apagar alguma coisa.

A primeira vez em que rodei o UNetbootin deu errado, lógico. Fui dar o
boot no netbook e ele dizia que a imagem estava inválida ("Invalid or
corrupt kernel image"). Aí formatei o pendrive sem usar a opção rápida
(levou uma meia hora) e gravei de novo. Aí, sim, deu errado de novo!
Então deixei de ser teimoso e fui olhar se o arquivo tinha sido baixado
direitinho. Como se faz isso? Conferindo o checksum. Checksum é uma
análise de arquivos que gera um código a partir dos dados do arquivo.
Dois arquivos idênticos devem gerar exatamente o mesmo código, como no
processo de assinatura digital. A maioria dos sites que têm grandes
arquivos para baixar disponibiliza o checksum para você conferir. No meu
caso, usei o sha1sum.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-QkH7MvjqzxI/U24_p5pMQPI/AAAAAAAAB84/2KyPh2VgQGY/s1600/invalid_image.jpg)](http://1.bp.blogspot.com/-QkH7MvjqzxI/U24_p5pMQPI/AAAAAAAAB84/2KyPh2VgQGY/s1600/invalid_image.jpg)

</div>

<div style="clear: both; text-align: left;">

[![](http://3.bp.blogspot.com/-mkXGqY7aCqQ/U24-EGxPZLI/AAAAAAAAB8s/cyGk2GGB7zY/s1600/sha1sum_v2.png)](http://3.bp.blogspot.com/-mkXGqY7aCqQ/U24-EGxPZLI/AAAAAAAAB8s/cyGk2GGB7zY/s1600/sha1sum_v2.png)Mesmo
no Windows, eu gosto de usar terminal unix, então uso muito o
[Cygwin](http://www.cygwin.com/). É como o "cmd" do Windows, mas você
usa "ls" ao invés de "dir", por exemplo. Ou seja, os comandos do Linux.
Dentro do Cygwin você pode instalar pacotes, como no Linux. Não me
lembro se o sha1sum já vem com ele ou instalei, mas rodei de lá. É só
dar um "sha1sum arquivo.iso" que ele te mostra o checksum do arquivo. O
comando demora um pouquinho para rodar (uns 2 minutos), não se preocupe.

</div>

<div style="clear: both; text-align: left;">

</div>

<div style="clear: both; text-align: left;">

O meu checksum deu bem diferente do que dizia o site do Manjaro, então
meu arquivo estava obviamente corrompido. Por isso tive de baixar de
novo e conferir. Na segunda vez deu certinho, como vocês podem ver na
imagem. O sha1sum que obtive no Cygwin foi exatamente o mesmo do arquivo
que baixei do site.

</div>

<div style="clear: both; text-align: left;">

</div>

<div style="clear: both; text-align: left;">

Hora de rodar o UNetbootin de novo. Gravei a imagem no pendrive com ele,
ejetei o pendrive e o inseri no netbook. 

</div>

<div style="clear: both; text-align: left;">

</div>

<div style="clear: both; text-align: left;">

Para dar boot pelo pendrive, meu netbook (Asus Eee PC 2G Surf) exige que
eu use a porta USB da esquerda. Depois de inserir o pendrive, você liga
o netbook e fica apertando ESC várias vezes, até surgir a tela de
escolher mídia.
</p>
<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-CVkltJdOhKA/U45kfZDK5FI/AAAAAAAACEk/PAbT2BsNXps/s1600/eeepc_boot_device.jpg)](http://1.bp.blogspot.com/-CVkltJdOhKA/U45kfZDK5FI/AAAAAAAACEk/PAbT2BsNXps/s1600/eeepc_boot_device.jpg)

</div>

 No meu netbook apareceram três opções de mídia:

-   HDD, que é drive SSD embutido no netbook;
-   USB DISK, que é o pendrive onde gravei a imagem de instalação com o
    UNetbootin; e
-   CardReader SD0, que é o cartão SD onde pretendemos instalar o
    sistema operacional.

 Escolha USB Drive e você vai ver a tela de boot do UNetbootin.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-a0SG7bVvwFY/U45nK5jYFDI/AAAAAAAACEw/DdnExhF0_DY/s1600/unetbootin-grub.jpg)](http://2.bp.blogspot.com/-a0SG7bVvwFY/U45nK5jYFDI/AAAAAAAACEw/DdnExhF0_DY/s1600/unetbootin-grub.jpg)

</div>

Nesta tela, a opção "default" não faz nada... É a opção "start" que dá o
boot pela imagem que está no pendrive. Vai entender... O processo de
inicialização mostra vários erros (não foi possível montar etc/sda e
outros), mas ele inicializa mesmo assim. Levou um tempinho, mas o
Manjaro XFCE iniciou...

</div>

<div style="clear: both; text-align: left;">

Uma vez dentro do Manjaro, você será recebido com uma grande tela de
boas vindas e terá a opção "Install Manjaro" disponível logo na primeira
tela. Você poderá inclusive escolher o idioma em que quer fazer a
instalação. E, sim, nosso "Português do Brasil" está entre as opções!
</p>
<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-XbfbLZg5bV0/U45rxpDLXKI/AAAAAAAACE8/HUS_q1NZ5Y4/s1600/Manjaro_Welcome.png)](http://2.bp.blogspot.com/-XbfbLZg5bV0/U45rxpDLXKI/AAAAAAAACE8/HUS_q1NZ5Y4/s1600/Manjaro_Welcome.png)[![](http://1.bp.blogspot.com/-_9HBRcx62I0/U45sKaJMw8I/AAAAAAAACFM/QIr--_U3hEc/s1600/portuguesBR.png)](http://1.bp.blogspot.com/-_9HBRcx62I0/U45sKaJMw8I/AAAAAAAACFM/QIr--_U3hEc/s1600/portuguesBR.png)

</div>

Ao iniciar a instalação, o Manjaro faz três verificações iniciais: se
você tem 6GB disponíveis, se você está ligado à rede elétrica e se você
está conectado à internet. De início, eu não estava conectado à
internet, mas ao clicar no ícone de rede desconectada (dois cabos de
rede com um x vermelho), pude escolher a minha rede Wi-Fi e me conectar,
sem nem sair da tela de instalação. Depois você escolhe o fuso horário
onde está e segue para a parte que exige atenção: Tipo de Instalação.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-kIbaujZq1GE/U45s3XeiK_I/AAAAAAAACFY/d45iq8Bzp3g/s1600/tipo_instalacao.png)](http://2.bp.blogspot.com/-kIbaujZq1GE/U45s3XeiK_I/AAAAAAAACFY/d45iq8Bzp3g/s1600/tipo_instalacao.png)

</div>

Eu continuo (anos depois) achando que o Linux que vem de fábrica nesses
EeePC é bem feito e merece continuar nele. Além disso, o HD interno
(SSD, na verdade) desse bicho só tem 2GB, então não adianta tentar
instalar o Manjaro nele. Assim, nossa melhor opção é gerenciar as
partições nós mesmos para escolhermos o nosso cartão SD como local de
instalação.

Escolhi "Gerenciar as partições da instalação do Manjaro (avançado)".

O instalador vai abrir uma tela de particionamento muito parecida com o
GParted e outros programas com a mesma finalidade. Escolha com cuidado o
dispositivo que quer particionar. Se estiver usando mídias de diferentes
tamanhos (como eu), fica fácil. Escolha a que tem o tamanho mais próximo
do cartão SD. Meu cartão é de 8GB e o mais próximo disso é o 7.40GB que
ele mostra. Se seu pendrive e cartão tiverem o mesmo tamanho, olhe o
rótulo das partições montadas. Lembra que falei para formatar o pendrive
com um nome fácil? É por isso.

O Manjaro pode te pedir para escolher um tipo de tabela de partições. Eu
escolhi msdos (MBR).

Particione o cartão SD com um espaço inicial de, pelo menos, 3MB. Você
pode fazer isso criando uma partição de 3MB inicialmente (de qualquer
tipo). Depois você cria uma segunda partição primária com ponto de
montagem "/" (root). Aí você apaga a primeira. Você só precisa de uma
partição. Há muita discussão sobre a melhor forma de particionar um
disco, mas estamos trabalhando com um cartãozinho SD, melhor deixar tudo
junto misturado mesmo.

Eu usei o tipo "ext4". Também existem inúmeras possibilidades de escolha
de filesystem, mas meu cartão vai morar dentro do netbook, então peguei
o tipo que pareceu me dar maior performance, sem me preocupar com
compatibilidade com outros sistemas operacionais. Se fosse me preocupar
em compartilhar esse cartão com máquinas Windows ou MAC's, eu
provavelmente ficaria com o fat32.

A minha partição ficou como na imagem abaixo, 4MB iniciais (acho que já
tinha esse espaço lá) e o restante todo como ponto de montagem "/"
(root). Esta tela eu já tirei de dentro do Manjaro instalado.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-eacwJKioe6E/U45wDwlDKqI/AAAAAAAACFk/GiZy50YMnxk/s1600/gparted.png)](http://1.bp.blogspot.com/-eacwJKioe6E/U45wDwlDKqI/AAAAAAAACFk/GiZy50YMnxk/s1600/gparted.png)

</div>

O Manjaro também pergunta onde ele deve instalar o gerenciador de
inicialização (GRUB). Eu pedi para ele colocar no mesmo cartão SD. Isso
quer dizer que eu vou ter que ficar sempre apertando ESC mil vezes para
entrar no meu Manjaro, mas não me importo. Assim, se alguém for fuçar no
netbook, vai cair no sistema operacional original (Xandros), enquanto eu
e meus leitores saberemos que o Manjaro está ali escondido ; ).

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-RHOZwDC_s8k/U451ti7qVOI/AAAAAAAACF0/9iNaMcbuTP0/s1600/quemevoce.png)](http://4.bp.blogspot.com/-RHOZwDC_s8k/U451ti7qVOI/AAAAAAAACF0/9iNaMcbuTP0/s1600/quemevoce.png)

</div>

Agora, o Manjaro vai perguntar "Quem é você?". Ele quer que você defina
seu usuário. Aparece uma caixinha "Utilize a senha do usuário root". Não
entendi bem. Deve ser algum problema de tradução... Eu marquei e defini
a senha do root também. É melhor você escolher do que ele definir algo
que todo mundo sabe, menos você. Deixei o Logon automático, para
facilitar a vida. Se você tiver alguma preocupação de acesso indevido,
peça para ele exigir senha no log in.

Depois de todas essas configurações, o Manjaro vai ficar um tempo
trabalhando... Ao final, ele avisa: "Instalação finalizada! Deseja
reiniciar o sistema?". Você pode dizer que sim e correr para o abraço,
seu Linux está instalado!

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-FgsRYyw3fxs/U453b_RFvPI/AAAAAAAACGA/fal9gcYXC64/s1600/firefox.jpg)](http://3.bp.blogspot.com/-FgsRYyw3fxs/U453b_RFvPI/AAAAAAAACGA/fal9gcYXC64/s1600/firefox.jpg)

</div>

O Manjaro já vem com o Firefox, LibreOffice e uma boa seleção de outros
programas. Ainda não precisei instalar outras coisas, mas vi que ele tem
uma opção "Adicionar / remover programas".

</div>

<div style="clear: both; text-align: left;">

</div>

Depois de instalar, ele ficou acusando atualizações a fazer, mas a
janela não cabia na tela para eu aceitar. Se isso acontecer com vocês,
vocês podem segurar a tecla Alt e arrastar um ponto qualquer da janela.
Não precisa pegar a janela por cima, não. Assim você consegue achar os
botões abaixo.

Aqui, a atualização não funcionou de cara. Aparentemente, uma das coisas
a atualizar era o gerenciador de janelas, então tive que ir para o
terminal em modo texto. Os comandos a rodar eu peguei numa resposta ao
[fórum Manjaro
Brasil](http://www.manjaro-linux.com.br/forum/viewtopic.php?f=16&t=2190).
Apertei Ctrl+Alt+F1, fiz o login e rodei os seguintes comandos:

`sudo pacman -Syysudo pacman -S manjaro-keyringsudo pacman -Suu`  
`sudo pacman -Suu`

Demorou um bocado! Aparentemente tinha muita coisa para ser atualizada.
Se a tela ficar preta, não se assuste, é só uma proteção de tela. Aperte
"Ctrl" ou outra tecla "inofensiva", que ele volta.

O último comando eu rodei mais  de uma vez mesmo. Ele atualiza uma parte
e depois atualiza o resto.

Estou há alguns dias com o sistema rodando e estou gostando. Ele demora
um pouquinho para iniciar no meu netbook, mas depois fica espertinho.
Minha ideia é ficar com ele por perto para usar principalmente o
terminal. Às vezes dou uma desconfigurada no meu Ubuntu e é legal ter
uma outra máquina para dar um "ssh" nele e ver o que está acontecendo.

Se você tem um netbook como o meu e expectativas muito altas, devo dizer
logo: mesmo rodando o Manjaro o meu netbook não dá conta de ver vídeos
do YouTube. Os vídeos até abrem e você consegue ouvir o áudio e tal, mas
é só para alguma emergência audiovisual. Para dar uma navegadinha na
internet ele serve bem.

<p>
Se quiserem saber sobre algum programa específico, por favor indiquem
nos comentários. Eu escolho os temas do blog com base na popularidade
dos posts existentes, então há boas chances de suas sugestões aparecerem
numa próxima atualização.

</div>

<div style="clear: both; text-align: left;">

Para ver outros posts similares, clique nas tags
[manjaro](http://umcarneiro.blogspot.com.br/search/label/manjaro),
[linux](http://umcarneiro.blogspot.com.br/search/label/linux) ou
[netbook](http://umcarneiro.blogspot.com.br/search/label/netbook),
abaixo.

</div>

<div class="separator" style="clear: both; text-align: left;">

</div>

<div class="separator" style="clear: both; text-align: left;">

Abs.,

</div>

<div class="separator" style="clear: both; text-align: left;">

Otávio

</div>


