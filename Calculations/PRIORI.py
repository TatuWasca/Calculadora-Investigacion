from math import ceil
from statsmodels.stats.power import TTestIndPower

def calcular_potencia_priori(d_cohen, error_alpha, potencia, ratio):
        COHEN_D = float(d_cohen)
        ALPHA   = float(error_alpha)
        POWER   = float(potencia)
        RATIO   = float(ratio)        #Casos : Controles

        analysis = TTestIndPower()

        n = analysis.solve_power(
            effect_size=COHEN_D,
            alpha=ALPHA,
            power=POWER,
            ratio=RATIO,
            alternative="two-sided"
        )

        n_redondeado = ceil(n)
        total        = n_redondeado * 2

        return str(total) + " | " + str(n_redondeado) + " - " + str(n_redondeado)