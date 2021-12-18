''' 
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 
'''
n1= float(input('Enter a first number: '))
n2= float(input('Enter a seccound number: '))
n3= float(input('Enter a third number: '))
# Verificando o menor:
lower= n1
if n2 < n3 and n2 < n1:
    lower= n2
if n3 < n2 and n3 < n1:
    lower= n3
# Verificando o maior:
biggest= n1
if n2 > n1 and n2 > n3:
    biggest= n2
if n3 > n1 and n3 > n2:
    biggest= n3
print(F"The lower number is {lower:.2f}.")
print(F"The biggest number is {biggest:.2f}.")

# if n1 == n2:
#   print('The first number is equal as the seccound: ')

""" if n1 > n2 and n1 > n3:
    print(f"The biggest number is {n1}.")
if n2 > n1 and n2 > n3:
    print(f"The biggest number is {n2}.")
if n3 > n2 and n3 > n1:
    print(f"The biggest number is {n3}.") 
if n1 < n2 and n1 < n3:
    print(f"The lower number is {n1}.")
if n2 < n1 and n2 < n3:
    print(f"The lower number is {n2}.")
if n3 < n2 and n3 < n1:
    print(f"The lower number is {n3}.")
print(f"The numbers were {n1, n2, n3}")""" # Foi Resumido.