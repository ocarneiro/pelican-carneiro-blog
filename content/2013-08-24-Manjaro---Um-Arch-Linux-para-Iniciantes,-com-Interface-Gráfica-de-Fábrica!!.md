Title: Manjaro - Um Arch Linux para Iniciantes, com Interface Gráfica de Fábrica!!
Date: 2013-08-24 15:28
Author: Otávio Carneiro
Slug: Manjaro---Um-Arch-Linux-para-Iniciantes,-com-Interface-Gráfica-de-Fábrica!!
Tags: manjaro, arch_linux

ATUALIZAÇÃO (em 18/06/2014): sugiro olhar [meu post mais recente sobre o
assunto](http://umcarneiro.blogspot.com.br/2014/06/como-instalar-o-manjaro-089-em-um.html),
em que ensino a instalar a versão 0.8.9 do Manjaro.

Depois de ler meus posts sobre o [Arch
Linux](http://umcarneiro.blogspot.com.br/search/label/arch%20linux)
(como instalar a
versão [2012.09.07](http://umcarneiro.blogspot.com.br/2012/09/como-instalar-o-arch-linux-versao.html) e
versão
[2013.01.04](http://umcarneiro.blogspot.com/2013/02/instalando-arch-linux-20130104.html)),
muita gente ficou esperando (em vão, foi mal!) um post sobre como
colocar uma interface gráfica nele.

E agora, depois de mais de 6 meses apanhando (e fazendo outras coisas,
confesso!), finalmente consegui! Não é exatamente o Arch Linux, mas é
quase... E o melhor: funciona no meu netbook velho, um [ASUS EeePC 2g
Surf](http://www.asus.com/Eee_Family/Eee_PC_2G_Surf/#overview), lançado
em 2007.

Estou falando do [Manjaro](http://manjaro.org/), uma distribuição Linux
que tenta aproveitar as vantagens do Arch Linux de uma forma mais
acessível a iniciantes.

O que os desenvolvedores dessa distribuição almejam é disponibilizar um
sistema 100% compatível com o Arch Linux, mas que já venha pronto para
usar, com interface gráfica e tudo.

E não é que os caras conseguiram? Claro que nem tudo são flores, se não
eu não teria levado tanto tempo, não teria escrito este post e você não
estaria lendo, mas vou dar o bizú completo para vocês agora.

[![](http://2.bp.blogspot.com/-TAFfNPw8eVs/UTezS5YKVzI/AAAAAAAABNM/_uMZjf47vQg/s320/06032013226.jpg)](http://2.bp.blogspot.com/-TAFfNPw8eVs/UTezS5YKVzI/AAAAAAAABNM/_uMZjf47vQg/s1600/06032013226.jpg)

Se vocês não leram meus posts anteriores, vou resumir. Eu já tinha
tentado instalar o Arch Linux duas vezes. Na
[primeira](http://umcarneiro.blogspot.com.br/2012/09/como-instalar-o-arch-linux-versao.html),
sofri um bocado só para conseguir dar boot usando o UNetbootin. Na
[segunda](http://umcarneiro.blogspot.com.br/2013/02/instalando-arch-linux-20130104.html),
sofri bem menos, mas levei um tempão só para colocar o sistema básico
rodando (sem interface gráfica).

Com o Manjaro, a coisa foi um pouco mais fácil, mas tive meus percalços.
Esse post se destina a te ajudar a evitar esses percalços. Se tiver
outras dúvidas, coloque nos comentários, que vou complementando o post.

**A versão 0.8.6 é boa. Vai com fé!**  
- Eu havia tentado instalar o Manjaro 0.8.5, mas o instalador gráfico
não funcionava bem na versão 32 bits. Para a versão 0.8.6 isso foi
corrigido. Eu usei a versão OpenBox. Acho que li em algum lugar que ela
era mais leve, agora não me lembro.  
- No momento em que estou escrevendo este post, a versão 0.8.6 é a
versão atual. Se você estiver lendo depois e a versão 0.8.6 não estiver
disponível, tente uma versão anterior e veja se obtém sucesso. Novas
versões tendem a levar algum tempo para estabilizar. No mundo do Linux,
muitas vezes as versões com número ímpar apresentam inovações e as
versões com número par são mais estáveis. Na dúvida, procure a versão
par.

**Use a versão i686, isso quer dizer 32 bits!**  
- Eu sempre me confundo com essas denominações de versões. Quando estava
tentando instalar o Arch, ele tinha uma versão "dual", mas depois fiquei
na dúvida: i686 ou x86\_64? Eu devia ter sacado que "x86\_64" é 64 bits,
né? Mas achei que i686 era Pentium e x86 era não Pentium (Celeron
inclusive?), sei lá... Maluquice minha. Se você está procurando uma
distribuição que sirva num computador velho, vá de i686.

**2GB não são suficientes! Você precisa de pelo menos 4GB!**  
- Meu netbook só tem 2GB de SSD internamente. O cartão de memória que eu
estava tentando usar também só tinha 2GB. Pode esquecer. Arrumem um
cartão SD de 4GB ou um pendrive de pelo menos esse tamanho.

**ImageWriter não serve. Use o UNetBootin.**  
- O manual do Manjaro fala nesse ImageWriter para colocar a mídia ISO do
instalador no pendrive. Eu cheguei a instalar esse ImageWriter, mas
acabei usando meu bom e velho
[UNetBootin](http://unetbootin.sourceforge.net/).  
- Na minha primeira tentativa de instalação do Arch Linux, tive que
alterar o arquivo syslinux.cfg depois de usar o UNetBootin, mas desta
vez, com o Manjaro 0.8.6, não precisei de nada disso. Foi gravar a
imagem e partir para a instalação.

**GRUB não instala - Path \`/boot/grub' is not readable by GRUB on boot.
Installation is impossible. Aborting.**  
- Se você mudou o tipo de filesystem usado pelo cartão SD durante a
instalação (de ext3 para ext4, por exemplo), o GRUB vai se perder e não
vai conseguir instalar.  
[![](http://4.bp.blogspot.com/-1b_Yf9mlBn8/UhkogIGBgFI/AAAAAAAABc0/mFPYIS6-zm4/s320/erroGrubnotReadable.png)](http://4.bp.blogspot.com/-1b_Yf9mlBn8/UhkogIGBgFI/AAAAAAAABc0/mFPYIS6-zm4/s1600/erroGrubnotReadable.png)-
O que você precisa fazer é já estar com o disco particionado quando
começar a instalação. Se precisar particionar para instalar, faça assim:
comece a instalação e vá até o particionamento. Pare. Reinicie o netbook
e comece de novo a instalação, dessa vez pulando o particionamento.  
- Lembre-se de, ao particionar, deixar 1MB no início da partição para o
GRUB, ou terá o problema abaixo (embedding too small).  
[Leia mais sobre o assunto aqui (em
inglês)](https://bbs.archlinux.org/viewtopic.php?id=154768)

**GRUB não instala - "embedding area is unusually small, core.img won't
fit in it":**


[![](http://4.bp.blogspot.com/-0B2I57Y03M8/UhkhRMva9kI/AAAAAAAABck/DpXmXLF6ang/s320/DSC01357.JPG)](http://4.bp.blogspot.com/-0B2I57Y03M8/UhkhRMva9kI/AAAAAAAABck/DpXmXLF6ang/s1600/DSC01357.JPG)

- Você precisa deixar um pequeno espaço no início do cartão SD (ou
pendrive) para o boot loader. Se você não fez isso (eu não fiz), você
receberá uma tela de erro como esta, dizendo que sua área de "embedding"
é muito pequena e que o "core.img" não vai caber nela.  
- Aí você tem duas opções: ou começa tudo de novo deixando um espaço
vazio no início do cartão SD na hora de particionar; ou  
- de dentro do próprio Manjaro, você pode rodar o GParted e mover a
primeira partição 1MB para a frente. Você pode fazer isso com a tela do
instalador aberta, e depois retomar a instalação. Eu fiz a alteração e
voltei no passo "2. Disk Preparation" só para informar qual partição eu
estava usando. Depois pulei direto para o passo "5. Install Bootloader"
para terminar a instalação.  
- A primeira alternativa (começar de novo) não é tão mal, já que a
segunda (mover a partição) leva uns 15 minutos. Claro que, se você está
lendo isso antes de começar, não vai precisar passar por este problema.  
[Leia mais aqui (em
inglês)](http://ubuntuforums.org/showthread.php?t=1528529)

**Login não funciona:**  
- Quando finalmente consegui fazer a instalação completa, descobri que
as senhas que informei durante a instalação não funcionavam... O teclado
do meu netbook (Asus 2g Surf) é bem pequeno e eu acho que o Num Lock é
ligado pelo Manjaro durante o boot, o que muda a letra "o" para "6", o
"j" para "1" e outras maluquices que tornam quase impossível digitar uma
senha corretamente.  
- O problema é que há alguns caracteres que não aparecem na tela, mas o
Linux registra na senha e depois você não consegue mais digitar
exatamente estes caracteres na hora de logar.  
- Para evitar que isso aconteça com você, teste o teclado quando ele te
pedir para colocar a senha. Aperte Ctrl+Alt+F1 e vá para o console (tela
preta). Se precisar de senha, o usuário padrão é manjaro e a senha é
manjaro. Digite qualquer coisa aí e veja se o teclado está funcionando
como deveria. Desligue o Num Lock com Fn+F11, se for o caso. Para voltar
para a interface gráfica, aperte Alt+F7.  
- Se você fez como eu e instalou tudo para descobrir depois que não
consegue acertar a senha de jeito nenhum, há uma solução. Siga os passos
abaixo.  
- Coloque o cartão de memória em outro computador, de preferência um
linux em que você tenha acesso como root.  
- Procure, no cartão de memória (não no seu computador), o arquivo
etc/passwd. Provavelmente vai ser algo como /media/SDCard/etc/passwd.
Atenção: não confunda com o /etc/passwd do computador onde você colocou
o cartão SD (ou pendrive).  
- Altere esse arquivo, onde aparece root:\*\*\*\*\*:0:0:root (\*\*\*\* é
um monte de caracteres, que podem ir até a outra linha). Altere para:  
    root::0:0:root  
- Isso vai zerar a senha do root, deixando você entrar sem senha. Você
pode fazer o mesmo para o usuário manjaro (ou o que você criou). Vai
ficar:  
    manjaro::1000:100::/home/manjar:/bin/bash  
- Altere também o arquivo /media/SDCard/etc/shadow. O procedimento é
mesmo, eliminar o campo de senha, deixando o vazio. Algo como:  
root::15930::::::  
manjaro::15930:0:99999:7:::  
- Isso deve resolver. Agora você conseguirá acessar o Manjaro. Recomendo
que você coloque senhas nos dois usuários assim que conseguir usá-los.  
[Leia mais aqui (em
inglês)](http://www.debianadmin.com/forgot-root-password-or-reset-root-password-in-debian.html)

**Próximos passos:**  
- Com a máquina devidamente instalada, eu recomendaria algumas ações:  
- Desligar o Num Lock na inicialização. Ainda não descobri como fazer
isso, mas tenho certeza de que há uma maneira. É muito irritante ficar
brigando com o tecladinho do netbook. Se você estiver usando um teclado
USB plugado nele, acho que nem vai perceber.  
- Desligar a inicialização automática da interface gráfica. Meu netbook
não é exatamente uma bala e eu me viro bem no console, então acho que
deixaria para rodar a interface gráfica quando ela fosse realmente
necessária. Depende do que eu for fazer com ele.  
- Instalar a IDE do Arduino. Eu tenho brincado muito com o
[Arduino](http://umcarneiro.blogspot.com.br/search/label/arduino) e acho
que esse netbook seria o acompanhamento perfeito para ele, mas ainda não
me aventurei a instalar a IDE. Se alguém lendo isso já tiver instalado o
Arduino no Manjaro (ou no Arch) e quiser me dar a dica nos comentários,
agradeço.

Para ver outros posts similares, clique nas tags
[manjaro](http://umcarneiro.blogspot.com.br/search/label/manjaro),
[linux](http://umcarneiro.blogspot.com.br/search/label/linux) ou
[netbook](http://umcarneiro.blogspot.com.br/search/label/netbook),
abaixo.

ATUALIZAÇÃO (em 18/06/2014): se você leu tudo e se animou a experimentar
o Manjaro, sugiro olhar [meu post mais recente sobre o
assunto](http://umcarneiro.blogspot.com.br/2014/06/como-instalar-o-manjaro-089-em-um.html),
em que ensino a instalar a versão 0.8.9.

Abraços,  
Otávio

