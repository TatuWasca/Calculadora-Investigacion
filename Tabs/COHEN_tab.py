import tkinter as tk
from tkinter import ttk
from Calculations.COHEN import calcular_d_de_cohen

class COHEN_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="D de Cohen")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campos para media de casos y controles
        ttk.Label(self.tab, text="x̄ - Casos:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.media_casos = ttk.Entry(self.tab, justify='center')
        self.media_casos.grid(row=0, column=1, sticky="w")

        ttk.Label(self.tab, text="x̄ - Controles:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.media_controles = ttk.Entry(self.tab, justify='center')
        self.media_controles.grid(row=1, column=1, sticky="w")

        #Campo para desviación estandar combinada
        ttk.Label(self.tab, text="DE combinada:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.dec_d_cohen = ttk.Entry(self.tab, justify='center', textvariable=self.app.state.dec)
        self.dec_d_cohen.grid(row=2, column=1, sticky="w")

        #Campos vacios para espaciado
        ttk.Label(self.tab).grid(
            row=3, column=0, sticky="w", pady=5
        )
        ttk.Label(self.tab).grid(
            row=4, column=0, sticky="w", pady=5
        )
        ttk.Label(self.tab).grid(
            row=5, column=0, sticky="w", pady=5
        )
        ttk.Label(self.tab).grid(
            row=6, column=0, sticky="w", pady=5
        )

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
        r = calcular_d_de_cohen(self.media_casos.get(), 
                                self.media_controles.get(), 
                                self.dec_d_cohen.get()
                                )

        self.result.set(r)
        self.app.state.cohen.set(r)