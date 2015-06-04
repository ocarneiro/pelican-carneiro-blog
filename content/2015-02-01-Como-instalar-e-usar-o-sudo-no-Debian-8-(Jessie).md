Title: Como instalar e usar o sudo no Debian 8 (Jessie)
Date: 2015-02-01 05:07
Author: Otávio Carneiro
Slug: Como-instalar-e-usar-o-sudo-no-Debian-8-(Jessie)

Se você resolveu experimentar o Debian 8 e se deparou com a falta do
comando sudo, este post é para você. 

Eu já tinha [instalado o Debian Jessie e deixado ele mais com a minha
cara](http://umcarneiro.blogspot.com/2014/11/deixando-o-debian-xfce-bonito.html)
e no meio do caminho instalei o sudo e várias outras coisas.

Hoje reinstalei o sistema e fiquei de novo abismado com a ausência do
comando sudo.

Se você é iniciante em linux e prefere fazer o máximo de tarefas na
interface gráfica, recomendo o meu artigo anterior (link acima). Neste
aqui eu vou usar mais o console, por ser mais rápido.

Ao instalar o Debian 8, você certamente definiu uma senha de root e
outra para seu usuário. Vamos precisar das duas.

1\) Abra um terminal;  
2) Digite "su"  
3) O sistema vai pedir uma senha. Esta é a senha de root.  
4) Digite "vi /etc/apt/sources.list"  
5) Procure uma linha começada com "deb cdrom: ". No começo desta linha,
digite "i" (para inserir) e coloque uma cerquilha: "\#" para que o
sistema ignore esta linha.  
6) Aperte ESC (para parar de escrever), ":" (dois pontos, para digitar
comandos), "wq" (salvar e sair) e Enter. Pronto, você atualizou seus
repositórios do apt e tirou o CD-Rom do Debian de lá. Se achar que fez
bobagem e quiser sair do vi sem salvar, aperte ESC, ":" "q!" e Enter.
Isso vai te tirar do modo de digitação (ESC), te colocar no modo de
comandos ":" e fechar o vi ("q") sem salvar ("!"). O vi é um editor de
texto bem peculiar, vale a pena aprender!

Feito isso, aproveite que está em modo root (o comando su do passo 2) e
instale o sudo:  
8) Digite "apt-get install sudo"  
9) Dê permissão ao seu usuário para usar o sudo. Digite "usermod -a -G
sudo seu\_usuario".  
10) Faça um logoff ou reinicie o computador para poder usar o sudo com
seu usuário.

A questão toda de usar "sudo" ou "su" é meio controversa. O Ubuntu
adiciona todo usuário aos sudoers, já o Debian sequer instala o sudo. Se
você tem uma opinião sobre qual das abordagens é melhor, deixe nos
comentários, por favor.

Se quiser ler mais posts sobre o
"[Debian](http://umcarneiro.blogspot.com.br/search/label/debian)" use
[este link](http://umcarneiro.blogspot.com.br/search/label/debian) ou os
marcadores do blog.

Abs!  
Otávio

