import random
def suma(a,b):
    res = a+b
    return "soy una suma", res

tipo, resultado = suma(3,4)
#print(tipo)
#print(resultado)

def get_stats():
    dados = [random.randint(1, 6) for i in range(4)]
    dados.sort()
    max_dados = dados[1:]
    return sum(max_dados)

stats = {
    "str": get_stats(),
    "agi": get_stats(),
    "inte": get_stats(),
}

print(stats)