class Watch:
    def __init__(self, h: int, m: int, s: int):
        self.__hora = 0
        self.__min = 0
        self.__sec = 0
        self.set_hora(h)
        self.set_min(m)
        self.set_sec(s)
