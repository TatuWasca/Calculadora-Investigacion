from math import sqrt

def calcular_dec(n_casos, n_controles, de_casos, de_controles):
        n1  = float(n_casos)
        n2  = float(n_controles)

        de1 = float(de_casos)
        de2 = float(de_controles)

        numerador   = ((n1 - 1) * de1**2) + ((n2 - 1) * de2**2)
        denominador = (n1 + n2 - 2)

        dec = sqrt(numerador/denominador)

        return f"{dec:.9f}"