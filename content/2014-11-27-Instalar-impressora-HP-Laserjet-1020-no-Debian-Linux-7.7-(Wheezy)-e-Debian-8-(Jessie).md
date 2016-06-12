Tags: debian, linux, tutorial
Title: Instalar impressora HP Laserjet 1020 no Debian Linux 7.7 (Wheezy) e Debian 8 (Jessie)
Date: 2014-11-27 17:35
Author: Otávio Carneiro
Slug: Instalar-impressora-HP-Laserjet-1020-no-Debian-Linux-7.7-(Wheezy)-e-Debian-8-(Jessie)

(Atualizado em 07/12/2014 para incluir configuração no Jessie)

Fiquei um tempão apanhando para colocar minha impressora para funcionar.

No fim, parece que o que funcionou foi instalar o pacote hannah-foo2zjs.

ATUALIZAÇÃO (em 07/02/2015): Para localizar o pacote, você precisa
adicionar os repositórios contrib e non-free ao synaptic, como fiz
[neste outro
post](http://umcarneiro.blogspot.com/2015/02/como-adicionar-os-repositorios-contrib.html).

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-8L5K6szdh6g/VHfP2QWIV5I/AAAAAAAACZQ/tdeWeFiWcyc/s1600/hannah.png)](http://2.bp.blogspot.com/-8L5K6szdh6g/VHfP2QWIV5I/AAAAAAAACZQ/tdeWeFiWcyc/s1600/hannah.png)

</div>

Com o pacote instalado, rodei em um terminal:  sudo hannah-foo2zjs

Com isso, pude escolher minha impressora (HP1020) no meio de muitas
outras HP, Minolta, Samsung e Xerox.

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-Tvx0EnObweg/VHfQQQ4XbvI/AAAAAAAACZY/FAETBy2eldU/s1600/hannah2.png)](http://4.bp.blogspot.com/-Tvx0EnObweg/VHfQQQ4XbvI/AAAAAAAACZY/FAETBy2eldU/s1600/hannah2.png)

</div>

Aí, marquei para fazer o download e pude adicionar a impressora
normalmente pelo gerenciador de impressão do Debian.

-- ATUALIZAÇÃO (em 07/12/2014) --  
A impressora parou de funcionar depois de ficar sem papel durante uma
impressão. Por coincidência, eu tinha também instalado o Debian Jessie
pouco antes e fiquei sem saber o que causou o problema. Para piorar,
esta minha dica também deixou de funcionar. Caos! Uma semana sem
impressora! Mas descobri como resolver:

1\) Desinstalei todos os programas relativos à impressora. Usei a
desinstalação completa (purge), que inclui as configurações. Nisso foram
embora: cups, hplip, hpcups, hannah-foo2zjs, foo2zjs e quase tudo que
tinha hp no nome.

2\) Reiniciei o computador.

3\) Reinstalei o cups e o hannah-foo2zjs.

4\) Criei um link para o arquivo getweb:  
  sudo ln -s /usr/sbin/getweb /usr/bin/getweb  
(parece que esse pacote hannah-foo2zjs está abandonado e usa referência
ao arquivo errado)

5\) Rodei o hannah-foo2zjs e instalei o driver como ensinei acima:  
  sudo hannah-foo2zjs

6\) Reiniciei o computador

7\) Instalei hplip e hplip-gui

8\) Reiniciei o computador

9\) Cliquei em "Menu de aplicativos" -\> Configurações -\> "Configurações
da impressora"

10\) Adicionei minha impressora, como se nada tivesse acontecido.

Mais uma coisa: quando o configurador de impressora ou o CUPS pedir
usuário e senha, faça login como root.

E se for imprimir frente e verso, use essa minha dica do ano passado que
ainda funciona direitinho:  
[Economizando papel no
Linux](http://umcarneiro.blogspot.com/2013/07/economizando-papel-no-linux.html)

-- Fim da Atualização --

Espero que isso ajude outros em apuros com o cups, hplip, hpcups e
outros tantos pacotes destinados a resolver problemas de instalação de
impressoras no linux.

Abraços!  
 

