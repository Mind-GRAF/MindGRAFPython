import random

from act import act
from agenda import agenda
from controlaction import controlAction


class DoOne (controlAction):
    def __init__(self) -> None:
      super().__init__()
    
    def __init__(self, identity):
        super().__init__(identity)  
      
        
    def perform (act):
        acts = []
        acts.append(act.getDownCableSet().getDownCable("do").getNodeSet())
        next_act = random.choice(acts)
        act.stage = agenda.start
        actStack.push(next_act)
           