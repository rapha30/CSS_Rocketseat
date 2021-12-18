'''
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
n= int(input('Enter a number: '))
if n%2 == 0:
    print(f"The number {n} is even.")
else:
    print(f"The numbeer {n} is odd. ")