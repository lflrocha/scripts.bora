#'﻿codigo;rodada;fase;grupo;campo;data;hora;time-a;time-b',

jogos = [
'1;1;Primeira fase;;2;09/03/2019;10:15;bola-preta;democrata-b',
'2;1;Primeira fase;;2;09/03/2019;11:30;puma;caiex',
'3;1;Primeira fase;;2;09/03/2019;15:15;esperanca;layser',
'4;1;Primeira fase;;1;13/03/2019;19:15;unidos;sao-jose',
'5;1;Primeira fase;;1;13/03/2019;20:30;fama-raca;duque-america',
'6;1;Primeira fase;;1;20/03/2019;19:30;fibrax-ii;fibrax-iii',
'7;2;Primeira fase;;1;16/03/2019;14:00;esperanca;fama-raca',
'8;2;Primeira fase;;1;16/03/2019;15:15;caiex;sao-jose',
'9;2;Primeira fase;;2;16/03/2019;10:15;puma;layser',
'10;2;Primeira fase;;2;16/03/2019;11:30;democrata-b;duque-america',
'11;2;Primeira fase;;2;16/03/2019;14:00;fibrax-ii;unidos',
'12;2;Primeira fase;;2;16/03/2019;15:15;bola-preta;fibrax-iii',
'13;3;Primeira fase;;2;23/03/2019;10:15;democrata-b;unidos',
'14;3;Primeira fase;;2;23/03/2019;11:30;bola-preta;layser',
'15;3;Primeira fase;;2;23/03/2019;14:00;fibrax-ii;esperanca',
'16;3;Primeira fase;;2;23/03/2019;15:15;duque-america;fibrax-iii',
'17;3;Primeira fase;;1;24/03/2019;9:00;puma;sao-jose',
'18;3;Primeira fase;;1;24/03/2019;10:15;caiex;fama-raca',
'19;4;Primeira fase;;1;30/03/2019;14:00;puma;fama-raca',
'20;4;Primeira fase;;1;30/03/2019;15:15;democrata-b;esperanca',
'21;4;Primeira fase;;2;30/03/2019;10:15;unidos;fibrax-iii',
'22;4;Primeira fase;;2;30/03/2019;11:30;caiex;fibrax-ii',
'23;4;Primeira fase;;2;30/03/2019;14:00;sao-jose;layser',
'24;4;Primeira fase;;2;30/03/2019;15:15;bola-preta;duque-america',
'25;5;Primeira fase;;2;06/04/2019;10:15;democrata-b;caiex',
'26;5;Primeira fase;;2;06/04/2019;11:30;fama-raca;layser',
'27;5;Primeira fase;;2;06/04/2019;14:00;esperanca;fibrax-iii',
'28;5;Primeira fase;;2;06/04/2019;15:15;puma;fibrax-ii',
'29;5;Primeira fase;;1;07/04/2019;9:00;unidos;duque-america',
'30;5;Primeira fase;;1;07/04/2019;10:15;bola-preta;sao-jose',
'31;6;Primeira fase;;1;13/04/2019;14:00;bola-preta;unidos',
'32;6;Primeira fase;;1;13/04/2019;15:15;puma;democrata-b',
'33;6;Primeira fase;;2;13/04/2019;10:15;fibrax-ii;layser',
'34;6;Primeira fase;;2;13/04/2019;11:30;esperanca;duque-america',
'35;6;Primeira fase;;2;13/04/2019;14:00;caiex;fibrax-iii',
'36;6;Primeira fase;;2;13/04/2019;15:15;fama-raca;sao-jose',
'37;7;Primeira fase;;2;27/04/2019;10:15;democrata-b;layser',
'38;7;Primeira fase;;2;27/04/2019;11:30;bola-preta;fama-raca',
'39;7;Primeira fase;;2;27/04/2019;14:00;puma;fibrax-iii',
'40;7;Primeira fase;;2;27/04/2019;15:15;fibrax-ii;sao-jose',
'41;7;Primeira fase;;1;28/04/2019;9:00;esperanca;unidos',
'42;7;Primeira fase;;1;28/04/2019;10:15;caiex;duque-america',
'43;8;Primeira fase;;2;04/05/2019;10:15;democrata-b;sao-jose',
'44;8;Primeira fase;;2;04/05/2019;11:30;fibrax-ii;fama-raca',
'45;8;Primeira fase;;2;04/05/2019;14:00;layser;fibrax-iii',
'46;8;Primeira fase;;2;04/05/2019;15:15;caiex;unidos',
'47;8;Primeira fase;;1;05/05/2019;9:00;puma;duque-america',
'48;8;Primeira fase;;1;05/05/2019;10:15;bola-preta;esperanca',
'49;9;Primeira fase;;2;11/05/2019;10:15;democrata-b;fama-raca',
'50;9;Primeira fase;;2;11/05/2019;11:30;puma;unidos',
'51;9;Primeira fase;;2;11/05/2019;14:00;bola-preta;fibrax-ii',
'52;9;Primeira fase;;2;11/05/2019;15:15;sao-jose;fibrax-iii',
'53;9;Primeira fase;;1;12/05/2019;9:00;caiex;esperanca',
'54;9;Primeira fase;;1;12/05/2019;10:15;duque-america;layser',
'55;10;Primeira fase;;1;14/05/2019;19:15;democrata-b;fibrax-ii',
'56;10;Primeira fase;;1;14/05/2019;20:45;fama-raca;fibrax-iii',
'57;10;Primeira fase;;1;15/05/2019;19:15;puma;esperanca',
'58;10;Primeira fase;;1;15/05/2019;20:45;bola-preta;caiex',
'59;10;Primeira fase;;1;16/05/2019;19:15;unidos;layser',
'60;10;Primeira fase;;1;16/05/2019;20:45;sao-jose;duque-america',
'61;11;Primeira fase;;1;19/05/2019;8:45;fibrax-ii;duque-america',
'62;11;Primeira fase;;1;19/05/2019;10:15;democrata-b;fibrax-iii',
'63;11;Primeira fase;;1;19/05/2019;11:30;caiex;layser',
'64;11;Primeira fase;;2;19/05/2019;8:45;esperanca;sao-jose',
'65;11;Primeira fase;;2;19/05/2019;10:15;fama-raca;unidos',
'66;11;Primeira fase;;2;19/05/2019;11:30;bola-preta;puma',
'67;1;Segunda fase;;2;26/05/2019;8:45;democrata-b;bola-preta',
'68;1;Segunda fase;;2;26/05/2019;10:15;caiex;puma',
'69;1;Segunda fase;;2;26/05/2019;11:30;fibrax-iii;fibrax-ii',
'70;1;Segunda fase;;1;28/05/2019;20:00;layser;esperanca',
'71;1;Segunda fase;;1;29/05/2019;19:15;sao-jose;unidos',
'72;1;Segunda fase;;1;29/05/2019;20:45;duque-america;fama-raca',
'73;2;Segunda fase;;2;02/06/2019;11:30;fama-raca;esperanca',
'74;2;Segunda fase;;1;04/06/2019;20:00;sao-jose;caiex',
'75;2;Segunda fase;;1;05/06/2019;19:15;layser;puma',
'76;2;Segunda fase;;1;05/06/2019;20:45;duque-america;democrata-b',
'77;2;Segunda fase;;1;06/06/2019;19:15;unidos;fibrax-ii',
'78;2;Segunda fase;;1;06/06/2019;20:45;fibrax-iii;bola-preta',
'79;3;Segunda fase;;2;09/06/2019;8:45;unidos;democrata-b',
'80;3;Segunda fase;;2;09/06/2019;10:15;layser;bola-preta',
'81;3;Segunda fase;;2;09/06/2019;11:30;esperanca;fibrax-ii',
'82;3;Segunda fase;;1;11/06/2019;19:15;fibrax-iii;duque-america',
'83;3;Segunda fase;;1;11/06/2019;20:30;sao-jose;puma',
'84;3;Segunda fase;;1;12/06/2019;20:00;fama-raca;caiex',
'85;4;Segunda fase;;2;16/06/2019;11:30;fama-raca;puma',
'86;4;Segunda fase;;1;18/06/2019;19:15;esperanca;democrata-b',
'87;4;Segunda fase;;1;18/06/2019;20:45;fibrax-iii;unidos',
'88;4;Segunda fase;;1;20/06/2019;8:45;fibrax-ii;caiex',
'89;4;Segunda fase;;1;20/06/2019;10:15;layser;sao-jose',
'90;4;Segunda fase;;1;20/06/2019;11:30;duque-america;bola-preta',
'91;5;Segunda fase;;2;23/06/2019;8:45;caiex;democrata-b',
'92;5;Segunda fase;;2;23/06/2019;10:15;layser;fama-raca',
'93;5;Segunda fase;;2;23/06/2019;11:30;fibrax-iii;esperanca',
'94;5;Segunda fase;;1;25/06/2019;20:00;fibrax-ii;puma',
'95;5;Segunda fase;;1;26/06/2019;19:15;duque-america;unidos',
'96;5;Segunda fase;;1;26/06/2019;20:45;sao-jose;bola-preta',
'97;6;Segunda fase;;2;30/06/2019;11:30;unidos;bola-preta',
'98;6;Segunda fase;;1;02/07/2019;20:00;democrata-b;puma',
'99;6;Segunda fase;;1;03/07/2019;19:15;layser;fibrax-ii',
'100;6;Segunda fase;;1;03/07/2019;20:45;duque-america;esperanca',
'101;6;Segunda fase;;1;04/07/2019;19:15;fibrax-iii;caiex',
'102;6;Segunda fase;;1;04/07/2019;20:45;sao-jose;fama-raca',
'103;7;Segunda fase;;2;07/07/2019;8:45;layser;democrata-b',
'104;7;Segunda fase;;2;07/07/2019;10:15;fama-raca;bola-preta',
'105;7;Segunda fase;;2;07/07/2019;11:30;fibrax-iii;puma',
'106;7;Segunda fase;;1;09/07/2019;20:00;sao-jose;fibrax-ii',
'107;7;Segunda fase;;1;10/07/2019;19:15;unidos;esperanca',
'108;7;Segunda fase;;1;10/07/2019;20:45;duque-america;caiex',
'109;8;Segunda fase;;2;14/07/2019;11:30;sao-jose;democrata-b',
'110;8;Segunda fase;;1;16/07/2019;20:00;fama-raca;fibrax-ii',
'111;8;Segunda fase;;1;17/07/2019;19:15;fibrax-iii;layser',
'112;8;Segunda fase;;1;17/07/2019;20:45;unidos;caiex',
'113;8;Segunda fase;;1;18/07/2019;19:15;duque-america;puma',
'114;8;Segunda fase;;1;18/07/2019;20:45;esperanca;bola-preta',
'115;9;Segunda fase;;2;21/07/2019;8:45;fama-raca;democrata-b',
'116;9;Segunda fase;;2;21/07/2019;10:15;unidos;puma',
'117;9;Segunda fase;;2;21/07/2019;11:30;fibrax-ii;bola-preta',
'118;9;Segunda fase;;1;23/07/2019;20:00;fibrax-iii;sao-jose',
'119;9;Segunda fase;;1;24/07/2019;19:15;esperanca;caiex',
'120;9;Segunda fase;;1;24/07/2019;20:45;layser;duque-america',
'121;10;Segunda fase;;1;28/07/2019;8:45;fibrax-ii;democrata-b',
'122;10;Segunda fase;;1;28/07/2019;10:15;fibrax-iii;fama-raca',
'123;10;Segunda fase;;1;28/07/2019;11:30;esperanca;puma',
'124;10;Segunda fase;;2;28/07/2019;8:45;caiex;bola-preta',
'125;10;Segunda fase;;2;28/07/2019;10:15;layser;unidos',
'126;10;Segunda fase;;2;28/07/2019;11:30;duque-america;sao-jose',
'127;11;Segunda fase;;1;30/07/2019;19:15;duque-america;fibrax-ii',
'128;11;Segunda fase;;1;30/07/2019;20:45;fibrax-iii;democrata-b',
'129;11;Segunda fase;;1;31/07/2019;19:15;layser;caiex',
'130;11;Segunda fase;;1;31/07/2019;20:45;sao-jose;esperanca',
'131;11;Segunda fase;;1;01/08/2019;19:15;unidos;fama-raca',
'132;11;Segunda fase;;1;01/08/2019;20:45;puma;bola-preta',
'133;1;Quartas;;2;04/08/2019;8:45;a-definir;a-definir',
'134;1;Quartas;;2;04/08/2019;10:15;a-definir;a-definir',
'135;1;Quartas;;2;04/08/2019;11:30;a-definir;a-definir',
'136;1;Quartas;;1;07/08/2019;19:15;a-definir;a-definir',
'137;1;Semi;;1;13/08/2019;19:15;a-definir;a-definir',
'138;1;Semi;;1;13/08/2019;20:30;a-definir;a-definir',
'139;1;Final;;1;18/08/2019;09:00;a-definir;a-definir',
]



destino = context['aabb-super-master-serie-b-2019']['jogos-1']
for jogo in jogos:
#  print jogo
  jogo = jogo.split(';')


  #'﻿codigo;rodada;fase;grupo;campo;data;hora;time-a;time-b',

  codigo = "%03d" % int(jogo[0])
  rodada = jogo[1]
  fase = jogo[2]
  grupo = jogo[3]
  campo = "Campo " + jogo[4]
  data = jogo[5]
  d1 = data.split('/')
  d2 = d1[2]+'/'+d1[1]+'/'+d1[0]



  hora = jogo[6]
  timea = jogo[7]
  timeb = jogo[8]
  id = "jogo"+codigo

  dt = DateTime(d2 + ' ' + hora + ' GMT')
  print dt


  destino.invokeFactory('Jogo', id)
  obj = destino[id]
  obj.setCodigo(codigo)
  obj.setRodada(rodada)
  obj.setFase(fase)
  obj.setGrupo(grupo)
  obj.setLocal(campo)
  obj.setDataHora(dt)
  obj.setTime1(timea)
  obj.setTime2(timeb)
  obj.reindexObject()
  print id

return printed
