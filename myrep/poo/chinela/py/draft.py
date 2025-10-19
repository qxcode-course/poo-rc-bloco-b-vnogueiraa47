class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, value: int):
        if (value >= 20) and (value <= 50) and (value % 2 == 0):
            self.__tamanho = value
        else:
            print("fail: tamanho inválido")

chinela = Chinela()


while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho) 

print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())