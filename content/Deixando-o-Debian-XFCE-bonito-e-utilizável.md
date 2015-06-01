Title: Deixando o Debian XFCE bonito e utilizável
Date: 2014-11-27 15:33
Author: Otávio Carneiro
Slug: Deixando-o-Debian-XFCE-bonito-e-utilizável

Logo que você instala o Debian 8 Jessie (ou o Debian 7 Wheezy com XFCE),
você fica com um Linux horroroso que não dá nenhuma vontade de usar.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-qNvbiufg_2Q/VHenSBbR8AI/AAAAAAAACXQ/9fzYo_Vfrmo/s1600/Captura%2Bde%2Btela%2B-%2B27-11-2014%2B-%2B20%3A32%3A44.png)](http://1.bp.blogspot.com/-qNvbiufg_2Q/VHenSBbR8AI/AAAAAAAACXQ/9fzYo_Vfrmo/s1600/Captura%2Bde%2Btela%2B-%2B27-11-2014%2B-%2B20%3A32%3A44.png)

</div>

Além de feio e esquisito, ele vêm com um browser estranho, um tal de
Iceweasel que é uma versão bizarra do Firefox. Vou te ensinar a se
livrar dele, mas antes vou executar algumas tarefas mais urgentes.

Muitas dicas eu tirei [desse site em
inglês](http://dontsurfinthenude.blogspot.com.br/2013/06/10-things-to-do-after-installing-debian.html),
mas vou reproduzir aqui em português e explicar alguma eventual
dificuldade que tive.

Primeiro, vá em Menu de aplicativos -\> Sistema -\> Gerenciador de
pacotes Synaptic. Vou chamar esse programa só de Synaptic daqui para
frente.

Dentro do Synaptic, vá em Configurações -\> Repositórios.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-q5OdyPL180A/VHeoW8Dd3sI/AAAAAAAACXg/y6LvdkH4J0o/s1600/synaptic.png)](http://2.bp.blogspot.com/-q5OdyPL180A/VHeoW8Dd3sI/AAAAAAAACXg/y6LvdkH4J0o/s1600/synaptic.png)

</div>

Marque as caixas "Aplicativos compatíveis com a DFSG mas com
dependências não-livres (contrib)" e "Aplicativos não compatíveis com a
DFSG (non-free)". Isso vai te permitir instalar programas não livres.
Aproveite e clique em "Other Software" e desmarque o CD-Rom. Clique em
Fechar.

<div class="separator" style="clear: both; text-align: center;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-xZuJzq4gorE/VHeoWq0e41I/AAAAAAAACXc/oHJ0p968VlY/s1600/non-free.png)](http://3.bp.blogspot.com/-xZuJzq4gorE/VHeoWq0e41I/AAAAAAAACXc/oHJ0p968VlY/s1600/non-free.png)

</div>

Clique no botão Recarregar.

Agora você já pode clicar na lupa e procurar pacotes de drivers não
livres de que você precisa. Quase todos os micros usam placas de rede
Realtek e o linux reclama da falta de um driver. No meu ficava assim:

[   12.244689] r8169 0000:03:00.0: firmware: agent aborted loading
rtl\_nic/rtl8168e-3.fw (not found?)  
[   12.244790] r8169 0000:03:00.0: eth0: unable to load firmware patch
rtl\_nic/rtl8168e-3.fw (-2)

Esse driver (assim como outros da Realtek) está em um pacote chamado
"firmware-realtek".

Se você tiver uma placa de vídeo Radeon ou outro equipamento que
desconfia que não está bem instalado, procure o pacote "firmware-linux".
Ele contém diversos drivers de vários fabricantes.

Para instalar qualquer programa, você clica com o botão direito nele e
escolhe "Marcar para instalação". Depois clica em "Aplicar".

Hora de deixar o Linux mais bonito! Vá em "Menu de aplicativos" -\>
Configurações -\> Aparência.

Escolha um Estilo de que goste. Eu gostei da Adwaita, mas preferi
aumentar a fonte. Deixei Sans, mas com fonte 12 (o padrão é 10).

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-rfwO3FjmDyM/VHev04ARgII/AAAAAAAACX0/cm9MO_cbVQk/s1600/aparencia.png)](http://1.bp.blogspot.com/-rfwO3FjmDyM/VHev04ARgII/AAAAAAAACX0/cm9MO_cbVQk/s1600/aparencia.png)

</div>

Hora de ajustar o papel de parede e o tamanho dos ícones no desktop.
"Menu de Aplicativos" -\> Configurações -\> "Área de Trabalho". Eu
escolhi ícones gigantes (54) no lugar do padrão (36). Coloquei também o
papel de parede Aquarius.svg no lugar do default (ou do xfce-stripes).

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-ZdSbJmn7r6k/VHev1IbC0kI/AAAAAAAACX4/g9n5oQXu9O0/s1600/area_de_trabalho.png)](http://2.bp.blogspot.com/-ZdSbJmn7r6k/VHev1IbC0kI/AAAAAAAACX4/g9n5oQXu9O0/s1600/area_de_trabalho.png)

</div>

Eu fico muito confuso com os "Espaços de trabalho" do Linux. Você pode
abrir programas em várias "telas" e depois ficar navegando por essas
telas. Eu acho isso esquisito e prefiro ficar com uma tela só. Para
desligar, vá para "Menu de Aplicativos" -\> Configurações -\> "Espaços
de Trabalho". Defini o Número de espaços de trabalho como 1.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-PoGZHNN59RM/VHexWeml79I/AAAAAAAACYI/J10yNH3UsiQ/s1600/espacos_de_Trabalho.png)](http://2.bp.blogspot.com/-PoGZHNN59RM/VHexWeml79I/AAAAAAAACYI/J10yNH3UsiQ/s1600/espacos_de_Trabalho.png)

</div>

Como tirei os outros espaços, posso tirar o seletor de espaço do painel
(aquela barra no topo da tela). Para alterar um painel (o XFCE vem com
dois deles), clique com o botão direito no painel, em  Painel e em
"Preferências do painel". Selecione o "Alternador de espaço de trabalho"
em Itens e clique no sinal de menos (-) para removê-lo.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-JDVN-KNtnHU/VHeyFXqJv9I/AAAAAAAACYQ/Dt7xDzL-d10/s1600/painel1.png)](http://2.bp.blogspot.com/-JDVN-KNtnHU/VHeyFXqJv9I/AAAAAAAACYQ/Dt7xDzL-d10/s1600/painel1.png)

</div>

Aproveite que está aí e mexa na posição e quantidade de painéis. Na
barra de seleção no topo da janela, selecione o Painel 2. Clique no
sinal de menos (-) para removê-lo também. No painel 1, eu aumentei o
tamanho da barra para 46 e desmarquei o "trancar painel". Assim, eu
posso arrastar a barra pegando pelas "alças" nos cantos dela. Arrastei
para baixo.

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-qIrYe5uo3lo/VHezW1ZG0TI/AAAAAAAACYc/Z0LSbxt_JfU/s1600/painel2.png)](http://4.bp.blogspot.com/-qIrYe5uo3lo/VHezW1ZG0TI/AAAAAAAACYc/Z0LSbxt_JfU/s1600/painel2.png)

</div>

Como aumentei o tamanho de vários botões, o menu dos programas ficou
pequeno em comparação com o resto. Para aumentá-lo, vá em "Menu de
aplicativos" -\> Configurações -\> "Gerenciador de Janelas".

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-lJb6wUm_4Es/VHe2NL_sj0I/AAAAAAAACYo/m8mV2QiCH1w/s1600/janela.png)](http://3.bp.blogspot.com/-lJb6wUm_4Es/VHe2NL_sj0I/AAAAAAAACYo/m8mV2QiCH1w/s1600/janela.png)

</div>

Aumentei a fonte de título. Ficou "Sans Bold | 12" (era 9). Também
troquei o tema dos botões. Em Estilo, escolhi "RedmondXP" (Windows XP).
Ele ficou com uns botões grandes para minimizar, maximizar e fechar a
janela com um x vermelho.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-mMBFzNCIPBE/VHe3F6CKZFI/AAAAAAAACYw/ESRi20L-NDk/s1600/superd.png)](http://2.bp.blogspot.com/-mMBFzNCIPBE/VHe3F6CKZFI/AAAAAAAACYw/ESRi20L-NDk/s1600/superd.png)

</div>

Aproveitei e cliquei em Teclado e mudei o botão de "Mostrar área de
trabalho". Coloquei <super>d (ou tecla do Windows + d), para ficar igual
ao do computador do trabalho (que usa Windows 7).

Para mudar algum atalho é só você só achar o item que quer trocar e
clicar duas vezes. Aí ele fica esperando você digitar o atalho que
escolheu.

Outra coisa que eu gosto de fazer é deixar o computador funcionar sem
senha. Eu prefiro que o pessoal daqui de casa consiga fazer coisas
normais com meu usuário (como acessar a internet e jogar minecraft) do
que criar uma senha para cada um. Para isso, você precisa configurar o
autologin.

O problema é que o Debian não vem com um jeito fácil de fazer isso. Você
tem que usar uma [linha de
comando](http://www.vivaolinux.com.br/topico/Debian/auto-login-debian-7-xfce/)
que faz isso, mas é fácil de errar e estragar alguma coisa desse jeito.
Preferi fazer [em
etapas](http://www.dailylinuxnews.com/blog/2014/09/things-to-do-after-installing-debian-jessie/):  
1) Instalar o sudo (pasme! o Debian não vem com o sudo instalado)

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-gupzCATTL88/VHe8aLHpFAI/AAAAAAAACZA/QVgsMvYjtkw/s1600/sudo.png)](http://3.bp.blogspot.com/-gupzCATTL88/VHe8aLHpFAI/AAAAAAAACZA/QVgsMvYjtkw/s1600/sudo.png)

</div>

 \*Obs: meu Synaptic queria instalar o "sudo" de um CD. Como nunca tive
um CD do Debian, fui em "Configurações" -\> Repositórios -\> "Other
software" e desmarquei a caixa do cd-rom. Fechei a janela e cliquei
Recarregar. Aí deu para instalar normal.

1.1. Clique na lupa e digite "sudo" (busque só por Nome, para
restringir);  
1.2. Procure o sudo na lista e clique sobre ele com o botão direito;  
1.3. Selecione "Marcar para instalação";  
1.4. Clique em aplicar.

2\) Dar acesso ao seu usuário para utilizar o sudo:  
2.1. Abra um terminal ("Menu de Aplicativos" -\> "Emulador de
Terminal").  
2.2. Escreva "su" e aperte enter.  
2.3. Digite a senha de root. (provavelmente pela última vez)  
2.4. Escreva "usermod -a -G sudo seu\_usuario" (trocando seu\_usuario
pelo seu login);  
2.5. Reinicie o computador.

3\) Mude o arquivo de configuração do lightdm  
3.1. Abra um terminal ("Menu de Aplicativos" -\> "Emulador de
Terminal");  
3.2. Escreva "sudo nano /etc/lightdm/lightdm.conf" e confirme com sua
senha;  
3.3. Desça a tela (com a seta para baixo do teclado) até achar
[SeatDefaults] (com os colchetes);  
3.4. Várias linhas abaixo (pouco acima de "\#Seat configuration", você
vai ver duas linhas assim:  
  \#autologin-user=  
  \#autologin-user-timeout=0  
3.5. Apague o cerquilha ("\#") dessas duas linhas. Na primeira, escreva
seu login:  
  autologin-user=seu\_usuario  
  autologin-user-timeout=0  
3.6. Aperte Ctrl+X para sair. Confirme que quer salvar o buffer com "S"
e aperte Enter quando ele perguntar o nome do arquivo.  
3.7. Pronto! Agora você pode reiniciar o computador de novo e perceberá
que não precisa mais colocar seu usuário e senha.

E os itens do painel?

Para item inicial, gostei do Menu Whisker:  
<http://gottcode.org/xfce4-whiskermenu-plugin/>

Ele se parece com o botão Iniciar do Windows 7 ou com o menu inicial do
Linux Mint. Eu acho muito mais fácil de usar, pois tem uma barra para
procurar programas.

Também gosto de ter ali na barra um terminal pronto para uso e o
browser.

Para instalar o Firefox no Debian, usei essa dica aqui:  
<http://www.whaleblubber.ca/install-firefox-debian/>

1\) Primeiro você baixa a versão que você quer. Eu queria a versão Linux
64-bit em português do Brasil:
<https://www.mozilla.org/en-US/firefox/all/?q=Portuguese%20%28Brazilian%29,%20Portugu%C3%AAs%20%28do%C2%A0Brasil%29>

<div class="separator" style="clear: both; text-align: center;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-Zy2stMl6_H4/VHfX_dAaXkI/AAAAAAAACZo/tSKcekc5tJo/s1600/download_ff.png)](http://3.bp.blogspot.com/-Zy2stMl6_H4/VHfX_dAaXkI/AAAAAAAACZo/tSKcekc5tJo/s1600/download_ff.png)

</div>

2\) Cliquei para Salvar e abri a pasta Downloads. Lá, cliquei com o botão
direito na janela e escolhi "Abrir terminal aqui".

3\) Dentro do terminal, você descompacta o arquivo que baixou:  
    tar xjf firefox-\*

4\) Isso vai criar uma pasta ali mesmo, que você deve mover para /opt/
com esse comando:  
    sudo mv firefox /opt/firefox

5\) E então você cria um link para este diretório na pasta de programas
(/usr/bin) assim:  
    sudo mv /usr/bin/firefox /usr/bin/firefox.old  
(isso tira o tal do iceweasel do lugar onde queremos o firefox)  
    sudo ln -s /opt/firefox/firefox /usr/bin/firefox  
(isso cria o link. Tem dois firefox no começo do comando, é assim mesmo)

6\) Agora você já pode dizer para o Debian que o firefox é um browser:  
    sudo update-alternatives --install /usr/bin/x-www-browser
x-www-browser /usr/bin/firefox 90

7\) E depois é só rodar o Firefox uma vez com sudo:  
    sudo firefox

[![](http://2.bp.blogspot.com/-RBE1aDEWtvU/VHfdv32MXdI/AAAAAAAACZ4/xEIX-3xVMd8/s1600/menu_ff.png)](http://2.bp.blogspot.com/-RBE1aDEWtvU/VHfdv32MXdI/AAAAAAAACZ4/xEIX-3xVMd8/s1600/menu_ff.png)  
Como colocamos o programa na pasta /opt/, seu usuário normal pode não
conseguir atualizá-lo, então recomendo que você olhe de vez em quando se
o Firefox está atualizado pelo menu Ajuda/Sobre o Firefox.

Nesta primeira execução, deixe somente o Firefox atualizar (ou te dizer
que já está atualizado) e feche a janela. Ao executar um programa com
"sudo" você está usando o perfil de root, que não é apropriado para
tarefas do dia a dia.

Para usar normalmente o browser, você pode usar a opção "Navegador web"
do menu do XFCE.

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-jmAFXFf9gHg/VHfeCvmXB0I/AAAAAAAACaA/W2JNatvNJBE/s1600/ff_atual.png)](http://4.bp.blogspot.com/-jmAFXFf9gHg/VHfeCvmXB0I/AAAAAAAACaA/W2JNatvNJBE/s1600/ff_atual.png)

</div>

Pronto. Com estas dicas, seu Linux já deve ter ficado com uma cara
bonita e mais agradável de se usar. Depois vou acrescentando dicas aqui
se achar que preciso mudar mais coisas.

Abraços!

</super>

