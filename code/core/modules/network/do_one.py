import random

from act import act
from agenda import agenda
from controlaction import controlaction

#to run this class we will remove anything comes from outside to make sure the function works
class DoOne (controlaction): #subclass of control action
    def __init__(self) -> None:
      super().__init__()
    
    def __init__(self, identity):
        super().__init__(identity)  
      
        
    def perform (act): # take an act
        
        acts = []
        acts.append(act.cable.getDownCableSet().getDownCable("do").getNodeSet())
        next_act = random.choice(acts)
        act.stage = agenda.start
        Runner.addtoActQ(next_act)
        
    
    
    
    
    
    
    
    
       
           