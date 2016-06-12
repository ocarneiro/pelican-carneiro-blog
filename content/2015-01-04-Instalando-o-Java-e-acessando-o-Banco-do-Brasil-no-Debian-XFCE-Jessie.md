Tags: debian, linux, tutorial
Title: Instalando o Java e acessando o Banco do Brasil no Debian XFCE Jessie
Date: 2015-01-04 07:03
Author: Otávio Carneiro
Slug: Instalando-o-Java-e-acessando-o-Banco-do-Brasil-no-Debian-XFCE-Jessie

Há algum tempo eu escrevi um post sobre como utilizar o site do [Banco
do Brasil (bb.com.br) no
Ubuntu](http://umcarneiro.blogspot.com.br/2013/04/como-acessar-o-site-do-banco-do-brasil.html)
e ele foi um dos mais lidos deste blog.

Agora que estou usando o [Debian XFCE
Jessie](http://umcarneiro.blogspot.com/2014/11/deixando-o-debian-xfce-bonito.html)
(futuro Debian 8), fui entrar no site do banco e o site ficou com a tela
toda em branco, escrito "Aguarde, iniciando o acesso..." e sem nenhuma
outra mensagem.

Imaginei que podia ser a falta do Java ou do plugin do Java e fui
investigar.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-7jhM11fQGdo/VK-tlDNWHRI/AAAAAAAACdw/MAjfy7EGkcM/s1600/bb_branco.png)](http://2.bp.blogspot.com/-7jhM11fQGdo/VK-tlDNWHRI/AAAAAAAACdw/MAjfy7EGkcM/s1600/bb_branco.png)

</div>

Tentei usar o mesmo procedimento do meu post anterior e descobri não ser
possível, então resolvi escrever este novo post.

Na verdade, acessar sites que usam Java no Debian se mostrou muito mais
fácil. Você só tem que instalar dois pacotes: openjdk e icedtea-plugin.

Vá em Menu de aplicativos -\> Sistema -\> Gerenciador de pacotes
Synaptic e Pesquise "openjdk". A pesquisa vai encontrar dezenas de
pacotes, mas o que queremos é o que tem "jre" (Java runtime engine) e
mais nada. No meu caso, encontrei o openjdk-7-jre.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-XaDkzwYJEWE/VKlU3MJLtWI/AAAAAAAACdE/SIFdNg19er4/s1600/openjdk.png)](http://1.bp.blogspot.com/-XaDkzwYJEWE/VKlU3MJLtWI/AAAAAAAACdE/SIFdNg19er4/s1600/openjdk.png)

</div>

Talvez até você já tivesse esse pacote instalado (eu já tinha), mas
ainda fica faltando o plugin para o browser. É aí que entra o
icedtea-plugin.

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-OswMVOI5lSo/VKlWD_-brmI/AAAAAAAACdQ/Y_lIUZ2GAsg/s1600/icedtea-plugin.png)](http://2.bp.blogspot.com/-OswMVOI5lSo/VKlWD_-brmI/AAAAAAAACdQ/Y_lIUZ2GAsg/s1600/icedtea-plugin.png)

</div>

Siga o mesmo procedimento acima, entre no Synaptic e busque
icedtea-plugin. A descrição não é lá tão elucidativa, mas explica:

"IcedTeaPlugin é uma extensão para navegador web para executar 
miniaplicativos Java, suportando LiveConnect/Javascript. Ele é
direcionado  
para xulrunner-1.9 e navegadores compatíveis que suportem o NPAPI."

Ou seja, o IcedTeaPlugin é o plugin do Java!

Depois de instalar o icedtea, o site do BB pediu várias permissões.

Primeiro, ele pediu para eu permitir o complemento do IcedTea-Web. Eu
cliquei em Permitir (Allow) e depois em Permitir e Memorizar (Allow and
Remember).

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-NiwijARyb24/VK-uIUigisI/AAAAAAAACd4/Z96dwlnH2rw/s1600/bb-permitir.png)](http://3.bp.blogspot.com/-NiwijARyb24/VK-uIUigisI/AAAAAAAACd4/Z96dwlnH2rw/s1600/bb-permitir.png)

</div>

   
Na tela seguinte, o site pediu para eu confirmar permissão para o Módulo
de Segurança do Banco do Brasil, já que ele usa recursos de dois outros
locais.

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-SRJSpt6cgU8/VKlX8QPzzpI/AAAAAAAACdc/zVqH49LqTFs/s1600/Modulo_Seguranca_Banco_Brasil_aapf_idh.png)](http://3.bp.blogspot.com/-SRJSpt6cgU8/VKlX8QPzzpI/AAAAAAAACdc/zVqH49LqTFs/s1600/Modulo_Seguranca_Banco_Brasil_aapf_idh.png)

</div>

A mensagem exata é a seguinte:

The application Modulo de Seguranca Banco do Brasil from
https://www2.bancobrasil.com.br/aapf/login.jsp?aapf.IDH=sim&perfil;=6
resources from the following remote locations:

-   www2.bancobrasil.com.br/aapf e
-   www2.bancobrasil.com.br/aapf/idh

Are you sure you want to run this application?

Eu respondi que sim (Yes) e o site entrou normalmente.

Abs.,  
Otávio

