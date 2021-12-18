'''
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
d= float(input('Enter a distance [km/h]: '))
if d <= 200:
    print(f"The price of ticket is U${d*0.5:.2f}. ")
else:
    print(f"The price of ticket is U${d*0.45:.2f}.")