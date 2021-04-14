'''
Un diccionario que permita  ingresar  los departamentos  y al menos 3 ciudades importante
la primera debe ser la capital 

'''

Departamentos={}

for i in range(3):
    departamento=input('Digite Departamento')
    ciudades=input('Capital y Ciudades Principales')
    Departamentos[departamento]=ciudades
    print('\n')
print('DATOS DEPARTAMENTOS'.center(50,'─'))      
for departamento, ciudades in Departamentos.items():
    print('Departamento ' + departamento  + ' Capital y Ciudades Principales ' + ciudades)      