import csv
from VariablesMeteorologicas import Variable

if __name__ == '__main__':
    lista=[]
    for i in range(30):
        lista.append([0]*24)
        
    archivo=open('mes.csv')
    reader=csv.reader(archivo,delimiter=',')
        
    for fila in reader:
        dia=int(fila[0])
        hora=int(fila[1])
        temperatura=float(fila[2])
        humedad=int(fila[3])
        presion=int(fila[4])
        unaVariable=Variable(dia,hora,temperatura,humedad,presion)
        lista[dia-1][hora-1]=unaVariable
    
    lista[2][0].mostrar()
    opcion=None
    while opcion!='d':
        print('\n')
        print('a) mostrar para las variables el mayor y el menor valor.')
        print('b) indicar la temperatura promedio por hora.')
        print('c) ingrese el dia y mostrar las tres variables por hora.')
        print('d) salir.')
        opcion=input('ingrese la opcion a realizar:')
    
        if opcion == 'a':
            unaVariable.menorvalortemperatura(lista)
            unaVariable.mayorvalortemperatura(lista)
            unaVariable.menorvalorhumedad(lista)
            unaVariable.mayorvalorhumedad(lista)
            unaVariable.menorvalorpresion(lista)
            unaVariable.mayorvalorpresion(lista)
    
        elif opcion == 'b':
            unaVariable.temperaturapromedio(lista)
    
        elif opcion == 'c':
            unaVariable.variabledia(lista)