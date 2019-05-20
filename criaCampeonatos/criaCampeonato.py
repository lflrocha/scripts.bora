#!/usr/bin/python
# -*- coding: UTF-8 -*-

import couchdb
import json
import urllib2

user = "admin"
password = "card1gans"
couchserver = couchdb.Server("http://%s:%s@45.56.114.69:5984/" % (user, password))
db = couchserver['bora2']

list = [
  'amarelos',
  'artilharia',
  'defesa',
  'disciplina',
  'jogos',
  'regulamento',
  'resenhas',
  'suspensos',
  'tabela',
  'times',
  'vermelhos',
]

campeonatos = [
    'aabb-socaite-adulto-2019'
]

for campeonato in campeonatos:
    for item in list:

        tabela = campeonato + '-' + item
        objeto = item

        if item == 'jogos':
            objeto = 'campeonato'

        if item == 'tabela':
            objeto = 'fases'

        db[tabela] = {objeto: '' }
        print tabela, "Criado"
