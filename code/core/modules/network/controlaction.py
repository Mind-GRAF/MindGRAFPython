
from operator import truediv
from act import act


class controlAction (act):
    def __init__(self) -> None:
        super().__init__()
        set_primitive(True)
        
    
    def __init__(self,identity):
        super().__init__(identity)
        set_primitive(True)    
        