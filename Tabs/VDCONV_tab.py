import tkinter as tk
from tkinter import ttk
from Calculations.VDCONV import nmol_to_ng

class VDCONV_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="Unit")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campo para valor
        ttk.Label(self.tab, text="Value (nmol/L):").grid(
            row=0, column=0, sticky="w", pady=5,
        )
        self.valor = ttk.Entry(self.tab, justify='center')
        self.valor.grid(row=0, column=1, sticky="w")

        #Campos vacios para espaciado
        ttk.Label(self.tab).grid(
            row=1, column=0, sticky="w", pady=5
        )
        ttk.Label(self.tab).grid(
            row=2, column=0, sticky="w", pady=5
        )
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
        r = nmol_to_ng(self.valor.get())

        self.result.set(r)