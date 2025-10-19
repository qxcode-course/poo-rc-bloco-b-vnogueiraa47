class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, valor: str):
        tam = ["PP", "P", "M", "G", "GG", "XG"]
        tam1 = ", ".join(tam)
        if valor not in tam:
            print(f"Tamanho invalido, os tamanhos permitidos são {tam1}")
        else:
            self.__tamanho = valor

camisa = Camisa()

while camisa.getTamanho() == "":
    print("Digite seu tamanho de camisa")
    tamanho = input()
    camisa.setTamanho(tamanho) 

print("Parabens, você comprou uma camisa tamanho", camisa.getTamanho())
