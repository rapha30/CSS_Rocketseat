name= input('Enter your completed name: ')
print('Your name in upper is {}.'.format(name.upper()))
print('Yor name in lower is {}.'.format(name.lower()))

'''
caractere= name.split()
caractere= ''.join(caractere)
print('The caractere number [no spaces] is {}.'.format(len(caractere)))
fname= name.split()

# fname= (fname[0]) Reduzi no .format()
# print('The first name has {} caracteres.'.format(len(fname[0])))
'''
# Reduzindo a forma de calcular a quantidade de caracteres retirando os espaços: 
print(f"The characters number is {len(name.replace(' ', ''))}.")

"""    
    Erros:
#print('The caractere number is {}.'.format(len(name.split(''.join))))
#print('The caractere number is {}.'.format(len(name.split()''.join()))) 
"""

"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""