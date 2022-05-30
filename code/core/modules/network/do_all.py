from pickle import FALSE, TRUE
from pydoc import resolve
from random import Random, randint
import random
#from Runner import Runner
from agenda import agenda
#from act import act
#from controlaction import controlAction


class do_all ():#this should be a sub class of control action
    def __init__(self) -> None:
        super().__init__()
    def __init__(self, identity):
        super().__init__(identity)    
   
            
    
    def perform (): #this should take an act
        acts = ["one","two","three","four","five"]
    

        while not len(acts) is 0:
            
            #acts.append(#act.getDownCableSet().getDownCable("do").getNodeSet())
            next_act = random.choice(acts)
            #act.stage = agenda.start
            #Runner.addToActQ(next_act)
            print(next_act)
            acts.remove(next_act)
            
            
        
    perform()    
        
        
               


   
   
                