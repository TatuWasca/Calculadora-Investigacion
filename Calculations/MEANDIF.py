from math import ceil
from statistics import NormalDist


def calcular_diferencia_medias(m1, m2, de1, de2, confidence, power, ratio):
    M1         = float(m1)
    M2         = float(m2)
    DE1        = float(de1)
    DE2        = float(de2)
    CONFIDENCE = float(confidence)
    POWER      = float(power)
    RATIO      = float(ratio)

    ALPHA      = 1 - CONFIDENCE / 100
    BETA       = 1 - POWER / 100

    Z_ALPHA    = NormalDist().inv_cdf(1 - ALPHA / 2)
    Z_BETA     = NormalDist().inv_cdf(1 - BETA)
    DELTA      = abs(M1 - M2)

    n1_num     = ((Z_ALPHA + Z_BETA) ** 2) * (DE1 ** 2 + (DE2 ** 2) / RATIO)
    n1_den     = DELTA ** 2

    n1         = round(n1_num / n1_den)
    n2         = round(RATIO  * n1)
    total      = n1 + n2 + 1 if (n1 + n2) % 2 == 1 else n1 + n2

    return str(total) + " | " + str(n1) + " - " + str(n2)