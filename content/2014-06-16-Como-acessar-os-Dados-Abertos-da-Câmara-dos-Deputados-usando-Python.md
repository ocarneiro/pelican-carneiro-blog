Title: Como acessar os Dados Abertos da Câmara dos Deputados usando Python
Date: 2014-06-16 21:36
Author: Otávio Carneiro
Slug: Como-acessar-os-Dados-Abertos-da-Câmara-dos-Deputados-usando-Python

A Câmara dos Deputados tem um serviço muito interessante chamado [Dados
Abertos](http://www2.camara.leg.br/transparencia/dados-abertos). A ideia
é que qualquer cidadão tenha acesso a informações sobre Deputados e
sobre a tramitação de propostas de leis. Você não precisa se cadastrar
nem nada, basta saber montar suas consultas. E foi para ensinar a
fazê-lo que resolvi escrever este post.

<style>  pre {background-color: #eeeeee; border: 1px dashed #999999; color: black; font-family: Andale Mono, Lucida Console, Monaco, fixed, monospace; font-size: 12px; line-height: 14px; overflow: auto; padding: 5px; width: 100%;}  code {color: black; word-wrap: normal;} </style>
O serviço Dados Abertos é um WebService. Um webservice é como se fosse
um sistema de informação sem telas. Você pode consultar o que quiser,
mas não tem um formulário para preencher o que quer. E o retorno do
sistema não é uma planilha bonitinha nem um relatório em PDF, é só um
monte de informação que você mesmo tem que tratar.

Eu resolvi usar python para fazer minhas pesquisas. Eu estou usando a
biblioteca [suds](https://fedorahosted.org/suds/), que é um cliente leve
de webservices para python.

Para instalar no linux, usei:

    $  sudo pip install suds

Para poder fazer isso, você tem que ter o
[python](https://www.python.org/) e o
[pip](http://pip.readthedocs.org/en/latest/index.html) instalados.

Depois você faz o seguinte:

    $ python

    >>> from suds.client import Client  #importa o cliente

Aí você define a URL:

    >>> url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl'

e acessa:

    >>> client = Client(url)

Pronto! Você já tem acesso ao WebService. Agora você pode olhar os
métodos disponíveis de forma já tratada pelo suds:

    >>> print (client)

Um dos métodos que ele mostra como disponíveis é esse:  
     ListarSiglasTipoProposicao()

Para consumí-lo, você faz o seguinte:

    >>> resultado = client.service.ListarSiglasTipoProposicao()

O retorno é um xml composto pela tag <siglas> que possui vários objetos
<sigla> com atributos "tipoSigla", "descricao" e outros.

Se quiser ver o "tipoSigla" do terceiro item, você pode acessá-lo assim:

    >>> resultado['siglas']['sigla'][2]._tipoSigla

E o retorno vai ser: 

    ANEXO

Agora digamos que você quer saber quantas medidas provisórias estão em
tramitação no Congresso Nacional neste momento...

Você poderia utilizar o método ListarProposicoes. Nossa chamada "print
client" mostra este método da seguinte forma:

Methods (11):  
            ListarProposicoes(xs:string sigla, xs:string numero,
xs:string ano, xs:string datApresentacaoIni, xs:string
datApresentacaoFim, xs:string idTipoAutor, xs:string parteNomeAutor,
xs:string siglaPartidoAutor, xs:string siglaUFAutor, xs:string
generoAutor, xs:string codEstado, xs:string codOrgaoEstado, xs:string
emTramitacao, )

Olhando a [documentação do
método](http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo/webservices/proposicoes-1/listarproposicoes),
você vai ver que alguns campos são obrigatórios. Um deles é o ano,
infelizmente. Então, para descobrir quantas medidas provisórias (de
qualquer ano) estão em tramitação no Congresso, você tem que fazer
várias chamadas como esta:

    >>> resultado = client.service.ListarProposicoes('MPV', None, 2014, None, None, None, None, None, None, None, None, None, 1)

O 'MPV' no começo significa Medida Provisória e o 1 no final indica que
a proposição está tramitando. Para ver quantas deram você usa o seguinte
comando:

    >>> len(resultado['proposicoes']['proposicao'])

Se quiser ver vários anos, pode executar o seguinte:

    >>> for a in range(2005,2015):...    resultado = client.service.ListarProposicoes('MPV', None, a, None, None, None, None, None, None, None, None, None, 1)...    print(str(a) + ': ' + str(len(resultado['proposicoes']['proposicao'])))...

Para minha surpresa, no momento em que fiz a consulta, havia 12
proposições do tipo Medida Provisória de 2014, e dezenas de outras de
outros anos. Na verdade, como vocês podem ver [em outra
consulta](http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarSituacoesProposicao),
quase todas as situações de proposições são consideradas "Ativas",
inclusive "Retirado pelo Autor", "Perdeu a Eficácia", "Enviada ao
Arquivo" e "Arquivada"... Acho que terei que montar meu próprio conceito
de "Ativa". Conto para vocês depois....

Abs.,Otávio </sigla></siglas>

