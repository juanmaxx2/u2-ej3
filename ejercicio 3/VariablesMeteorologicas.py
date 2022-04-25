class VM():
    __dia=int
    __hora=int
    __temperatura=int
    __humedad=int
    __presion=float
    
    def __init__(self,dia,hora,temperatura,humedad,presion):
        self.__dia=dia
        self.__hora=hora
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion
    
    def temperatura(self):
        