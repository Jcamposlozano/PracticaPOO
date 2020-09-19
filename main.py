from Empleado import *

empleados = []


e1 = Empleado()
e1.setNombre('Jonathan')
#e1.nombre = 'Jonathan' #### ESTO ESTA MAL
e1.setApellido('Campos Lozano')
e1.setSueldo(1000000)
e1.setDiasLiquidados(10)
empleados.append(e1) #Ingreso informacion en el arreglo


e2 = Empleado()
e2.setNombre('Angelica')
e2.setApellido('Franco R')
e2.setSueldo(2500000)
e2.setDiasLiquidados(30)
empleados.append(e2) #Ingreso informacion en el arreglo


#for i in empleados:
#    print('********************')
#    print(i)

f = open('empleados.txt', 'w')
for i in empleados:
    f.write('\n******************\n')
    f.write(str(i))
f.close()



