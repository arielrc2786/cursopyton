#try..captura los errores y poder controlarlos
#n1 = int(input('digite un nro'))

try:
    nro1=int(input('digite nro 1'))
    nro2=int(input('digite nro 2'))
    suma= nro1 + nro2
    print(f'la suma es  {suma}')
except:
    print('Error esto no es un numero')    