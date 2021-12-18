n= input('Enter a name: ').split()
# n= n.split() Foi reduzido.
print('The fisrt name is {}.'.format((n[0])))
print('The last name is {}.'.format(n[len(n)-1]))

# O len() de um split conta a quatidade de itens na lista [começando do 1 e não do "0" (padrão python)]

#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.