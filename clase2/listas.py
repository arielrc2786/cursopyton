#Listas-- conjunto de datos almancenados en una variable.
#para crear una lista el nombre=[ele1,ele2...eleN]
#las listas son MUTABLES--PUEDE CAMBIAR


Estudiantes=['Yessica','Ariel','Gisela','Jesus']
notas=['Jesus',4.7,True]
#insertar elemento en una lista  APPEND,LO HACE AL FINAL DE LA LISTA 

Estudiantes.append('profe')
print('Nuevo elemento de la lista'.center(50,'*'))
print(Estudiantes)


print(f'Elemento de la posicion 2 {Estudiantes[2]}')
Estudiantes[0]='Chica Gonzalez'
print(Estudiantes)


print('\n\LISTA ORDENADA ASCENDENTE...')
#comando sort-- para ordenar la lista
Estudiantes.sort()
print (Estudiantes)
print('\n\LISTA ORDENADA DESCENDIENTE...')
Estudiantes.reverse()
print(Estudiantes)


#Eliminar elemento en una lista REMOVE  
print('Eliminar elemento de la lista'.center(50,'*'))
Estudiantes.remove ('profe')
print('Eliminado el elemento profe')
print (Estudiantes)


