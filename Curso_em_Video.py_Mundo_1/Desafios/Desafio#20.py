from random import shuffle
n1= input('Enter one name: ')
n2= input('Enter seccond name: ')
n3= input('Enter quarto name: ')
n4= input('Enter terceiro name: ')
l= [n1, n2, n3, n4]
shuffle(l)
print('The sequência is {}.'.format(l))