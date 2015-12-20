Title: Testei o LibreOffice Online - e achei fantástico!
Date: 2015-12-19 16:42
Author: Otávio Carneiro
Slug: 2015-12-19-Testei-o-LibreOffice-Online
Tags: LibreOffice, software_livre

**Lançamento LibreOffice Online**  
Esta semana, [saiu uma notícia](http://news.softpedia.com/news/owncloud-and-collabora-announces-libreoffice-online-for-owncloud-server-vm-497627.shtml) que me chamou muito a atenção. Finalmente anunciaram uma versão funcional do LibreOffice Online, a versão "cloud" ou "nas nuvens" do LibreOffice. Já faz algum tempo que circula a ideia de um equivalente livre do Google Docs ou do MS Office 365, mas até o momento não havia nada de concreto.

No dia 15/12/2015, no entanto, saiu a esperada notícia. Finalmente existe um software de escritório que você pode instalar no seu próprio servidor e usar de onde quiser.

**O que é?**  
O codinome do projeto é [CODE](https://www.collaboraoffice.com/code/), sigla para Collabora Online Development Edition. O Collabora no nome do projeto se refere à empresa [Collabora](https://www.collaboraoffice.com/about-us/), a mesma que desenvolve a versão do LibreOffice [utilizada pelo governo do Reino Unido](http://news.softpedia.com/news/uk-government-is-kicking-out-microsoft-office-and-adopts-libreoffice-494919.shtml).

Na própria [página do projeto](https://www.collaboraoffice.com/code/) há links para baixar um arquivo .vmdk diretamente ou via um torrent. Este arquivo você utiliza como um disco virtual em uma máquina virtual no VirtualBox ou software similar. Foi o que eu fiz.

**Como instalar**  
Se quiser experimentar também, veja os passos que utilizei abaixo.

1) Abra o VirtualBox e crie uma nova máquina virtual  
 - A página do projeto fala para criar com uma versão específica de Linux, mas o linux já está no arquivo, você não precisa se preocupar.

[<img src="{filename}/images/lo-code/01a-tipo.png" width=400>]({filename}/images/lo-code/01a-tipo.png)  
 - o disco virtual é a parte importante. É aqui que você vai indicar o arquivo .vmdk (já descompactado) que você baixou da internet.  
[<img src="{filename}/images/lo-code/01b-disco.png" width=400>]({filename}/images/lo-code/01b-disco.png)

2) Na configuração de rede, você escolhe o modo Bridge.  
 - no modo bridge, a máquina virtual que você está criando será reconhecida pelo roteador como se fosse uma outra máquina e ganhará um ip próprio.  
[<img src="{filename}/images/lo-code/02-configRede.png" width=400>]({filename}/images/lo-code/02-configRede.png)

3) Pronto! Você já pode iniciar a máquina!  
[<img src="{filename}/images/lo-code/03-boot.png" width=400>]({filename}/images/lo-code/03-boot.png)

4) Quando ela subir, já aparecerá o endereço que você deve utilizar para acessar o LibreOffice Online!  
[<img src="{filename}/images/lo-code/04-iniciado.png" width=400>]({filename}/images/lo-code/04-iniciado.png)

5) E ao acessar esse endereço, você já chega na tela de login.  
 - O padrão é usuário admin e senha admin.  
 - E o melhor: ele já reconhece sua língua e aparece em português do Brasil (pt-BR)!  
[<img src="{filename}/images/lo-code/05-login-ptBR.png" width=400>]({filename}/images/lo-code/05-login-ptBR.png)

6) A tela inicial parece com o Dropbox. É o [ownClowd](https://owncloud.org/).  
 - ownCloud é uma alternativa ao Dropbox. É a sua própria nuvem, como o nome sugere.  
 - o CODE (LibreOffice Online do Collabora) se baseia em uma espécie de plugin do ownCloud que sabe abrir e editar os arquivos do LibreOffice que estão no repositório. É uma solução genial!  
 - é um dos princípios do software livre: não reinvente a roda!  
[<img src="{filename}/images/lo-code/06-tela-inicial.png" width=400>]({filename}/images/lo-code/06-tela-inicial.png)

7) O repositório já vem com uma pasta cheia de exemplos para você experimentar.  
[<img src="{filename}/images/lo-code/07-documentos.png" width=400>]({filename}/images/lo-code/07-documentos.png)

8) Ao clicar no primeiro documento, você já pode editá-lo. No browser!  
[<img src="{filename}/images/lo-code/08-documento-texto1.png" width=400>]({filename}/images/lo-code/08-documento-texto1.png)

9) A edição do arquivo (no browser!!!) é idêntica à edição no LibreOffice "normal".  
 - você pode selecionar trechos do texto, mudar fonte e tudo o mais!
[<img src="{filename}/images/lo-code/09-editando.png" width=400>]({filename}/images/lo-code/09-editando.png)

10) Após a edição, você pode salvar no próprio repositório (online) ou baixar como um arquivo ODF (ou pdf ou até do Microsoft Word).  
[<img src="{filename}/images/lo-code/10-download.png" width=400>]({filename}/images/lo-code/10-download.png)

11) O arquivo baixado como ODF (Open Document Format, o formato do LibreOffice) pode ser editado normalmente.  
[<img src="{filename}/images/lo-code/11-libreoffice-local.png" width=400>]({filename}/images/lo-code/11-libreoffice-local.png)

12) Você pode inclusive utilizar fontes que só existem no seu computador!  
 - usei aqui a fonte [Yikes!](http://www.dafont.com/pt/yikes.font), a mesma que utilizamos nos [stickers do Calango](https://github.com/calangohc/calango-telegram-stickers) para o Telegram.  
[<img src="{filename}/images/lo-code/12-editado-lo-local.png" width=400>]({filename}/images/lo-code/12-editado-lo-local.png)

13) Voltando ao browser, você pode fazer upload do arquivo.  
[<img src="{filename}/images/lo-code/13-upload.png" width=400>]({filename}/images/lo-code/13-upload.png)

14) O arquivo carregado fica disponível como todos os outros.  
[<img src="{filename}/images/lo-code/14-uploaded.png" width=400>]({filename}/images/lo-code/14-uploaded.png)

15) Como o servidor não tem a fonte que utilizamos, outra é exibida no lugar, mas o arquivo não perde a informação da fonte original.  
[<img src="{filename}/images/lo-code/15-editando-arq-gerado-local.png" width=400>]({filename}/images/lo-code/15-editando-arq-gerado-local.png)

**Em resumo:**  
 - A ferramenta é muito fácil de instalar, basta baixar um arquivo e subir em uma máquina virtual;  
 - É muito fácil de usar;  
 - A compatilibidade do editor com o LibreOffice Writer 4.3 foi perfeita neste teste inicial;  
 - Vale muito a pena experimentar!

Neste post brinquei somente com um documento de texto do LibreOffice Writer (equivalente ao Microsoft Word). 

Em uma próxima vez, podemos olhar os outros formatos de arquivo, Calc (tipo Excel) e Impress (equivalente ao PowerPoint). 

Se tiverem alguma questão que queiram ver abordada, por favor coloquem nos comentários.

Obrigado!  
Otávio
