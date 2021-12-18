'''
# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randrange
from emoji import emojize
n= randrange(0, 5)
c= int(input('Please enter a number [1 ~~ 5]: '))
if c == n:
    print('Congratulations, you win!')
else:
    print('f, you lose. :/')
print(f"The number selected was {n} and its number was {c}.")

print(emojize(f"The number selected is {n} and your number was {c}.:sunglasses:", use_aliases=True))