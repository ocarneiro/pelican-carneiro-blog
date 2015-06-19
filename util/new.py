#! /usr/bin/env python3
import datetime, sys

#obtém a hora atual e a imprime
now = datetime.datetime.now()
(year,month,day,hour,minute)=(now.year, now.month, now.day, now.hour, now.minute)

#trata nome informado na linha de comando
if len(sys.argv)>1:
    title = sys.argv[1]
else:
    #ou pede para o usuário inserir
    title = input("Nome do artigo? ")
print("Title: {}".format(title))

print("Date: {}-{:02}-{:02} {:02}:{:02}".format(year,month,day,hour,minute))

#cria o slug a partir do nome, trocando espaços por -
slug = "{}-{:02}-{:02}-{}".format(year,month,day,title.replace(" ", "-"))
print("Slug: {}".format(slug))



with open(slug + ".md", "w") as post:
    print("Title: {}".format(title), file=post)
    print("Date: {}-{:02}-{:02} {:02}:{:02}".format(year,month,day,hour,minute), file=post)
    print("Author: Otávio Carneiro", file=post)
    print("Slug: {}".format(slug), file=post)
    print("Tags: ", file=post)
#Title: Minecraft para a Educação - Parte 1
#Date: 2015-06-04 15:36
#Author: Otávio Carneiro
#Slug: Minecraft-para-a-Educacao-Parte-1
#Tags: python, minecraft, cidadania, educação, raspberry pi
