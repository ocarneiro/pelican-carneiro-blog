Title: Como acessar o site do Banco do Brasil no Ubuntu 12.04
Date: 2013-04-30 08:18
Author: Otávio Carneiro
Slug: Como-acessar-o-site-do-Banco-do-Brasil-no-Ubuntu-12.04

[  
![](http://1.bp.blogspot.com/-A3l7ePaC4xE/UX_Vd51RITI/AAAAAAAABOw/Qmts016vo2U/s320/InstalarJava-00-BancoDoBrasilsemJava.png)](http://1.bp.blogspot.com/-A3l7ePaC4xE/UX_Vd51RITI/AAAAAAAABOw/Qmts016vo2U/s1600/InstalarJava-00-BancoDoBrasilsemJava.png)  
**Atualização (jan/2015):** [Procedimento para acessar o BB no Debian
Jessie
XFCE](http://umcarneiro.blogspot.com.br/2015/01/instalando-o-java-e-acessando-o-banco.html)

Pessoal,

Estou usando o Ubuntu 12.04 no desktop de casa e, na hora de acessar o
site (sítio?) do Banco do Brasil, notei que não tinha o Java instalado.
Procurei na Central de Programas do Ubuntu e não tinha Java por lá. E
agora? Procuremos na internet...

Achei o [Blog do Alexandre di
Salvo](http://alexandredisalvo.wordpress.com/2012/05/01/instalando-java-7-no-ubuntu-12-04-serve-para-banco-do-brasil-tambem/),
em que ele ensina a instalar o Java 7, mas ele usa linhas de comando.
Como sei que muita gente tem medo das telas com fundo preto e letras
brancas desde a primeira vez que usaram o "DOS", achei melhor ensinar
aqui a fazer a mesma coisa usando a interface gráfica...

[![](http://2.bp.blogspot.com/-Gu1XNKDTIIs/UX_Kz8NLxYI/AAAAAAAABNg/iHIS9HvLIv0/s320/InstalarJava-01-Canais.png)](http://2.bp.blogspot.com/-Gu1XNKDTIIs/UX_Kz8NLxYI/AAAAAAAABNg/iHIS9HvLIv0/s1600/InstalarJava-01-Canais.png)A
primeira coisa a fazer é adicionar um canal de software à Central do
Ubuntu. Isso é algo a ser feito com cautela. Um canal de software é um
repositório de programas que a Central de Programas vai usar quando você
estiver querendo instalar alguma coisa. É bom sempre dar uma pesquisada
antes de adicionar qualquer coisa a seus canais, pois além de software
maliciosos, você pode instalar algum software que cause
incompatibilidade com o seu sistema e deixá-lo instável.  
<span id="goog_269492698"></span><span id="goog_269492699"></span>

O repositório indicado pelo Alexandre é o do [WebUpd
8](http://www.webupd8.org/), que parece ter [boa reputação na
internet](http://askubuntu.com/questions/143708/should-i-trust-these-packages-and-ppas),
então eu o adicionei.

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-Nsx6woNcv-w/UX_K9zQ2EqI/AAAAAAAABNo/mG37NJW5xvQ/s320/InstalarJava-02-adicionar.png)](http://3.bp.blogspot.com/-Nsx6woNcv-w/UX_K9zQ2EqI/AAAAAAAABNo/mG37NJW5xvQ/s1600/InstalarJava-02-adicionar.png)[![](http://3.bp.blogspot.com/-f3wIm7fjm1g/UX_K_mssV9I/AAAAAAAABNw/ByAQN_7Gy3U/s320/InstalarJava-03-FonteWebuod8team.png)](http://3.bp.blogspot.com/-f3wIm7fjm1g/UX_K_mssV9I/AAAAAAAABNw/ByAQN_7Gy3U/s1600/InstalarJava-03-FonteWebuod8team.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

Para fazer isso, entre na Central de Programas do Ubuntu, clique em
Editar -\> Canais de Software -\> Outros Programas -\> Adicionar -\>
ppa:webupd8team/java

Depois de adicionar este Canal, pode ser necessário atualizar a lista de
repositórios do Ubuntu. Para fazer isso, basta entrar no Gerenciador de
Atualizações e clicar em Verificar.

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-jgAG3LDzJW8/UX_QSb-c1GI/AAAAAAAABOA/RlN1LsTW2mA/s320/InstalarJava-05-GerenciadorAtualizacoes.png)](http://3.bp.blogspot.com/-jgAG3LDzJW8/UX_QSb-c1GI/AAAAAAAABOA/RlN1LsTW2mA/s1600/InstalarJava-05-GerenciadorAtualizacoes.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-b3H_8IVBVNU/UX_QSrO6lWI/AAAAAAAABOE/gwdlaTI-obk/s320/InstalarJava-06-Verificar.png) ](http://1.bp.blogspot.com/-b3H_8IVBVNU/UX_QSrO6lWI/AAAAAAAABOE/gwdlaTI-obk/s1600/InstalarJava-06-Verificar.png) 

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Agora você já pode voltar à Central de Programas do Ubuntu e procurar o
Java de novo. Ele é um "item técnico" (um programa usado por outros
programas), então você tem que clicar no link abaixo da janela: "Mostrar
XX itens técnicos".

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-eBpd14a5wKY/UX_Q4EzkZtI/AAAAAAAABOQ/MhDT4C2qM24/s320/InstalarJava-09-MostrarItensTecnicos.png)](http://1.bp.blogspot.com/-eBpd14a5wKY/UX_Q4EzkZtI/AAAAAAAABOQ/MhDT4C2qM24/s1600/InstalarJava-09-MostrarItensTecnicos.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

Pronto, agora você vai ver o Oracle Java (TM) Development Kit (JDK) 7.
Na realidade, precisaríamos só do JRE (Java Runtime Engine), mas isso é
o que temos. O JDK é o Java para quem escreve programas em Java. O JRE é
o Java para quem roda programas (e sites) que usam Java, então ele é bem
menor. Como não encontrei um JRE que possa ser instalado dessa forma,
vamos de JDK mesmo.

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-A07WyHlIvto/UX_Q4piaHAI/AAAAAAAABOY/cufNKbTNnJw/s320/InstalarJava-10-Java7.png)](http://1.bp.blogspot.com/-A07WyHlIvto/UX_Q4piaHAI/AAAAAAAABOY/cufNKbTNnJw/s1600/InstalarJava-10-Java7.png)

</div>

 

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-E6mSyQ4ALQs/UX_Q46OWBXI/AAAAAAAABOg/M8qNxl3djfY/s320/InstalarJava-11-Instalando.png)](http://2.bp.blogspot.com/-E6mSyQ4ALQs/UX_Q46OWBXI/AAAAAAAABOg/M8qNxl3djfY/s1600/InstalarJava-11-Instalando.png)

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Instalei o Java 7. Acabou? Ainda não, falta o plugin do Firefox...

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Procure por Plugin Java na Central de Programas do Ubuntu. Você deve
encontrar o Icedtea.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-N2fwxksdy4c/UX_WCual1LI/AAAAAAAABPA/yJa_fcDRmGI/s320/InstalarJava15-IcedTea.png)](http://4.bp.blogspot.com/-N2fwxksdy4c/UX_WCual1LI/AAAAAAAABPA/yJa_fcDRmGI/s1600/InstalarJava15-IcedTea.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Depois de instalá-lo, feche o Firefox (não esqueça de gravar este blog
nos favoritos antes disso ; ).

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Reabra o Firefox e volte ao site do Banco do Brasil. Dessa vez, ele vai
abrir uma janelinha cinza perguntando se pode executar o "jmid", criado
pelo Banco do Brasil. Clique "Executar".

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-xThGlksG4xI/UX_Wh1vFKOI/AAAAAAAABPI/R5TmjzrfcgI/s320/InstalarJava-17-jmid.png)](http://4.bp.blogspot.com/-xThGlksG4xI/UX_Wh1vFKOI/AAAAAAAABPI/R5TmjzrfcgI/s1600/InstalarJava-17-jmid.png)

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Na próxima tela, ele vai mostrar uma advertência perguntando se você
deseja bloquear a execução desse mesmo programa que você acabou de
permitir. Responda "Não". Atenção! Responda "Não", entendeu? Esse é
aquele tipo de pergunta de lógica "Você é contra a proibição do
desarmamento?", tem mais de uma negativa, mas o que você quer é
"permitir" a execução (de novo!), ou seja, "Não" bloquear.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-cKufBzr5bFU/UX_WwlPHXPI/AAAAAAAABPQ/Is57pAApMj4/s320/InstalarJava-16-Nao.png)](http://4.bp.blogspot.com/-cKufBzr5bFU/UX_WwlPHXPI/AAAAAAAABPQ/Is57pAApMj4/s1600/InstalarJava-16-Nao.png)

</div>

<div class="separator" style="clear: both; text-align: center;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Se você se confundiu (não te culpo) e respondeu que sim, você vai
precisar reiniciar o computador e entrar no site do Banco de novo. Desta
vez, clique "Executar" e "NÃO!". Aí, sim, vai funcionar.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://1.bp.blogspot.com/-_SNa_dRJYns/UX_XtzRMJNI/AAAAAAAABPc/1GvqUmrsvrk/s320/InstalarJava-17-BB.png)](http://1.bp.blogspot.com/-_SNa_dRJYns/UX_XtzRMJNI/AAAAAAAABPc/1GvqUmrsvrk/s1600/InstalarJava-17-BB.png)

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Pronto! Você já pode acessar o seu banco. 

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

**ATUALIZAÇÃO:** A partir de uma atualização ocorrida agora na segunda
quinzena de outubro de 2013, a pergunta que o Java faz antes de acessar
o sítio do Banco do Brasil mudou. Ao invés de perguntar se você quer
bloquear o JMID, ele mostra esta tela:

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-dyaUodCZ_fY/UnLR5Qp7JrI/AAAAAAAABhA/C13dfSJ-M80/s320/NovaTelaPermitirBB.png)](http://4.bp.blogspot.com/-dyaUodCZ_fY/UnLR5Qp7JrI/AAAAAAAABhA/C13dfSJ-M80/s1600/NovaTelaPermitirBB.png)

</div>

"Advertência de Segurança: Permitir acesso à aplicação a seguir por este
site?"  
Basicamente é a mesma pergunta que ele fazia antes, mas colocada de uma
maneira mais simples e com respostas que indicam claramente sua
intenção: "permitir" ou "não permitir".

**ATUALIZAÇÃO de maio/2014:** Recentemente, a mensagem mudou novamente.
Agora ela é assim:

<div class="separator" style="clear: both; text-align: center;">

[![](http://4.bp.blogspot.com/-XHQijVh3b6o/U2gXmOZe9JI/AAAAAAAAB6E/EWNeyuFpR-A/s1600/novaTela20140502.png)](http://4.bp.blogspot.com/-XHQijVh3b6o/U2gXmOZe9JI/AAAAAAAAB6E/EWNeyuFpR-A/s1600/novaTela20140502.png)

</div>

  "Deseja executar esta aplicação? Módulo de Segurança Banco do Brasil".
Agora você tem a opção de "Executar" ou "Cancelar" e mais: agora você
pode dizer para o Java não mostrar novamente esta tela. Parece que é o
fim das confirmações, não? Veremos.

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

**CONTINUANDO DO POST ORIGINAL:**

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Agora vem a pergunta que não quer calar: é seguro acessar o Internet
Banking dessa forma? Eu não queria ter que responder, mas não posso me
esquivar... 

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Quais são as brechas de segurança que existem entre você e o Internet
Banking? O maior perigo que eu vejo é a possibilidade de interceptação
dos seus dados bancários. Quais são as proteções contra isso?
Criptografia e certificação digital. Como saber se estas proteções estão
sendo aplicadas? Veja as informações apresentadas no ícone de cadeado do
Firefox. Vou tentar explicar algumas delas.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

[![](http://2.bp.blogspot.com/-sz5auqPsxk8/UX_aCXV5_oI/AAAAAAAABPs/03p5bQ2WwYc/s320/InstalarJava-20-cadeado.png)](http://2.bp.blogspot.com/-sz5auqPsxk8/UX_aCXV5_oI/AAAAAAAABPs/03p5bQ2WwYc/s1600/InstalarJava-20-cadeado.png)Ao
clicar no cadeado, você vai ver que a conexão é criptografada e que o
certificado digital é homologado pela VeriSign, que é uma conhecida
empresa do ramo de soluções de segurança, recentemente adquirida pela
Norton. 

</div>

<div class="separator" style="clear: both; text-align: justify;">

Você pode clicar no botão "Mais informações..." e obter mais detalhes.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-h1mjcozkBis/UX_atF2S73I/AAAAAAAABP0/krVtVim33ws/s320/InstalarJava-21-Seguranca.png)](http://3.bp.blogspot.com/-h1mjcozkBis/UX_atF2S73I/AAAAAAAABP0/krVtVim33ws/s1600/InstalarJava-21-Seguranca.png)

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Duas informações nesta tela são interessantes. 

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Na parte de Identidade do site, você vê que está acessando realmente
www2.bancobrasil.com.br. Por que isso é importante? Sites maliciosos
podem "personificar" o site do banco, mas não teriam a sua identidade
homologada pela VeriSign ou outra autoridade certificadora. Você pode
clicar em "Exibir certificado" e ver mais detalhes, de que vou falar
abaixo.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Na parte de Detalhes técnicos, você vê que a conexão está sendo
criptografada com uma criptografia de nível alto. Isso quer dizer que as
informações que você digita são codificadas e só podem ser lidas pelo
destinatário (o banco, no caso).

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Clicando em "Exibir certificado" você pode ver mais detalhes sobre o
certificado. Se tiver curiosidade, pode aprender um bocado sobre o
processo de certificação digital, que é muito interessante. Se não tiver
curiosidade, basta saber que o site foi certificado como pertencendo
realmente à empresa Banco do Brasil S.A. e que esse certificado foi
emitido por uma empresa de renome. 

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-l89IU96Uju4/UX_cdKBUzBI/AAAAAAAABQA/1t2-UvSg7w8/s320/InstalarJava-22-Certificado.png)](http://2.bp.blogspot.com/-l89IU96Uju4/UX_cdKBUzBI/AAAAAAAABQA/1t2-UvSg7w8/s1600/InstalarJava-22-Certificado.png)

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Resumindo, é seguro? Deixo para você decidir, pois não posso me
responsabilizar pelo que você faz ou não faz na internet. Também não sei
se qualquer pessoa usa o seu computador ou se todo mundo tem a sua senha
ou se seu browser está desatualizado ou qualquer outra situação de
risco. Só posso fazer recomendações:

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

1\) Não acesse o seu banco de qualquer computador. Mais importante: não
acesse o seu banco de lan houses ou telecentros. Se estiver fora de casa
e quiser fazer transações, vá ao banco.

</div>

<div class="separator" style="clear: both; text-align: justify;">

2\) Mantenha seu sistema operacional atualizado;

</div>

<div class="separator" style="clear: both; text-align: justify;">

3\) Mantenha seu browser atualizado;

</div>

<div class="separator" style="clear: both; text-align: justify;">

4\) Mantenha o Java atualizado. No caso do Linux, vale olhar a reputação
do Canal de Software de onde você instalou o Java. Se não tiver usado o
procedimento que indiquei (ou se estiver no Windows), tenha certeza de
que instalou o Java do site oficial (www.java.com).

</div>

<div class="separator" style="clear: both; text-align: justify;">

5\) Quando acessar sites de banco, dê uma olhada no cadeado. Não tem
cadeado? Não entre.

</div>

<div class="separator" style="clear: both; text-align: justify;">

6\) Clique no cadeado e veja se o site é do banco que você quer entrar
mesmo. O certificado é de outra empresa que não tem nada a ver? Não
entre.

</div>

<div class="separator" style="clear: both; text-align: justify;">

7\) Está na dúvida? Não entre.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Seguindo tudo isso, estarei seguro? Ainda assim não sei. Você pode estar
usando o site e ninjas alienígenas entrarem por sua janela e te forçarem
a comprar créditos para seus celulares intergaláticos. Se você imaginar
outro cenário de risco (antes ou depois do apocalipse zumbi), deixe um
comentário para ajudar outros leitores.

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Abraços,

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Otávio

</div>

<div class="separator" style="clear: both; text-align: justify;">

</div>

<div class="separator" style="clear: both; text-align: justify;">

Para ver posts semelhantes, clique no marcador "[home
banking](http://umcarneiro.blogspot.com.br/search/label/home%20banking)"

</div>
