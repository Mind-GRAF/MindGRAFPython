import random

from act import act
from agenda import agenda
from controlaction import controlAction

#to run this class we will remove anything comes from outside to make sure the function works
class DoOne (): #subclass of control action
    def __init__(self) -> None:
      super().__init__()
    
    def __init__(self, identity):
        super().__init__(identity)  
      
        
    def perform (): # take an act
        acts = ["one","two","three","four","five"]
        #acts = []
        #acts.append("act.getDownCableSet().getDownCable("do").getNodeSet()")
        next_act = random.choice(acts)
        #act.stage = agenda.start
        #Runner.addtoactqueuen(next_act)
        print(next_act)
    
    
    perform()
    
    
    
    
    
    
       
           