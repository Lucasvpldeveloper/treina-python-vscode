#!/usr / bin /python  
# -* - coding : utf -8 -* -

nome = str(input('Qual é o seu nome? '))
salario1 = float(input('Qual é o seu salário fixo? R$'))
salario2 = float(input("Quanto você vendeu no mês? R$"))

salario3 = (salario2 * 15) / 100

print(nome, 'Seu salário fixo é R$', salario1, 'e sua comissão foi R$', salario3, 'total = R$',(salario2 + salario3))