n = input('Digite alguma coisa ')
print('O tipo primitivo deste valor é,', type(n))
print('Só tem espaços?', n.isspace())
print('É numérico?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculo?', n.upper())
print('Está em minúsculo?', n.lower())
print('Está capitalizada?', n.istitle())