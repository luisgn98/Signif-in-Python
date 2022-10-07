import math

def signif(x, n):
    return round(x, n - int(math.floor(math.log10(abs(x)))) - 1)