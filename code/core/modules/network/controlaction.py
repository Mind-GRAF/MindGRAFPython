from act import act
from actionnode import actionnode , abstractmethod


class controlaction (actionnode):
    def __init__(self) -> None:
        super().__init__()
        actionnode.set_primitive(True)
        
    
    def __init__(self,identity):
        super().__init__(identity)
        actionnode.set_primitive(True)    
        