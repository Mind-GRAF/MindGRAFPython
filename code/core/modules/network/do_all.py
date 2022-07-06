from pickle import FALSE, TRUE
from pydoc import resolve
from random import Random, randint
import random

from agenda import agenda
from controlaction import controlaction


class do_all (controlaction):
    def __init__(self) -> None:
        super().__init__()
    def __init__(self, identity):
        super().__init__(identity)    
   
            
    
    def perform (act): #this should take an act
        #acts should be a node set but NodeSet class is not finished so i can not use it
        acts = []
        acts.append(act.Cable.getDownCableset().getDowncable("do").getNodeSet())
        while not len(acts) is 0:
            
            next_act = random.choice(acts)
            act.stage = agenda.start
            Runner.addToActQ(next_act)
            acts.remove(next_act)
            
            
        
   
        
        
               


   
   
                