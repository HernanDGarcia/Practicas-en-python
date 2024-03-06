'''
'''

from personas import Empleado
from objetos import Tarjeta

t1 = Tarjeta("001")
e1 = Empleado("diego", t1)

e1.fichar()