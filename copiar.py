#!/usr/bin/bash
# -*- coding: utf8 -*-

ano = int(input('Informe o ano de nascimento: '))
mes = int(input('Informe o mês de nascimento: '))
dia = int(input('Informe o dia de nascimento: '))
anoAtual = 2024
mesAtual = 6
diaAtual = 8

meses = ( ( anoAtual - ano ) * 12 )
print("Meses: ", meses)

if mes > mesAtual:
    # meses = meses + ( 12 - mes ) + mesAtual
    meses += ( 12 - mes ) + mesAtual
elif mes < mesAtual:
    meses += mesAtual - mes
else: # Desnecessário, está aqui apenas por didática
    meses = meses

print("Meses: ", meses)

dias = meses * 30
print("Dias: ", dias)

if dia > diaAtual:
    dias += 30 - dia + diaAtual
elif dia < diaAtual:
    dias += diaAtual - dia
else: # Desnecessário, está aqui apenas por didática
    dias = dias

print("Dias: ", dias)