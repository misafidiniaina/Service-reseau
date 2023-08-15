
class Regle:
    def __init__(self, chain, num, target, prot, opt, source, destination,etat:list):
        self.__num = num
        self.__target = target
        self.__prot = prot
        self.__opt = opt
        self.__source = source
        self.__destination = destination
        self.__chain = chain
        self.__etat = " ".join(etat)
    @property
    def etat(self):
        return self.__etat
    @property
    def num(self):
        return self.__num

    @property
    def target(self):
        return self.__target

    @property
    def protocol(self):
        return self.__prot

    @property
    def option(self):
        return self.__opt

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def chain(self):
        return self.__chain

    def __repr__(self):
        return f"[chain={self.__chain} num={self.__num}, target={self.__target}, protocol={self.__prot}" \
               f", opt={self.__opt} source={self.__source}, destination={self.__destination}]"
