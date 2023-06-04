from .pessoa import Pessoa

def getData(compra):
    return compra.data

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []


    def registroCompra(self, compra):
        self.compras.append(compra)


    def getUltimaCompra(self):
        return None if not self.compras else sorted(self.compras, key=getData)[-1].data


    def totalCompras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total