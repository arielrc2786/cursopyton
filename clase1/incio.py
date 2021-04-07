print(''.center(100,'─'))
print('Desarrollador: Ariel Rivera Correa')
print('Correo:arielriverac@hotmail.com')
print('Tema:Introduccion')
print('Fecha:5 Abril 2021')
print(''.center(100,'─'))

# variables
#dinamicamente tipado
#sumar dos numeros cualquiera

#print -- menajes en pantalla
#capturar el contenido in 

""" nro1=int(input('Nro 1'))
nro2=int(input('Nro 2'))
suma= nro1 + nro2
print('suma=' , suma) """

# variables de tipo texto y concatenar

print('* FUNCIONES DE CADENA *'.center(100))

texto = 'Desarrollo de software'

print(texto.center(100))
print(texto.rjust(100))
print(texto.ljust(100))

print(texto.lower())#todo en minuscula
print(texto.upper())# todo en mayuscula
print(texto.capitalize())# inicial en mayuscula

#concatenar

nombre='Ariel'
Saludo=' como estas?'
Curso= 'Python'
print('Hola {} {} bienvenid@ al curso de {}'+Saludo,nombre,Curso)
print('Hola {} {} bienvenid@ al curso de {}'.format(nombre,Saludo,Curso))
print(f'Hola {nombre} {Saludo} Bienvenid@ al curso de {Curso}', )