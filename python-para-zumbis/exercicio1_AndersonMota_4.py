from __future__ import division

salario = input("Digite o valor do salario:")
percentual = input("Digite o percentual de aumento:")

aumento = (percentual / 100) * salario
print "Valor do aumento: %.2f" %aumento
print "Valor total do novo salário: %.2f" %(aumento + salario)