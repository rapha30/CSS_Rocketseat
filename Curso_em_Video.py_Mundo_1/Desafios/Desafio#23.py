#n= input(str('Enter a number [0 at 9999]: '))
#print('The unity is {}.'.format(n[3]))
#print('The ten is {}.'.format(n[2]))
#print('The Hundred is {}.'.format(n[1]))
#print('The Thousand is {}.'.format(n[0]))
#   Corrigir.

#   Como ainda não sei If // Else, fica:

n= int(input('Enter a number [0 at 9999]: '))
'''
u= n//10 %10
t= n//100 %10
h= n//1000 %10
T= n//10000 %10
''' #   Ou de forma reduzida:
print('The unity is {}.'.format(n%10))
print('The ten is {}.'.format(n//10 %10))
print('The Hundred is {}.'.format(n//100 %10))
print('The Thousand is {}.'.format(n//1000 %10))


#   Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
