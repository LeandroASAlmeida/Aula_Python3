#Elaborar um algoritmo que peça para o usuario ir digitando um valor inteiro
#A saida do laço sera -1
#ao final  devera retornar a soma dos valores informados

n1 = 0
soma = 0

while (n1 != -1):
    soma = soma + n1
    n1 = int(input("INFORME UM NUMERO INTEIRO : "))
    
print('A soma dos valores: ' + str(soma))
