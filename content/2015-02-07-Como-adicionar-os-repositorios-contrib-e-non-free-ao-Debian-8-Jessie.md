Tags: debian, linux, tutorial
Title: Como adicionar os repositórios contrib e non-free ao Debian 8 (Jessie)
Date: 2015-02-07 13:40
Author: Otávio Carneiro
Slug: Como-adicionar-os-repositórios-contrib-e-non-free-ao-Debian-8-(Jessie)

Demorei um pouco para me acostumar com o Gerenciador de Pacotes
(Synaptic) do Debian 8 (Jessie). Minha versão do Synaptic é a 0.81.2.

Depois de apanhar um bocado, finalmente descobri como adicionar os
repositórios contrib e non-free, necessários para a instalação do pacote
hannah-foo2zjs (que usei para [configurar minha impressora no
Debian](http://umcarneiro.blogspot.com.br/2014/11/instalar-impressora-hp-laserjet-1020-no.html))
e outros.

Em versões anteriores, havia um checkbox em que você marcava estes
repositórios, mas agora você precisa digitar na área "Seção(ões)".

Fica assim:  
URI: http://ftp.br.debian.org/debian/  
Distribuição: jessie  
Seção(ões): non-free contrib main

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-D2So8FEhgSg/VNaFwI48DZI/AAAAAAAAChg/nt7M62tKdIc/s1600/synaptic-repositorios.jpg)](http://2.bp.blogspot.com/-D2So8FEhgSg/VNaFwI48DZI/AAAAAAAAChg/nt7M62tKdIc/s1600/synaptic-repositorios.jpg)

</div>

Parece bobo, mas achei que merecia um post.

Abraços,  
Otávio

