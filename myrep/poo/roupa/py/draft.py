class Roupa:
    def __init__(self):
        self.__tamanho: str = ""
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, valor: str):
        tam = ["PP", "P", "M", "G", "GG"]
        xg = ["XG"]
        xG = "".join(xg)
        tam1 = ", ".join(tam)
        if valor not in tam:
            print(f"fail: Valor inválido, tente {tam1} ou {xG}")
        else:
            self.__tamanho = valor

def main():
     roupa = Roupa()

     while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break
        elif command == "size":
            valor = str(args[1])
            roupa.setTamanho(valor)
        elif command == "show":
            tamanho = roupa.getTamanho()
            print(f"size: ({tamanho})")
main()