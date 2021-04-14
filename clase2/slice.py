listaMercado=['carne','pollo','huevo','arepas','leche','arroz','papas','cafe','panela','carnes frias','parva','quesito']

#Longitud o tamaño de una lista LEN
print (listaMercado)
print(f'Nro de elementos de la lista {len(listaMercado)}') 

print('lista ordenada'.center(50,'─'))
listaMercado.sort()
print(listaMercado)

#slice-- Son para Imprimir rangos de posicion de los elementos
print('\n\nListar los 4 primeros elementos de la lista')
print (listaMercado[0:4])

print('\n\nMostrar la lista con salto de elementos')
print (listaMercado[0::2])

print('\n Mostrar el ultimo elemento de la lista')
print('El ultimo elemento de la lista es',listaMercado[-1])

print('\nBuscar elemento dentro de una lista')

print('cafe'in listaMercado)

print(listaMercado[4:])#desde el elemento .... hasta el final
print(listaMercado[:5])#empieza en inicio hasta el final 