from Reportset import ReportSet
from act import act
from Reportset import ReportSet
from actionnode import actionnode

class disbelieve(actionnode):
    def __init__(self) -> None:
        super().__init__()
    
    def __init__(self,identity):
        super().__init__(identity)
        actionnode.set_primitive(True)    
    
    
    
    def perform(act):
        p = act.cable.getDownCableSet().getDownCable("obj").getNodeSet().getNode(0) 
        ContextController.removepropfromcontext(p)
        