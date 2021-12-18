'''
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

""" 
y= int(print('Enter a year:'))
if y <= 400:
    if y%4 == 0:
        print(f"The year {y} is leap year.")
    else: 
        print(f"The year {y} don't is leap year.") 
"""

from datetime import date
y= int(input('Enter a year or put "0" for current year:'))
if y == 0:
    y= date.today().year
if y%4 == 0 and y%100 != 0 or y%400 == 0:
    print(f"The year {y} IS leap year. ")
else:
    print(f"The year {y} DON'T leap year. ")