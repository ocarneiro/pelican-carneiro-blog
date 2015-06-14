Title: Toque e clique no touchpad
Date: 2015-06-14 13:55
Author: Otávio Carneiro
Slug: Toque-e-clique-no-touchpad
Tags: debian, tutorial

Fui usar o Debian 8 em um notebook mais antigo e ele instalou perfeitamente, de primeira. O único porém é que o touchpad (aquela superfície que a gente usa como mouse) não reconhecia toques rápidos como cliques. 

Para explicar melhor. Praticamente todos os notebooks hoje em dia têm aquela área abaixo do teclado em que você pode passar o dedo para movimentar o cursor. Alguns até são multitouch e aceitam gestos, tipo arrastar com dois dedos para rolar a tela, arrastar com três dedos para trocar de programa, pinch-to-zoom (fazer movimento de pinça para dar zoom) e etc. Pois é, esta área é conhecida como touchpad.

O hardware mais conhecido de touchpad é o Synaptics. Se precisar buscar soluções para isso, vale usar esta palavra chave.

No meu caso, a solução para usar o toque como o clique eu achei neste fórum: [http://forums.fedoraforum.org/showthread.php?t=282700](http://forums.fedoraforum.org/showthread.php?t=282700)

A ideia ali é basicamente criar um arquivo em "/etc/X11/xorg.conf.d/" chamado "10-synaptics.conf".

A tal pasta xorg.conf.d não existia no meu caso, então fiz o seguinte:

    :::bash
    sudo mkdir /etc/X11/xorg.conf.d
    sudo mousepad /etc/X11/xorg.conf.d/10-synaptics.conf
    
Isso fez com que o mousepad (equivalente ao notepad) criasse um arquivo novo e o abrisse como root.

Se o "sudo" não estiver funcionando, veja meu outro post sobre como [instalar o sudo no Debian 8]({filename}/2015-02-01-Como-instalar-e-usar-o-sudo-no-Debian-8-Jessie.md).

Dentro do arquivo, colei o seguinte código:

    Section "InputClass"  
    		Identifier "touchpad catchall"  
    		Driver "synaptics"  
    		MatchIsTouchpad "on"  
    		MatchDevicePath "/dev/input/event*"  
    		Option "TapButton1" "1"  
    		Option "TapButton2" "2"  
   			Option "TapButton3" "3"  
    		Option "VertTwoFingerScroll" "on"  
    		Option "HorizTwoFingerScroll" "on"  
    EndSection  

Aí é só salvar o arquivo e reiniciar o computador.

Repare que de quebra você ganha um gesto: o de arrastar com dois dedos para rolar a tela na vertical ou horizontal.

Bom proveito!

Abraço!  
Otávio
