import tkinter as tk
from tkinter import ttk
from Calculations.IC95 import calcular_ic95

class IC95_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="IC95%")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campo para prevalencia
        ttk.Label(self.tab, text="Prevalencia (%):").grid(
            row=0, column=0, sticky="w", pady=5,
        )
        self.prevalencia = ttk.Entry(self.tab, justify='center')
        self.prevalencia.grid(row=0, column=1, sticky="w")

        #Campo para precisión
        ttk.Label(self.tab, text="Precisión (n / 2):").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.precision = ttk.Entry(self.tab, justify='center')
        self.precision.insert(0, 2)
        self.precision.grid(row=1, column=1, sticky="w")
        
        #Campo para número de población
        ttk.Label(self.tab, text="N - Población (2.000):").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.tamaño_poblacion = ttk.Entry(self.tab, justify='center')
        self.tamaño_poblacion.insert(0, 2000)
        self.tamaño_poblacion.grid(row=2, column=1, sticky="w")

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
        r = calcular_ic95(self.prevalencia.get(), 
                          self.precision.get(),
                          self.tamaño_poblacion.get()
                          )

        self.result.set(r)