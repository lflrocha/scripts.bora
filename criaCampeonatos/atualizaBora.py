#!/usr/bin/python
# -*- coding: UTF-8 -*-

import couchdb
import json
import urllib2

user = "admin"
password = "card1gans"
couchserver = couchdb.Server("http://%s:%s@45.56.114.69:5984/" % (user, password))
db = couchserver['bora2']

documentos = [
  ('amarelos','getAmarelos2.json'),
  ('artilharia','getArtilharia2.json'),
  ('defesa','getDefesa2.json'),
  ('disciplina','getDisciplina2.json'),
#  ('jogos','getJogos2.json'),
  ('regulamento','getRegulamento2.json'),
  ('resenhas','getResenhas2.json'),
  ('suspensos','getSuspensos2.json'),
  ('tabela','getTabela2.json'),
  ('times','getTimes2.json'),
  ('vermelhos','getVermelhos2.json')
]


campeonatos = [
  'clube-da-oab-categoria-livre',
  'clube-da-oab-categoria-master',
  'clube-da-oab-subsecoes',
  'apcef-socaite-adulto',
  'apcef-socaite-master-2018',
  'apcef-veteranos',
  'asbac',
  'adepol',
  'lifa-2018-livre',
  'lifa-2018-feminino',
  'lifa-2018-master-campo',
  'lifa-2018-master-society',
  'lifa-2018-supermaster',
  'copa-sangue-no-olho-2018'
]

campeonatos = [
  'clube-da-oab-categoria-master'
]

for campeonato in campeonatos:
    for documento in documentos:
        url = "http://bora.lflr.com.br/%s/%s" % (campeonato, documento[1])
        aux = urllib2.urlopen(url)
        aux2 = aux.read()
        dados = json.loads(aux2)
        chave = documento[0]
        if documento == 'jogos':
            chave = 'campeonato'

        if documento == 'tabela':
            chave = 'fases'

        id = campeonato + '-' + documento[0]
        doc = db.get(id)
        doc[chave] = dados[chave]
        doc = db.save(doc)
        print chave, "Saved"
