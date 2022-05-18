from RUISet import RUISet

class RUI(RUISet):
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

    def isVarsCompatible(self,r):
        return True
    
    def isDisjoint(self,r):
        return True
    def combine(self,r):
        return self+r
