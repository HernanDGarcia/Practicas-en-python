import json
import numpy as np

def get_nombres():
    with open('nombres.json', 'r') as fn:
        names = json.load(fn)

    return np.random.choice(names, 30)
