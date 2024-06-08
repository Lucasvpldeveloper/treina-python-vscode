#!/usr / bin /python  
# -* - coding : utf -8 -* -
ano = int(input('Qual o ano que você nasceu? '))
mes = int(input('Qual o mês você nasceu? '))
dia = int(input('Qual o dia que você nasceu? '))

meses = ( (2024 - ano) * 12 ) 

if mes > 6:
    #meses = meses (12 - mes) + 6
    meses += (12 - mes) + 6
elif mes < 6:
    meses += 6 - mes 
else: 
    meses = meses

print('Meses', meses)

dias = meses * 30

print('Dias', dias)

if dia > 8:
    dias += 30 - dia + 8
elif dia < 8:
    dias += 8 - dia
else:
    dias = dias 

print("Dias: ", dias)


