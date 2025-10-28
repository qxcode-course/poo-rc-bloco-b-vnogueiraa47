class Watch:
    def __init__(self, h: int, m: int, s: int):
        self.__hora = 0
        self.__min = 0
        self.__sec = 0
        self.set_hora(h)
        self.set_min(m)
        self.set_sec(s)

    def set_hora(self, valor:int):
        if valor < 0 or valor > 23:
            print("fail: hora inválida")
            return self
        self.__hora = valor
        return self

    def set_min(self, valor:int):
        if valor < 0 or valor > 59:
            print("fail: minuto inválido")
            return self
        self.__min = valor
        return self

    def set_sec(self, valor:int):
        if valor < 0 or valor > 59:
            print("fail: segundo inválido")
            return self
        self.__sec = valor
        return self
    
    def get_hora(self):
        return self.__hora
    
    def get_min(self):
        return self.__min

    def get_sec(self):
        return self.__sec
    
    def __str__(self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__sec:02d}"
    
    

        
