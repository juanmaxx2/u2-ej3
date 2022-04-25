import csv
from VariablesMeteorologicas import VM

if __name__ == '__main__':
    lista=[]
    archivo=open("Registro.csv")
    reader=csv.reader(archivo,delimiter=",")
    for fila in reader:
        magnitudes=VM(int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),float(fila[4]))
        lista.append(magnitudes)
    x=0
    while x != 4:
       print('1) Mostrar dia y hora menor y mayor valor/variable')
       print('2) Indicar la temperatura mensual por cada hora')
       print('3) Mostrar las 3 variables de un dia')
       print('4) Salir')
       x=int(input('\nIngrese opcion que desea realizar:'))
       
       if x==1:
           temp=
           temp1=
           hum=
           hum1=
           pres=
           pres1=
           print('el dia y la hora de temperatura de menor valor es:', format(temp))
           print('el dia y la hora de temperatura de mayor valor es:', format(temp1))
           print('el dia y la hora de humedad de menor valor es:', format(hum))
           print('el dia y la hora de humedad de mayor valor es:', format(hum1))
           print('el dia y la hora de presion de menor valor es:', format(pres))
           print('el dia y la hora de presion de mayor valor es:', format(pres1))