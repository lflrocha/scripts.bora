#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import os
import time
import datetime

from PIL import Image, ImageDraw, ImageFont

corFonteVerde = (0, 255, 133, 255)
corFonteBranca = (255, 255, 255, 255)
corFontePreta = (14, 255, 8, 255)


fonteTitulo = ImageFont.truetype('fontes/Portico Regular.otf', 200)
fonteRodada = ImageFont.truetype('fontes/Metropolis-ExtraBold.otf', 150)
fonteJogador = ImageFont.truetype('fontes/Portico Regular.otf', 100)
fonteTime = ImageFont.truetype('fontes/Portico Light.otf', 100)

fotoX = 600
fotoY = 600


base = Image.open('campo.png').convert('RGBA')
baseImg = Image.new('RGBA', base.size, (255,255,255,0))
baseText = ImageDraw.Draw(baseImg)


baseText.text((260, 100), u"ASBAC 2018", font=fonteTitulo, fill=corFonteBranca)
baseText.text((260, 300), u"Rodada 10", font=fonteRodada, fill=corFonteBranca)


def geraArte(arquivo, pX, pY):


    aux = arquivo.split(' - ')
    foto01 = Image.open('fotos/' + arquivo + '.jpg').convert('RGBA')
    foto01 = foto01.resize((fotoX,fotoY), Image.ANTIALIAS)
    baseImg.paste(foto01, (pX,pY), mask=foto01)

    tamanhoNome = baseText.textsize(aux[1], font=fonteJogador)
    x = (pX + (fotoX/2)) - (tamanhoNome[0]/2)
    baseText.text((x, pY + fotoY + 10), aux[1], font=fonteJogador, fill=corFonteBranca)

    tamanhoTime = baseText.textsize(aux[2], font=fonteJogador)
    x = (pX + (fotoX/2)) - (tamanhoTime[0]/2)
    baseText.text((x, pY + fotoY + 100 + 10), aux[2], font=fonteTime, fill=corFonteBranca)

    #out.save('export_A.png')


arquivo = [
    [u"01 - João Marcelo - Dez-treinandos", 1650, 5100],
    [u"02 - Juninho Morato - Dez-treinados", 3115, 4350],
    [u"03 - Kaká - Experi" , 2175, 4050],
    [u"04 - Lessa - Piratas" , 1200, 4050],
    [u"05 - Madruga - Combo" , 345 , 4350],
    [u"06 - Marcelo - Sambola" ,1200 ,2800 ],
    [u"07 - Muka - Calangos" , 2175, 2800],
    [u"08 - Pedro Crema - Combo" , 345 , 2250],
    [u"09 - Pelé - Galáticos" , 3115 , 2250],
    [u"10 - Rannderson - Galáticos" , 945 , 925],
    [u"11 - Tiago Pequeno - Experi" , 2415 , 925 ],
]


for item in arquivo:
    geraArte(item[0], item[1], item[2])
out = Image.alpha_composite(base, baseImg)
out.show()
