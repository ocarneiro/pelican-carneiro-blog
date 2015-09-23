Title: Criando uma tag cloud no Pelican 3
Date: 2015-09-23 10:59
Author: Otávio Carneiro
Slug: 2015-09-23-Criando-uma-tag-cloud-no-Pelican-3
Tags: pelican, tag-cloud, blogs, internet

Quando [migrei meu blog pro Pelican]({tag}pelican), notei que as tags ficaram numa lista simples e aquilo me incomodou um pouco, então fui estudar como criar uma tag cloud no Pelican.

Aparentemente, em versões anteriores o Pelican criava as nuvens de tag nativamente, mas a partir da versão 3, [você precisa de um plugin](http://docs.getpelican.com/en/3.6.0/faq.html#my-tag-cloud-is-missing-broken-since-i-upgraded-pelican) para isso.

A [explicação na página oficial do Pelican](http://docs.getpelican.com/en/3.6.3/plugins.html) é meio seca, diz só que você deve definir uma variável, sem dizer nem onde nem como:

    PLUGINS = ['pacote.meuplugin',]

Se eu conseguir instalar aqui, depois de publicar este post vou tentar submeter uma alteração na documentação oficial [no github](https://github.com/getpelican/pelican/blob/master/docs/plugins.rst).

O plugin para a tag cloud sugerido na página oficial também está [no github](https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud). Tem alguns arquivos no repositório, mas baixei só o [tag_cloud.py](https://github.com/getpelican/pelican-plugins/raw/master/tag_cloud/tag_cloud.py) e o gravei numa pasta plugins. Ficou assim:

        blog/
        ├── content
        ├── ...
        ├── output
        └── plugins
               └── tag_cloud.py

No meu arquivo **pelicanconf.py** adicionei estas linhas:

    :::python
    #Ativar a tag cloud (nuvem de tags)
    PLUGIN_PATHS = ["plugins"]
    PLUGINS = ["tag_cloud"]

Na pasta do tema que estou usando, alterei o arquivo **base.html**.

Ele era assim:

    :::html
        <h3>Tags</h3>
        <ul>
        {% for tag, articles in tags | sort %}
                <li><a href="{{ SITEURL }}/{{ tag.url }}"
                       >{{ tag }}</a></li>
        {% endfor %}
        </ul>

E ficou assim:

    :::html
        <h3>Tag cloud</h3>
        <ul class="tagcloud">
            {% for tag in tag_cloud %}
                <li class="tag-{{ tag.1 }}"
                         ><a href="{{ SITEURL }}/{{ tag.0.url }}"
                                        >{{ tag.0 }}</a></li>
            {% endfor %}
        </ul>       

Republiquei e... Nada!! 

Claro, faltou criar os estilos CSS para cada nível da tag.

Editei o arquivo **style.css** do meu tema e incluí o seguinte:

    :::css
        ul.tagcloud {
          list-style: none;
            padding: 0;
        }

        ul.tagcloud li {
            display: inline-block;
        }

        li.tag-1 {
            font-size: 180%;
        }

        li.tag-2 {
            font-size: 150%;
        }

        li.tag-3 {
            font-size: 120%;
        }

        li.tag-4 {
            font-size: 110%;
        }

        li.tag-5 {
            font-size: 100%;
        }

        li.tag-6 {
            font-size: 90%;
        }

[<img src="{filename}/images/tag-cloud-nuvem-tag.png" width=100 align="right">]({filename}/images/tag-cloud-nuvem-tag.png)

E o resultado é o que você está vendo aí ao lado. No momento em que escrevi este post, minha nuvem estava como nesta imagem.

Para resumir, os arquivos que tive que alterar (*) ou acrescentar (+) para ela funcionar foram os seguintes:

      blog/
        ├── pelicanconf.py *
        ├── content
        ├── plugins +
        │     └── tag_cloud.py +
        └── themes
              └── meutema
                    ├── templates
                    │      └── base.html *
                    └── static
                          └── css
                               └── style.css *

Confesso que achei mais trabalhoso do que gostaria, mas agora tenho uma nuvem bacana no blog.

Abs!  
Otávio


