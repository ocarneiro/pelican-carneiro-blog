Title: Como criar um ambiente de desenvolvimento python no Debian
Date: 2015-02-07 19:55
Author: Otávio Carneiro
Slug: Como-criar-um-ambiente-de-desenvolvimento-python-no-Debian

Estou me baseando na seguinte pergunta (e respostas) do StackOverflow
para criar meu ambiente de desenvolvimento Python:

<http://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python>

1\) Baixar o Virtualenv:  
- Fui aqui: <https://pypi.python.org/pypi/virtualenv#downloads>  
- Baixei a versão tar.gz  
- A versão foi a 12.0.7, a mais recente no momento  
- Para descompactar, rodei o seguinte:  
   tar xvf virtualenv\*

2\) Escolher um lugar para o seu ambiente inicial  
- O virtualenv cria um ambiente de desenvolvimento isolado. Não é
exatamente uma máquina virtual, mas você pode imaginar que é algo
parecido.  
- No procedimento que estamos adotando, você vai criar um "ambiente
zero". É um ambiente de desenvolvimento com as bibliotecas e módulos
básicos dos quais você vai derivar ambientes específicos para cada
projeto.  
- Eu escolhi gravar o meu ambiente inicial em "\~/py-env0"

3\) Criar o seu ambiente inicial  
- Estou usando o python 2.7.8, mas não deve haver diferença para o
python 3.  
- Rodei o seguinte comando:  
python virtualenv.py \~/py-env0  
- Eu estava no diretório onde descompactei o arquivo do virtualenv que
baixei acima.

4\) Instale o virtualenv no seu ambiente inicial:  
\~/py-env0/bin/pip install virtualenv\*.tar.gz  
ATUALIZAÇÃO (em 13/02/2015): Meu amigo Paulo Henrique me alertou que
este passo é confuso. "Tem que executar o pip sobre o arquivo que eu já
descompactei?". É isso mesmo! Se você tiver fé, confie em mim e rode
assim mesmo. Se você precisar entender, corra para o fim do post (depois
das referências) que eu explico.

5\) Crie o ambiente de desenvolvimento do seu projeto:  
\~/py-env0/bin/virtualenv pasta\_do\_projeto/env

6\) Ative o ambiente de desenvolvimento quando estiver trabalhando nele:  
. pasta\_do\_projeto/env/bin/activate  
Repare que o comando começa com um ponto e um espaço.  Isso é
importante! Isso faz com que o comando seja executado no ambiente
(shell) atual.  
Na maioria dos sistemas (os que usam o bash), isso equivale a:  
source pasta\_do\_projeto/env/bin/activate

7\) Alguns módulos exigem o pacote python-dev:  
sudo apt-get install python-dev

PERGUNTA BÔNUS: Você deve versionar o ambiente junto com o projeto?  
RESPOSTA: Não. Ao invés disso, versione o arquivo requirements.txt
gerado com o comando abaixo:  
pip freeze

Para instalar os módulos listados no arquivo, use o seguinte:  
pip install -r requirements.txt

Referências:  
<http://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repository>  
<http://stackoverflow.com/questions/6812207/how-can-i-correctly-install-multiple-non-package-distribute-virtualenv-pip-ecosys>  
<http://askubuntu.com/questions/232932/in-a-bash-script-what-does-a-dot-followed-by-a-space-and-then-a-path-mean>

Bons projetos!

Abs.,  
Otávio

----------------------------------------------------------------  
ATUALIZAÇÃO (em 13/02/2015): Mas por quê?! Por que rodar o "pip
virtualenv\*.tar.gz" no passo 4 ??!!

Vou tentar explicar...

Antes de começar o tutorial, não havia nenhum virtualenv, nem pip, nem
nada na sua máquina. Quando você executa o passo 3, você roda o
virtualenv a partir do código fonte. Ali você está criando um primeiro
ambiente (que chamei de \~/py-env0). Só que neste primeiro ambiente,
pasme!, não há nenhum virtualenv instalado.

Ahn?

Sabe aquele filme "A Origem" em que as pessoas vivem dentro de um sonho
de uma pessoa que está sonhando que está tendo outro sonho? É tipo isso.

No seu ambiente linux (A), não tem virtualenv nenhum instalado:

A (nenhum virtualenv aqui)

No passo 3 você cria o primeiro "sonho", um ambiente em \~/py-env0:

A (nenhum virtualenv aqui)  
      B (\~/py-env0, nenhum virtualenv aqui também)

Só que você está criando esse \~/py-env0 (B) justamente para poder ter
uma base, um ponto de partida para criar outros ambientes. Então você
precisa instalar o virtualenv neste ambiente B. É isso que você faz no
passo 4:

A (sem virtualenv)  
      B (\~/py-env0, agora com virtualenv!)

no passo 5, você usa esse virtualenv recém-instalado em B para criar o
seu ambiente de projeto (C):

A (nunca terá virtualenv)  
      B (\~/py-env0, o pai de todos os virtualenvs)  
            C (projeto/env, o filho de B)

Neste ambiente C, depois de ativado (passo 6) você já pode dar "pip
install qqcoisa" e instalar qualquer pacote. Pode até dar "pip install
virtualenv" e instalar um virtualenv.

Peraí! Então eu poderia ter ativado o ambiente B e usado "pip install
virtualenv" lá no passo 4? Sim, jovem gafanhoto. Só que o pip teria
baixado de novo um pacote que você tinha acabado de baixar e estava bem
à mão, compactado naquele arquivo .tar.gz. Sem nem precisar ativar
nada...

É, eu sei... Não faz nenhum sentido... Respire e beba um copo d'água
antes de ler o próximo parágrafo.

Se você está batendo cabeça e não conseguiu fazer nada disso, não se
desespere. O python 2.7.9 já vem com o pip. Você pode dar um "pip
install virtualenv" e ser feliz assim que instalar. Uma hora dessas eu
experimento e conto aqui como é.

Abraços,  
Otávio


