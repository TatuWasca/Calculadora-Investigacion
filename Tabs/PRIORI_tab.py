import tkinter as tk
from tkinter import ttk
from Calculations.PRIORI import calcular_potencia_priori

class PRIORI_TAB:
    def __init__(self, app, notebook):
        self.app      = app
        self.notebook = notebook

        self.tab      = ttk.Frame(notebook, padding=10)
        self.notebook.add(self.tab, text="Potencia Priori")

        self.tab.columnconfigure(0, weight=1)
        
        self.result = tk.StringVar()
        self.crear_tab()
    
    def crear_tab(self):
        #Campos para d de cohen
        ttk.Label(self.tab, text="D de cohen:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.d_cohen = ttk.Entry(self.tab, justify='center', textvariable=self.app.state.cohen)
        self.d_cohen.grid(row=0, column=1, sticky="w")

        #Campos para error alpha
        ttk.Label(self.tab, text="Error alpha (0.05):").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.error_alpha = ttk.Entry(self.tab, justify='center')
        self.error_alpha.insert(0, 0.05)
        self.error_alpha.grid(row=1, column=1, sticky="w")

        #Campos para potencia
        ttk.Label(self.tab, text="Potencia (0.8):").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.potencia = ttk.Entry(self.tab, justify='center')
        self.potencia.insert(0, 0.8)
        self.potencia.grid(row=2, column=1, sticky="w")

        #Campos para potencia
        ttk.Label(self.tab, text="Ratio (n2 : n1):").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.ratio = ttk.Entry(self.tab, justify='center')
        self.ratio.insert(0, 1)
        self.ratio.grid(row=3, column=1, sticky="w")

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
        r = calcular_potencia_priori(self.d_cohen.get(), 
                                     self.error_alpha.get(), 
                                     self.potencia.get(),
                                     self.ratio.get()
                                     )

        self.result.set(r)