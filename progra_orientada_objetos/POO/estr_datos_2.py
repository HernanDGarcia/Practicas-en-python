'''
estructura de datos 
'''

class Lista_se:
    '''
    Cabeza de la lista simplemente enlazada
    '''
    def __init__(self):
        self.nodo = None
    
    def agregar(self, valor):
        if self.nodo:
            self.nodo.agregar(valor)
        else:
            self.nodo = Nodo_se(valor)

    def listar(self):
        return self.nodo.listar()

    def size(self):
        if self.nodo:
            return self.nodo.size()
        else:
            return 0
            

class Nodo_se:
    '''
    Nodo de la lista simplemente enlazada
    '''
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
    def agregar(self, valor):
        if self.next:
            self.next.agregar(valor)
        else:
            self.next = Nodo_se(valor)
    
    def listar(self):
        if self.next:
            siguiente = self.next.listar()
        else:
            return self.valor

        return f"{self.valor} {siguiente}"
    
    def size(self):
        if self.next:
            elemento = 1
            return elemento + self.next.size()
        else:
            return 0

    

if __name__ == "__main__":
    lista = Lista_se()


    lista.agregar(5)
    lista.agregar(3)
    lista.agregar(4)
    lista.agregar(8)
    lista.agregar(2)

    res = lista.listar()
    print(res)

    cantidad = lista.size()
    print(cantidad)