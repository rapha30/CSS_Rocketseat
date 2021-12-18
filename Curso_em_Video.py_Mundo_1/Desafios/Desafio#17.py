from math import sqrt, pow, exp
co= float(input('Enter the adjacent leg: ')) 
ca= float(input('Enter the opposite leg: '))
m= input('Enter the unit of measurement [cm, m, km]: ')
print('The length of hypotenuse is {}{}!'.format(sqrt(co**2+ca**2), m))
# print('The length of hypotenuse is {}{}!'.format(sqrt((pow(co, 2))+(pow(co, 2))), m)) = dando erro!