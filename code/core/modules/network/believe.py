from act import act
from actionnode import actionnode


class believe (actionnode):
    def __init__(self) -> None:
        super().__init__()
        actionnode.set_primitive(True)
        
    def __init__(self,identity) -> None:
        super().__init__(identity)
        actionnode.set_primitive(True)
            
    def perform(act):
        prop_node =Cable(act).getDowncableset().getDownCable('obj').getnodeset().getnode(0)        			
        Context().addToContext(prop_node,"")
        
        support = []
        support.append(prop_node.get_basic_support())
        new_report = []
        new_report.append("new report of this support and get current context name ")
        prop_node.sent(new_report)
        

    
    
    
    
    