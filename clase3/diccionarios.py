'''
Diccionarios
*son elementos no ordendos
*se pueden indexar
*SON MUTEABLES...se pueden modificar
*NO PERMITEN CLAVES REPETIDAS}
*Dentro de un diccionario pueden existir otros diccionarios

CONCEPTOS
llave-- que este me identifica el elemento, hace las veces de indice
valor-- contenido de la llave


llave:valor
key:valor


Cedula     nombre    celular 
123  :      Gisela    300-300-30-30
'''

Estudiantes = {123:'Gisela 300-300-30-30',124:['Ariel,3010-301-31-31,320-320-2020'],125:'Jesus 321-321-2121'}

print(Estudiantes)
print()

print(Estudiantes[123])
print(Estudiantes[124])
print(Estudiantes[125])

#Agregar un nuevo elemento,siempre lo hace al final 

Estudiantes[126]='Yessica 318-318-1818'

print('\n\n')
print(Estudiantes)

#Modificar un elemento,debo hacerlo por la key 
Estudiantes[125]='Jesus 321-321-2020'
print('\n\n')
print(Estudiantes)
print(Estudiantes[125])

#Buscar un key dentro del diccionario..GET
print(123 in Estudiantes)

print(Estudiantes.get(123,'El Dato no existe o esta mal digitado'))

#Mostrar todas las llaves o los key

print (Estudiantes.keys())

#Mostrar todas las llaves o los key
print (Estudiantes.values())

