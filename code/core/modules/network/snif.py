
import array
from  act import  act
from agenda import agenda
from controlaction import controlAction
from realtion import relation


class snif( controlAction,act):
    
    
    def __init__(self) -> None:
        super().__init__()
        
        
    def __init__(self, identity):
        super().__init__(identity)
        
            
        
    
    def perform(act):
        if act.stage is agenda .start:
            act.start()
        elif act.stage is agenda.test_precondition:
            act.test()
        else:
            return    
            
            
    
    def start(act):
        act.stage = agenda.test_precondition
        actStack.push(act)
        guards = []
        for n in act.getDownCableSet().getDownCable("obj").getNodeSet():
            guards.append(n.getDowncableset().getdowncable("guard").getNOdeset())
             
        for guard in guards:
            # should be actToPropchannel with currentcontext with requester "ACT" and reporter (guard)
            ##and this instance guard recieve request from this acttoprop channnel
            # asserting proconditions with this new channel
             
         return      
        
        
        
    def test(act):
        possible_acts = []
        all_guard_act = []
        satisfied_guard = []
        satisfied_guard.append(act.process_reports())
        act.stage = agenda.done
        all_guard_act = act.getDownCableSet().getDownCable("obj").getNodeSet()
        
        for guard_act in all_guard_act:
            contain_all = True
            for n in guard_act.getDownCableSet().getDownCable("guard").getNodeSet():
                if (not satisfied_guard.__contains__(n)):
                    contain_all = False
            
            if  contain_all:
                possible_acts.append(guard_act.getDownCableSet().getDownCable("act").getNodeSet().getNOde(0))
        
        wire =[]
        r1 = relation.do
        r2 = relation.action
        for i in len(possible_acts):
            wire.append(add_new_wire(r1,possible_acts[i]))
        
        wire.append(add_new_wire(r2,#new node called action node
                                 ))
        #then build new moleculer node (will not cooded yet) 
        #restart the agenda of this mo;eculer node (act node)
        #added to the act stack  
        
                                    
             
                                      
            
        
        
        
        
            
            
        
        
        
    
    
    