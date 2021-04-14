#if se utiliza para realizar comparaciones con los datos

'''
 if(pregunta)
    instruccion
 else
    instruccion
aniado
if(pregunta)
    instruccion
elif
    instruccion
elif
    instruccion
else
    instruccion
 
'''
print('digitar dos numeros diferenes y decir cual es el mayor \n')

nro1=int(input('Nro 1'))
nro2=int(input('Nro 2'))
nro3=int(input('Nro 3'))

if nro1 > nro2:
   print(f'El numero {nro1} es el mayor')
   print('mas instrucciones.tantas linesas como necesite') 
   print('mas instrucciones.tantas linesas como necesite') 
   print('mas instrucciones.tantas linesas como necesite') 
else:
    print(f'El numero {nro2} es el mayor')
    print('mas instrucciones.tantas linesas como necesite') 
    print('mas instrucciones.tantas linesas como necesite') 
    print('mas instrucciones.tantas linesas como necesite') 

print('Digitar tres numeros DIFERENTES y decir cual es el mayor \n')         

if nro1 > nro2 and nro1 >nro3:
    print(f'El numero {nro1} es el mayor')
elif nro2 > nro3:
    print(f'El numero {nro2} es el mayor')
else:
    print(f'El numero {nro3} es el mayor')    



