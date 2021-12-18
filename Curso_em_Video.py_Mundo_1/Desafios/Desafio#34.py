'''
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
wage= float(input("Enter your wage: "))
if wage > 1250:
    print(F"Your salary with increase is U${wage*1.1:.2f}. ")
else:
    print(F"Your salary with increase is U${wage*1.15:.2f}. ")