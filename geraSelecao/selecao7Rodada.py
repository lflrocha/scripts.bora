#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps

destino = "/Users/lflrocha/Google Drive/_Shared/Bora/"

urls = [
    "http://bora.lflr.com.br/cbm-society-principal-2019/selecao/selecao_7.2019-03-20.2376746938/",
    "http://bora.lflr.com.br/cbm-society-antigoes-2019/selecao/selecao_7.2019-03-20.3798147413/"
]

semReservas = [
    u'CBM - Society Principal 2019',
    u'CBM - Society Antigões 2019'
]


posicoes = {'331': [
        (360, 960),

        (660, 780),
        (360, 780),
        ( 60, 780),

        (590, 600),
        (360, 600),
        (130, 600),

        (360, 420)],
    '2221': [
        (360, 960),

        (490, 780),
        (230, 780),

        (60, 650),
        (680, 650),

        (510, 500),
        (210, 500),

        (360, 350)] }

for url in urls:

    response = requests.get(url+ '/getSelecaoText')
    aux = response.text
    aux = aux.split('\n')

    campeonato = aux[0]
    print campeonato
    logo = aux[1]
    logoId = logo.split('http://bora.lflr.com.br/')
    logoCampeonatoId = logoId[1][:-5]

    response = requests.get(logo, stream=True)
    with open('temp/campeonato/'+logoCampeonatoId+'.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    fase = aux[2]
    rodada = aux[3]
    esquema = aux[4]

    nomeArq = campeonato+'_'+fase+'_rodada_'+rodada

    titulares = []
    tecnico = []
    reservas = []

    for i in range(5,20):

        if i < 13:
            aux2 = aux[i].split('|')
            time = aux2[0]
            logo = aux2[1]
            logoId = logo.split('/times/')
            logoId = logoId[1][:-5]
            nome = aux2[2]
            foto = aux2[3]
            fotoId = foto.split('/times/')
            fotoId = fotoId[1][:-5]
            fotoId = fotoId.replace('/','_')

            response = requests.get(logo, stream=True)
            with open('temp/times/'+logoId+'.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            response = requests.get(foto, stream=True)
            with open('temp/fotos/'+fotoId+'.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            titulares.append([time, logoId, nome, fotoId])


        if i == 13:
            aux2 = aux[i].split('|')
            time = aux2[0]
            nome = aux2[2]
            tecnico = [time, nome]


        if i > 13:
            aux2 = aux[i].split('|')
            time = aux2[0]
            nome = aux2[1]
            pos = aux2[2]

            reservas.append([time, nome, pos])


    fonteRodada = ImageFont.truetype('fontes/Portico Regular.otf', 30)
    fonteNome = ImageFont.truetype('fontes/segoe-ui-semibold.ttf', 15)
    fonteNomeReserva = ImageFont.truetype('fontes/segoe-ui-bold.otf', 22)
    fonteTimeReserva = ImageFont.truetype('fontes/segoe-ui-semibold.ttf', 20)
    fonteTreinador = ImageFont.truetype('fontes/segoe-ui-semibold.ttf', 16)
    fonteCard = ImageFont.truetype('fontes/Portico Light.otf', 32)
    fonteTime = ImageFont.truetype('fontes/segoe-ui-semibold.ttf', 18)

    corFonteBranca = (255, 255, 255, 255)
    corFonteAzul = (13, 102, 177, 255)
    corFonteCard = (31, 63, 144, 255)

    boxFill = (0, 0, 0, 255)

    if campeonato in semReservas:
        base = Image.open('assets/campo-semreserva.png').convert('RGBA')
    else:
        base = Image.open('assets/campo.png').convert('RGBA')


    tarja = Image.open('assets/tarja.png').convert('RGBA')

    baseImg = Image.new('RGBA', base.size, (255,255,255,0))
    baseText = ImageDraw.Draw(baseImg)

    tamFase = baseText.textsize(fase, font=fonteRodada)
    tamRodada = baseText.textsize(rodada, font=fonteRodada)

    faseX = 74 + (280 - tamFase[0]) / 2
    rodadaX = 74 + (280 - tamRodada[0]) / 2


    baseText.text((faseX, 145), fase, font=fonteRodada, fill=corFonteAzul)
    baseText.text((rodadaX, 180), rodada, font=fonteRodada, fill=corFonteAzul)

    logoCampeonato = Image.open('temp/campeonato/' + logoCampeonatoId + '.png').convert('RGBA')
    logoCampeonato = logoCampeonato.resize((180,180), Image.ANTIALIAS)
    baseImg.paste(logoCampeonato, (800,5), mask=logoCampeonato)

    baseText.text((740, 900), tecnico[1] + ' - ' + tecnico[0], font=fonteTreinador, fill=corFonteBranca)

    for i, jogador in enumerate(reservas):
        posY = 1070 + 25 * i
        posX = 29
        time = jogador[0]
        nome = jogador[1]
        pos = jogador[2]
        texto =  ' - ' + time + ' ('+ pos +')'
        delta = baseText.textsize(nome, font=fonteNomeReserva)
        if i > 2:
            posX = 500
            posY = 1070 + 25 * (i-3)

        baseText.text((posX, posY), nome, font=fonteNomeReserva, fill=corFonteBranca)
        baseText.text((posX + delta[0], posY + 2), texto, font=fonteTimeReserva, fill=corFonteBranca)

    ps = posicoes[esquema]
    for i, jogador in enumerate(titulares):

        time = jogador[0]
        logo = jogador[1]
        nome = jogador[2]
        foto = jogador[3]

        fotoJogador = Image.open('temp/fotos/' + foto + '.png').convert('RGBA')
        fotoJogador = fotoJogador.resize((150,150), Image.ANTIALIAS)

        size = (150, 150)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        foto2Jogador = ImageOps.fit(fotoJogador, mask.size, centering=(0.5, 0.5))
        foto2Jogador.putalpha(mask)

        pX = ps[i][0]
        pY = ps[i][1]
        baseImg.paste(foto2Jogador, (pX+75,pY-150), mask=foto2Jogador)

    #    box1 = ImageDraw.Draw(baseImg)
    #    box1.rectangle((pX+75, pY-10, pX+75 + 150, pY + 10 ), fill=boxFill)
        baseImg.paste(tarja, (pX+75,pY-10), mask=tarja)

        tamanho = baseText.textsize(nome, font=fonteNome)
        DX = 150 - (tamanho[0]/2)
        baseText.text((pX + DX, pY-11), nome, font=fonteNome, fill=corFonteBranca)



        logo = Image.open('temp/times/' + logo + '.png').convert('RGBA')
        logo = logo.resize((60,60), Image.ANTIALIAS)
        pX = ps[i][0]
        pY = ps[i][1]
        baseImg.paste(logo, (pX+75+120,pY-60), mask=logo)



    out = Image.alpha_composite(base, baseImg)
    out.save(destino+"selecao_" + nomeArq + ".png")

    card = Image.open('assets/card.png').convert('RGBA')
    cargImg = Image.new('RGBA', card.size, (255,255,255,0))
    cardText = ImageDraw.Draw(cargImg)

    tamFase = baseText.textsize(fase, font=fonteCard)
    tamRodada = baseText.textsize(rodada, font=fonteCard)

    faseX = 55 + (340 - tamFase[0]) / 2
    rodadaX = 55 + (340 - tamRodada[0]) / 2

    cardText.text((faseX, 205), fase, font=fonteCard, fill=corFonteCard)
    cardText.text((rodadaX, 235), rodada, font=fonteCard, fill=corFonteCard)

    out = Image.alpha_composite(card, cargImg)
    out.save(destino+"card_" + nomeArq + ".png")
