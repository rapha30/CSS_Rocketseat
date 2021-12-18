frase='Curso em Video Python'
# TODA CONTAGEM DE CARACTERE COMEÇA DO NUMERAL "0".
print(frase[9]) # É a DÉCIMA letra, os caracteres começam a ser contados do "0".
print(frase[9:13]) # Vai do caractere "0" até o "12" POIS o "13" é ignorado (como se fosse INTERVALO ABERTO).
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2]) # O :2 após a separação significa que PULA de 2 em 2.
# PODERIA SER ASSIM PARA IR DO INICIO AO FIM PULANDO DE 2 EM 2: print(frase[::2])
print(frase[:5]) # Significa do início (não tem nada da esse sentido) até o caractere 5, a QUARTA letra começando do 1.
print(frase[15:]) # Do caractere 15 ao fim.
print(frase[9::3])
len(frase) # len= quantidade de caracteres.
frase.count('o') # conta quantos "o" tem em 'frase'.
# Em frase.count('O') Vai retornar 0, pois não tem "O" ("o" maiúsculo) em 'frase', MAS se fizer frase.upper().count('O') Retornará 3, 
# Pois vai pesquisar "O" na frase posta em maiúscula pelo .upper().
frase.count('o', 0, 13) # conta do caractere 0 até o 12 (o 13 não conta, como se fosse intervalo aberto).
frase.find('deo') # encontra o 'deo' e indica o caractere que se inicia.
frase.rfind('deo') # encontra o 'deo' começando a procura do lado direito para o esquerdo.
frase.find('Android') # como não existe ele retorna '-1'.
'Curso' in frase # verifica se tem e retorna "True" or "false".
frase.replace('Python', 'Android') # Troca a palavra. (Substitue, inverte) replace= substituir
frase.upper() # Colocar TUDO Maiúsculo.
frase.lower() # Colocar TUDO Minúsculo.
frase.capitalize() # Deixa o primeiro em maiúsculo.
frase.title() # Deixa a inicial de toda palavra maiúscula.

frase1= ('   Aprenda Python  ')
frase.strip() # Exclui os espaços inúteis (à direita e à esquerda)
frase.rstrip() # O lado direito é excluido.
frase.lstrip() # O lado esquerdo.

# Retornando à "frase"
frase= 'Cuso em Video Python'
# Como tirar os espaços ENTRE as palavras?
frase.split() # Divide em lista cada palavra [divide pelos espaços].
'-'.join(frase) # Junta os elementos que foram DESTACADOS com split, junta colocando "-".

# OBS: TEM SPLIT >< DE STRIP, O SPLIT É O QUE SEPARA EM LISTA.

print("""As I walk through the valley of the shadow of death
I take a look at my life, and realize there's nothin' left
'Cause I've been blastin' and laughin' so long
That even my momma thinks that my mind is gone""") # Para poder escrever o texto por completo sem varios "print()".

""" $ pip install unidecode

from unidecode import unidecode
str1 = 'café'
print(unidecode(str1))
cafe # Tira acentuação.
"""