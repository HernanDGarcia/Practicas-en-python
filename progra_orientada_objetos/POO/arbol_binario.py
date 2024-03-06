'''
Binary Search Tree
Estructura muy compleja y lina que te permite buscar datos de forma mas
rápida que con una lista
'''

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, valor):
        if self.root:
            self.root.add_node(valor)
        else:
            self.root = Nodo_tree(valor)

    def buscar_valor(self, valor):
        print(f"buscando valor {valor}")

        if self.root:
            self.root.buscar_valor(valor)

        else:
            print("el valor no exisite")                
     
class Nodo_tree:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

    def add_node(self, valor):
        if valor < self.valor:
             # Inserta en el nodo de la izquierda
            if self.left:
                self.left.add_node
            else:
                self.left = Nodo_tree(valor)
        elif valor > self.valor:
            if self.right:
                self.right.add_node
            else:
                self.right = Nodo_tree(valor)

    def buscar_valor(self, valor):
        if valor == self.valor:
            print("valor encontrado")

        elif valor < self.valor:
            if self.left:
                self.left.buscar_valor(valor)
            else:
                print("el valor no existe")
        
        elif valor > self.valor:
            if self.right:
                self.right.buscar_valor(valor)
            else:
                print("el valor no existe")

arbol = Tree()

#[9, 5, 35, 2, 7, 23]

arbol.add_node(9)
arbol.add_node(5)
arbol.add_node(35)
arbol.add_node(2)
arbol.add_node(7)
arbol.add_node(23)

arbol.buscar_valor(5)