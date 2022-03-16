# O Banco Proway agora decidiu que precisa implementar o sistema de
# distribuição inteligente!
# Esse sistema consiste em entregar a menor quantidade possível de cédulas para o
# cliente.
# Exemplo: Valor de saque: 127
# Notas de 100 -> 1
# Notas de 50 -> 0
# Notas de 20 -> 1
# Notas de 10 -> 0
# Notas de 5 -> 1
# Notas de 2 -> 1
# Notas de 1 -> 0
# Tempo estimado: 20 minutos!
# Não mostrar com saldo zero


t100 = 0
t50 = 0
t20 = 0
t10 = 0
t5 = 0
t2 = 0
t1 = 0


t1 = 0
valor = int(input('Valor do Saque: '))
while (valor >= 100):
    t100 += 1
    valor -= 100
while (valor >= 50):
    t100 += 1
    valor -= 50
while (valor >= 20):
    t20 += 1
    valor -= 20
while (valor >= 10):
    t10 += 1
    valor -= 10
while (valor >= 5):
    t5 += 1
    valor -= 5
while (valor >= 2):
    t2 += 1
    valor -= 2
while (valor >= 1):
    t1 += 1
    valor -= 1


if(t100 > 0):
    print('Total de notas de R$ 100 ->' + str(t100))
if(t50 > 0):
    print('Total de notas de R$ 50 ->' + str(t50))
if(t20 > 0):
    print('Total de notas de R$ 20 ->' + str(t20))
if(t10 > 0):
    print('Total de notas de R$ 10 ->' + str(t10))
if(t5 > 0):
    print('Total de notas de R$ 5 ->' + str(t5))
if(t2 > 0):
    print('Total de notas de R$ 2 ->' + str(t2))
if(t1 > 0):
    print('Total de notas de R$ 1 ->' + str(t1))
