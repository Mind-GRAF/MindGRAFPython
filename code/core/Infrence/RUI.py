from RUI_Controller import RUI_Controller

class RUI(RUI_Controller):
    Subs =list
    Pcount=int
    Ncount=int
    Fns=bool
    InfType=str

    def __init__(self):
        self.Subs=[]
        self.Pcount=0
        self.Ncount=0
        self.Fns=True
        self.InfType=""
        super().__init__('RUI')
