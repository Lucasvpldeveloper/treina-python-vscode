#!/usr / bin /python  
# -* - coding : utf -8 -* -
custo = float(input('Qual o valor do seu produto? '))
porcentagem = float(input('Quantos % você gostaria de adicionar ao seu produto? '))
tot1 = porcentagem / 100
tot2 = tot1 * custo 
tot3 = custo + tot2
print('Então R$', custo, '+', porcentagem, '% = R$', tot3)