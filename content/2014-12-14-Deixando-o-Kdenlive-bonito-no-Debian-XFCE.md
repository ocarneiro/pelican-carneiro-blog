Tags: debian, linux, tutorial
Title: Deixando o Kdenlive bonito no Debian XFCE
Date: 2014-12-14 04:43
Author: Otávio Carneiro
Slug: Deixando-o-Kdenlive-bonito-no-Debian-XFCE

Quem acompanha [meu canal no
YouTube](https://www.youtube.com/user/UmCarneiro)sabe que eu tenho usado
o Openshot para editar vídeos (no final de cada vídeo sempre indico os
softwares utilizados).

O [Openshot](http://www.openshot.org/) é um software fácil e bonito, mas
tem uns [bugs muito
irritantes](http://cweiske.de/tagebuch/avoid-openshot.htm).

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-0GWA79xcPYc/VI19Nn6QyOI/AAAAAAAACaY/Ztf4U8QtWxo/s1600/openshot.png)](http://4.bp.blogspot.com/-0GWA79xcPYc/VI19Nn6QyOI/AAAAAAAACaY/Ztf4U8QtWxo/s1600/openshot.png)

</div>

Fui procurar alternativas e encontrei o
[Kdenlive](https://kdenlive.org/).

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-3XynxYkHH84/VI1-FbnARPI/AAAAAAAACao/dbTdTpfY31M/s1600/kdenlive-depois.png)](http://2.bp.blogspot.com/-3XynxYkHH84/VI1-FbnARPI/AAAAAAAACao/dbTdTpfY31M/s1600/kdenlive-depois.png)

</div>

O Kdenlive parece muito promissor, mas na instalação inicial ele é
feioso demais. É frescura, eu sei, mas você ficar usando todos os dias
um programa feio desmotiva qualquer um. Ainda mais depois de ter se
esforçado para [deixar o restante do sistema operacional
bonito](http://umcarneiro.blogspot.com.br/2014/11/deixando-o-debian-xfce-bonito.html).

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-l87Ut_YgYyQ/VI1951uctwI/AAAAAAAACag/D2hRGBCHgZk/s1600/kdenlive-antes.png) ](http://3.bp.blogspot.com/-l87Ut_YgYyQ/VI1951uctwI/AAAAAAAACag/D2hRGBCHgZk/s1600/kdenlive-antes.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

Lá fui eu, então, procurar um jeito de embelezar o Kdenlive. Tem um
artigo bem completo e em português no [blog "Grita!
(Ricolândia)"](http://grita.ricolandia.com/2014/04/04/gtk-e-qt-mesma-aparencia-e-icones/),
mas vou dar algumas dicas aqui também.

O que você tem que fazer é instalar alguns pacotes de configuração
visual do KDE. Alguns deixam bem claro na descrição a que se destinam:

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-FY1__XWQUio/VI1_MswdVXI/AAAAAAAACa0/0Q_yhMkY6Do/s1600/synaptic.png)](http://1.bp.blogspot.com/-FY1__XWQUio/VI1_MswdVXI/AAAAAAAACa0/0Q_yhMkY6Do/s1600/synaptic.png)

</div>

**gtk2-engines-oxygen**  
"Garante consistência visual entre GTK+ e aplicações baseadas em Qt sob
o KDE". Traduzi do inglês e ainda não dá para entender nada, né? Instale
e confie!

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-dYp16lRebr8/VI1_uRlBI7I/AAAAAAAACa8/RyoHavI-uv0/s1600/kde-config-gtk-synaptic.png)](http://4.bp.blogspot.com/-dYp16lRebr8/VI1_uRlBI7I/AAAAAAAACa8/RyoHavI-uv0/s1600/kde-config-gtk-synaptic.png)

</div>

**kde-config-gtk-style**  
"Janela para adaptar a aparência de aplicações GTK+ ao seu gosto sob o
KDE". Ficou claro? Pois é.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-TGnZCf4Ogjw/VI2ANTVcWLI/AAAAAAAACbI/R5WkGsfS8qg/s1600/synaptic-qtconfig.png)](http://2.bp.blogspot.com/-TGnZCf4Ogjw/VI2ANTVcWLI/AAAAAAAACbI/R5WkGsfS8qg/s1600/synaptic-qtconfig.png)

</div>

**qt4-qtconfig**  
"Qt é uma infraestrutura interplataforma de aplicações C++. O principal  
recurso da Qt é o seu rico conjunto de widgets que fornecem
funcionalidades padrões para a interface gráfica do usuário (GUI).

O programa de configuração da Qt permite que os usuários configurem a  
aparência e o comportamento de qualquer aplicativo desenvolvido em Qt
4."

Taí uma explicação interessante! Na verdade, todo programa que roda no
ambiente gráfico precisa saber como desenhar na tela. Ao invés do
programador escrever que o computador deve desenhar um retângulo aqui
para escrever o título e um círculo ali para ser um botão, ele utiliza
uma biblioteca. Uma biblioteca é um conjunto de programas com uma função
específica. GTK+ e Qt são duas bibliotecas bastante populares que cuidam
de toda a parafernália necessária para desenhar janelas, botões, ícones
e afins, permitindo que os programadores cuidem da funcionalidade do seu
próprio programa ao invés de se preocupar com geometria e pixels.

Pois bem, com estes programas você já consegue fazer uma configuração
básica.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-lXYavVA-PVw/VI2Bscd-OYI/AAAAAAAACbU/5mU0eWSygvE/s1600/qtconfig.png)](http://1.bp.blogspot.com/-lXYavVA-PVw/VI2Bscd-OYI/AAAAAAAACbU/5mU0eWSygvE/s1600/qtconfig.png)

</div>

Indo em "Menu de aplicativos" -\> Configurações -\> "Configurações do Qt
4", você já pode dizer que o estilo que você quer utilizar é o mesmo que
das outras aplicações. Ou seja, você pode mudar o "GUI Style" para
"GTK+".

Isso já vai ajudar um bocado, ajustando as cores e os ícones para o tema
que você tinha configurado para o XFCE. Mas as letras continuam
minúsculas (fonte 8).

Para ajustar isso, você tem que instalar mais um pacote.

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-bw2c2omrk7M/VI2CwVmXsvI/AAAAAAAACbg/MdhrAk51HxQ/s1600/systemsettings-kde-synaptic.png)](http://4.bp.blogspot.com/-bw2c2omrk7M/VI2CwVmXsvI/AAAAAAAACbg/MdhrAk51HxQ/s1600/systemsettings-kde-synaptic.png)

</div>

**systemsettings**  
"System Settings é uma interface de usuário aprimorada para configurar a
área de trabalho e outros aspectos do sistema."  
[![](http://4.bp.blogspot.com/-z_ojYFWYJpo/VI2D7KaNBOI/AAAAAAAACbs/Ezu_6skTn6U/s1600/systemsettings-kde.png)](http://4.bp.blogspot.com/-z_ojYFWYJpo/VI2D7KaNBOI/AAAAAAAACbs/Ezu_6skTn6U/s1600/systemsettings-kde.png)Na
verdade, o systemsettings é um configurador do ambiente KDE (uma
alternativa ao XFCE que estamos utilizando no resto do sistema). Só que
vamos usá-lo para configurar a aparência de programas do KDE (como o
Kdenlive) no nosso ambiente XFCE.

Como o systemsettings não é um programa feito para rodar no Debian XFCE,
ele não aparece no Menu de Aplicativos, você tem que rodá-lo do
terminal. Calma, você só executa ele de lá, mas configura numa janela
normal. Abra um terminal e digite systemsettings.

Agora, sim!

Você já pode ir lá e configurar o tamanho das fontes. Você pode até
deixar o kdenlive aberto. Quando você clicar "Apply" (Aplicar), as
mudanças já serão visíveis no kdenlive. Eu coloquei letras com tamanho
12 para tudo.

No mesmo programa você pode alterar também cores, ícones e outras
coisas, mas eu só aumentei a fonte.

Dentro do kdenlive eu ainda fechei a janela "Transição" e aumentei as
outras arrastando-as pelos cantos. É, ficou mais parecido com o
Openshot, eu sei, mas o que eu queria era facilitar a minha vida para
poder publicar mais vídeos para vocês.

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-3XynxYkHH84/VI1-FbnARPI/AAAAAAAACas/owrzAAadaSU/s1600/kdenlive-depois.png)](http://4.bp.blogspot.com/-3XynxYkHH84/VI1-FbnARPI/AAAAAAAACas/owrzAAadaSU/s1600/kdenlive-depois.png)

</div>

Abraços!  
Otávio

