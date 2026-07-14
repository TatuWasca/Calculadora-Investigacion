from math import ceil

def calcular_ic95(prevalencia, precision, tamaño_poblacion):
    p = float(prevalencia) / 100
    q = 1 - p
    d = p / float(precision)
    z = 1.96

    # Tamaño muestral sin corrección
    n        = ((z**2) * p * q) / (d**2)
    result_n = ceil(n)

    # Corrección por población finita
    N = float(tamaño_poblacion)
    if N != 0:
        n_corr   = n / (1 + ((n - 1) / N))
        result_N = ceil(n_corr)
    
        return str(result_n) + " | " + str(result_N)
    else:
        return str(result_n)