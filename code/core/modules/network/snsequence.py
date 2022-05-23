


from act import act
from agenda import agenda
from controlaction import controlAction


class SNSequence (controlAction):
    def __init__(self) -> None:
        super().__init__()
        
    
    def perform  (act):
        acts = act.getDownCableSet().getDownCable("obj").getNodeSet()
        while not acts.isEmpty():
            next_act = acts.getNode(acts.size()-1)
            act.stage = agenda.start
            actStack.push(next_act)
            acts.remove_node(next_act)
            
            
        