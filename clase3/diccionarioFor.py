#imprimir o mostrar el diccionario
#crear un diccionario vacion

Estudiantes={}

#dos variables Cedula y otra para el nombre y el celular
#dicc={key:valor}

for i in range(2):
    cedula=input('Digite la Cedula ')
    datos=input('Nombre y celular ')
    Estudiantes[cedula]=datos
    print('\n')

print('DATOS ESTUDIANTES'.center(50,'─'))
for cedula, datos in Estudiantes.items():
    print ('Cedula' + cedula + 'Nombre y celuar' + datos) 

