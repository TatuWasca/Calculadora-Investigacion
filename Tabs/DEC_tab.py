import tkinter as tk
from tkinter import ttk
from Calculations.DEC import calcular_dec

class DEC_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="DEC")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campos para tamaño muestral
        ttk.Label(self.tab, text="N - Casos:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.n_casos = ttk.Entry(self.tab, justify='center')
        self.n_casos.grid(row=0, column=1, sticky="w")

        ttk.Label(self.tab, text="N - Controles:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.n_controles = ttk.Entry(self.tab, justify='center')
        self.n_controles.grid(row=1, column=1, sticky="w")

        #Campos para desviaciones estandar
        ttk.Label(self.tab, text="DE - Casos:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.de_casos = ttk.Entry(self.tab, justify='center')
        self.de_casos.grid(row=2, column=1, sticky="w")

        ttk.Label(self.tab, text="DE - Controles:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.de_controles = ttk.Entry(self.tab, justify='center')
        self.de_controles.grid(row=3, column=1, sticky="w")

        #Campos vacios para espaciado
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
        r = calcular_dec(self.n_casos.get(), 
                         self.n_controles.get(), 
                         self.de_casos.get(), 
                         self.de_controles.get()
                         )

        self.result.set(r)
        self.app.state.dec.set(r)