from tkinter import ttk

from Tabs.VDCONV_tab  import VDCONV_TAB
from Tabs.IC95_tab    import IC95_TAB
from Tabs.DEC_tab     import DEC_TAB
from Tabs.COHEN_tab   import COHEN_TAB
from Tabs.PRIORI_tab  import PRIORI_TAB
from Tabs.MEANDIF_tab import MEANDIF_TAB
from States           import States

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("402x350")
        self.root.resizable(False, False)

        self.state = States()
        
        self.crear_notebook()
        self.crear_tabs()
        self.crear_styles()
        

    def crear_notebook(self):
        self.notebook = ttk.Notebook()
        self.notebook.pack(fill="both", expand=True)


    def crear_tabs(self):
        self.VDCONV_tab  = VDCONV_TAB(self, self.notebook)
        self.IC95_tab    = IC95_TAB(self, self.notebook)
        self.DEC_tab     = DEC_TAB(self, self.notebook)
        self.COHEN_tab   = COHEN_TAB(self, self.notebook)
        self.PRIORI_tab  = PRIORI_TAB(self, self.notebook)
        self.MEANDIF_tab = MEANDIF_TAB(self, self.notebook)
    
    
    def crear_styles(self):
        style = ttk.Style()

        style.theme_use("clam")
        style.configure(
            "TNotebook.Tab",
            padding=(5, 5),
        )
        style.map(
            "TNotebook.Tab",
            foreground=[
                ("selected", "#FF0000"),
                ("!selected", "#000000")
                ]
        )