def calcular_d_de_cohen(media_casos, media_controles, dec_cohen):
        media_casos     = float(media_casos)
        media_controles = float(media_controles)
        dec             = float(dec_cohen)

        d = (media_controles - media_casos) / dec

        return f"{d:.9f}"