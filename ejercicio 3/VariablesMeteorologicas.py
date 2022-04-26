class Variable:
    __dia=''
    __hora=''
    __temperatura=''
    __humedad=''
    __presion=''
    
    def __init__(self,dia,hora,temperatura,humedad,presion):
        self.__dia=dia
        self.__hora=hora
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion
    
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion (self):
        return self.__presion
    
    def mostrar(self):
            print (str(self.__dia)+','+str(self.__temperatura)+','+str(self.__humedad)+','+str(self.__presion))
            
    def menorvalortemperatura(self,lista):
        mini=9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].getTemperatura()<mini:
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    mini=lista[i][j].getTemperatura()
        print('\nEl valor minimo de temperatura es:' + str(mini) + ' , la hora es:' + str(hora) + ' y el dia es:' + str(dia))
                
    def mayorvalortemperatura(self,lista):
        maxi=-9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if maxi<lista[i][j].getTemperatura():
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    maxi=lista[i][j].getTemperatura()
        print('\nEl valor maximo de temperatura es:' + str(maxi) + 'y la hora es:' + str(hora) + 'y el dia es:' + str(dia))
    
    def menorvalorhumedad(self,lista):
        mini=9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].getHumedad()<mini:
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    mini=lista[i][j].getHumedad()
        print('\nEl valor minimo de humedad es:' + str(mini) + ' y la hora es:' + str(hora) + ' y el dia es:' + str(dia))

    def mayorvalorhumedad(self,lista):
        maxi=-9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].getHumedad()>maxi:
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    maxi=lista[i][j].getHumedad()
        print('\nEl valor maximo de temperatura es:' + str(maxi) + ' y la hora es:' + str(hora) + 'y el dia es:' + str(dia))
    
    def menorvalorpresion(self,lista):
        mini=9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].getPresion()<mini:
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    mini=lista[i][j].getPresion()
        print('\nEl valor minimo de presion es:' + str(mini) + ' y la hora es:' + str(hora) + 'y el dia es:' + str(dia))
        
    def mayorvalorpresion(self,lista):
        maxi=-9999999
        hora=None
        dia=None
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].getPresion()>maxi:
                    hora=lista[i][j].getHora()
                    dia=lista[i][j].getDia()
                    maxi=lista[i][j].getPresion()
        print('\nEl valor maximo de presion es:' + str(maxi) + ' y la hora es:' + str(hora) + 'y el dia es:' + str(dia))
        
    def temperaturapromedio(self,lista):
        cant=1
        prom=0
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                prom=prom+int(lista[i][j].getTemperatura())
                cant=cant+1
        prom=prom/cant
        print('\nLa temperatura promedio es:', format(prom))
    
    def variabledia(self,lista):
        i=input('ingrese dia que desee buscar las variables por hora:')
        for j in range(len(lista[i])):
            print('en la hora:'+j+'la temperatura fue:'+lista[i][j].getTemperatura+' la humedad fue:'+lista[i][j].getHumedad+' y la presion:'+lista[i][j].getPresion)