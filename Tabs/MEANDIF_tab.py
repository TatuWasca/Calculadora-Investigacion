import tkinter as tk
from tkinter import ttk
from Calculations.MEANDIF import calcular_diferencia_medias

class MEANDIF_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="Mean Difference")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campo para media casos
        ttk.Label(self.tab, text="x̄ - Casos:").grid(
            row=0, column=0, sticky="w", pady=5,
        )
        self.m_casos = ttk.Entry(self.tab, justify='center')
        self.m_casos.grid(row=0, column=1, sticky="w")
        
        #Campo para media controles
        ttk.Label(self.tab, text="x̄ - Controles:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.m_controles = ttk.Entry(self.tab, justify='center')
        self.m_controles.grid(row=1, column=1, sticky="w")

        #Campo para desviación estandar casos
        ttk.Label(self.tab, text="DE - Casos:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.de_casos = ttk.Entry(self.tab, justify='center')
        self.de_casos.grid(row=2, column=1, sticky="w")

        #Campo para desviación estandar controles
        ttk.Label(self.tab, text="DE - Controles:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.de_controles = ttk.Entry(self.tab, justify='center')
        self.de_controles.grid(row=3, column=1, sticky="w")

        #Campo para nivel de confianza
        ttk.Label(self.tab, text="Confianza (95%):").grid(
            row=4, column=0, sticky="w", pady=5
        )
        self.confianza = ttk.Entry(self.tab, justify='center')
        self.confianza.insert(0, 95)
        self.confianza.grid(row=4, column=1, sticky="w")
        
        #Campo para potencia
        ttk.Label(self.tab, text="Potencia (80):").grid(
            row=5, column=0, sticky="w", pady=5
        )
        self.power = ttk.Entry(self.tab, justify='center')
        self.power.insert(0, 80)
        self.power.grid(row=5, column=1, sticky="w")

        #Campo para ratio
        ttk.Label(self.tab, text="Ratio (n2 : n1):").grid(
            row=6, column=0, sticky="w", pady=5
        )
        self.ratio = ttk.Entry(self.tab, justify='center')
        self.ratio.insert(0, 1)
        self.ratio.grid(row=6, column=1, sticky="w")

        #Botón para calcular
        ttk.Button(
            self.tab,
            text="Calcular",
            command=self.calcular
        ).grid(row=7, column=0, columnspan=2, pady=15)

        #Resultado
        ttk.Label(self.tab, text="Resultado:").grid(
            row=8, column=0, sticky="w"
        )
        ttk.Entry(
            self.tab,
            justify='center',
            textvariable=self.result,
            state="readonly",
            width=20
        ).grid(row=8, column=1)
    
    def calcular(self):
        r = calcular_diferencia_medias(self.m_casos.get(), 
                                       self.m_controles.get(),
                                       self.de_casos.get(),
                                       self.de_controles.get(),
                                       self.confianza.get(),
                                       self.power.get(),
                                       self.ratio.get()
                                       )

        self.result.set(r)