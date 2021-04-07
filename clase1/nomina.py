print(''.center(100,'─'))
print('Desarrollador: Ariel Rivera Correa')
print('Correo:arielriverac@hotmail.com')
print('Tema:Introduccion')
print('Fecha:5 Abril 2021')
print('CALCULAR NOMINA'.center(100,'─'))


#Nombre,salario,nrotrabajadas,calcular el pago
'''Dato Entrada
      nombre,salario,nrotrabajadas
    Datos Proceso
        vlrHora = salario/240
        totalPago= valorHora * nroTrabajadas
    Datos Salida
        nombre,salario,nrotrabajadas,totalPago    
    
'''
# Datos de entrada
nombre=input('Nombre ----->')
salario=int(input('Salario ------->'))
nroHorTrab=int(input('Hora trabajadas -->'))

#datos proceso
vlrHora= salario/240
totalPago= vlrHora * nroHorTrab

#datos salida
print(f'{nombre}'.center(50,'─'))
print(f'Salario-----> {salario}')
print(f'Valor Hora----> {vlrHora}')
print(f'Horas Trabajadas--> {nroHorTrab}')
print(f'total a pagar ---->{totalPago}')

