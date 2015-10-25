Title: Como criar um componente para o Fritzing
Date: 2014-01-10 17:12
Author: Otávio Carneiro
Slug: 2014-01-10-como-criar-um-componente-para-o-fritzing
Tags: arduino, diy, eletrônica, fritzing, olho_de_lcd, projetos, tutorial

[<img src="{filename}/images/old/displayLCDNokia5110_bb.jpg" width="480">]({filename}/images/old/displayLCDNokia5110_bb.jpg)Quando
fui documentar o meu projeto de [criar um olho de brinquedo usando um
display LCD Nokia
5110](http://umcarneiro.blogspot.com/2014/01/olho-de-lcd-com-arduino-e-nokia-5110.html),
descobri que o [Fritzing](http://www.fritzing.org/) não tem um desenho
deste display. E agora? Como fazer para desenhar?

A [referência oficial do
Fritzing](http://fritzing.org/learning/tutorials/creating-custom-parts/providing-part-graphics/)
que achei na internet dizia estar desatualizada e mandava ir procurar no
blog deles, mas não tinha um link direto.

Na verdade, a instrução estava desatualizada por existir um novo editor
de partes dentro do Fritzing desde a versão 0.7.9, mas a versão que eu
tinha (0.6.3, a que você encontra na Central de Programas do Ubuntu)
ainda não vinha com esse editor.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  [<img src="{filename}/images/old/Fritzing085.png" width="480">]({filename}/images/old/Fritzing085.png)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------

Dei uma pesquisada e o editor novo me pareceu bem melhor que o anterior,
então baixei a versão atual do Fritzing, a 0.8.5. Se estiver usando o
Ubuntu, recomendo você baixar a versão disponível na Central de
Programas do Ubuntu primeiro e depois instalar essa, isso garante que as
dependências estarão atendidas.

O post do blog do Fritzing que detalha como usar o novo editor de
componentes está neste link:  
<http://blog.fritzing.org/2012/10/09/new-parts-editor-released/>

Tudo o que escrevi aqui aprendi lendo esse post, então se tiverem
dúvidas, vão ali primeiro.

[<img src="{filename}/images/old/Display128x64.png" width="480">]({filename}/images/old/Display128x64.png)O
editor de componentes (parts) do Fritzing precisa começar sempre de um
componente existente. Como estamos trabalhando com um display de LCD,
faz todo sentido partir de outro display de LCD. O Nokia 5110 é um
display gráfico, então eu inseri um display gráfico 128 x 64.

[<img src="{filename}/images/old/medidas.jpg" width="480">]({filename}/images/old/medidas.jpg)A
partir daí, você pode clicar no componente com o botão direito e
selecionar Editar ou ir em Componente -\> Editar (Criador de Novos
Componentes).

Para criar as imagens, eu exportei para SVG o desenho do display de
128x64 (verde) e o abri no [Inkscape](http://inkscape.org/). O desenho
já chegou no Inkscape com medidas corretas (para um display grande).
Usando medidas em mm, consegui redesenhar o meu display. Tomei alguns
cuidados para conseguir importá-lo de volta no Fritzing:

-   Não mexi na posição inicial do desenho (que começa nas coordenadas
    0,0);
-   Alterei o tamanho total do desenho SVG (Propriedades do Documento) e
    o deixei do tamanho do meu componente (43,5x43mm);
-   Não mexi nos pinos que já existiam, só removi os que estavam
    sobrando.

O que eu fiz foi basicamente desagrupá-lo todo, mudar a cor, apagar
vários dos pinos e aplicar as medidas que eu mesmo obtive com uma régua.
Evitei tentar colocar os pinos de cima, já que não iria precisar deles.

Ao voltar para o Fritzing, carreguei minha imagem (Ctrl+O) e ele
magicamente já identificou os pinos, deixando os que apaguei desmarcados
(não encontrados).



[<img src="{filename}/images/old/fritzingDisplayNovo.png" width="480">]({filename}/images/old/fritzingDisplayNovo.png)



Fui até a aba "Conectores" e apaguei os conectores de 1 a 12 (os mesmos
que eu tinha apagado do desenho) e reajustei os demais conforme a
realidade (1 a 8, RST, CE, DC, etc.)

Na aba "Metadado", preenchi as informações sobre o componente. Na aba
"Ícone", fui em Arquivo -\> "Reusar imagem do protoboard".





Para a aba "PCB" você tem que gerar um novo arquivo SVG. Você faz o
mesmo processo da visão Protoboard: exportar o desenho existente e
editar.

A única coisa diferente é que os pontos de solda têm que estar em um
grupo chamado "copper0". Para isso, você agrupa os circulos que
representam os pontos de solda (Ctrl+G) e edita o nome do grupo
apertando Ctrl+Shift+X e alterando a propriedade "id" para "copper0".
Ctrl+Enter grava a alteração do nome no campo. Salve o arquivo e o
importe no Fritzing que ele vai reconhecer.



[<img src="{filename}/images/old/inkscape_groupId.png" width="480">]({filename}/images/old/inkscape_groupId.png)



A aba Esquemático você pode fazer como quiser, basta usar as [fontes
corretas](http://fritzing.org/learning/tutorials/creating-custom-parts/download-fonts-and-templates/).
Se não usar, não tem problema, o Fritzing troca para você.

Pronto! Agora você já pode usar o componente que você desenhou no seu
projeto!



[<img src="{filename}/images/old/fritzing_customPart.png" width="480">]({filename}/images/old/fritzing_customPart.png)



O componente que eu criei você pode [pegar
aqui](https://github.com/ocarneiro/nokia-lcd-5110)e usar como quiser.

UPDATE: No dia 16/01/2014, postei um exemplo de como colocar o display
para funcionar, com código e tudo. [Veja
aqui](http://carneiro.blog.br/um/2014-01-31-Olho-de-LCD-com-Arduino-e-Nokia-5110-sucesso.html).

Você pode ver todas as etapas deste projeto usando [este
link](http://carneiro.blog.br/um/tag/olho_de_lcd.html), ou
clicando na tag "[olho\_de\_lcd](http://carneiro.blog.br/um/tag/olho_de_lcd.html)",
abaixo.
