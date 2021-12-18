'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''
v= float(input('Enter a speed of your car: '))
if v > 80:
    print(f"You were fined, your fine is U${(v-80)*7:.2f}, don't exceed 80km/h.")
# else: Simplificado.
#    print('Alright, can  go! :))') 
print('Alright, can  go! :))')