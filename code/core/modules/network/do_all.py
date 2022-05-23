from pickle import FALSE, TRUE
from pydoc import resolve
from random import Random, randint
import random
from agenda import agenda
from act import act
from controlaction import controlAction


class do_all (controlAction):
    def __init__(self) -> None:
        super().__init__()
    
    def perform (act):
        while not len(acts) is 0:
            acts = []
            acts.append(act.getDownCableSet().getDownCable("do").getNodeSet())
            next_act = acts.getNode(random.choice(acts))
            act.stage = agenda.start
            actStack.push(next_act)
            acts.remove(next_act)
            
            
        
        
        
        
               


   
   
                