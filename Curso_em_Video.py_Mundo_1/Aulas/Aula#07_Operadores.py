''' 
n=int(input('Digite o número 01: '))
n2=int(input('Agora o número 02: '))
print('A soma entre {} e {} é igual a  {}!'.format(n, n2, n+n2))

Simbolos: 
** ou pow(x, y) = potenciação
// = Divisão Inteira
% = Resto da divisão

Ordem de precedência:
() > ** > *, /, //, % > +, -

Para calcular raizes, então eleva à frações:
Ex.: 27**(1/3)
'''
n1= int(input('Digite um valor: '))
n2= int(input('digite outro valor: '))
s= n1+n2
m= n1*n2
d= n1/n2
p= n1**n2
di= n1//n2
r= n1%n2
print('A sua soma é {}, sua multiplicação é {}, divisão {:.2f} e potenciação {}!'.format(s, m, d, p), end=' ') # end=' ' serviu para não quebrar linha.
print('Sua divisão inteira {} e o resto {}.'.format(di, r))