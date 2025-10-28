 class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def __str__(self):
        return f"{self.getNome():{self.getDinheir()}"
    
    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.dinheiro
    
    def pagar(self, valor: int):
        if valor > self.__dinheiro
            valorPago = self.__dinheiro
            self.__dinheiro = 0
            return valorPago
        if valor >= self.__dinheiro:
            self._dinheiro -= valor
            return valor
    
    def receber(self, valor:int)
        self.__dinheiro += valor

class Moto:
    def __init__(self):
        self.__custo: 0 
        self.__motorista: None
        self.__passageiro: None
    
    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
     
    def setMotorista(self, motorista: Pessoa):
        self.__motorista = motorista
    
    def setPassageiro(self, passageiro: Pessoa):
        self.__passageiro = passageiro

    def drive(self, distancia: int)
        self.__custo = distancia
    
    def leavePass(self):
        passageiro = self.__passageiro
        motorista = self.__motorista
        custo = self.__custo
        if passageiro.getDinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")
        pagar(passageiro) = custo
        receber(motorista) = custo
        self.__custo = 0
        self.__passageiro = None

        


        


        
            