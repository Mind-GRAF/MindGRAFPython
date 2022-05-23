from array import array
from pydoc import _OldStyleClass
from re import X
from tracemalloc import start
from agenda import agenda
from controlaction import controlAction
from realtion import relation


class Achieve (controlAction):
    def __init__(self) -> None:
        super().__init__()
    
    def perform(act):
        if act.stage is agenda.start:
            act.start(act)
        elif act.stage is agenda.find_plan:
            act.find_plan(act)
        else:
            return    
            
            
    def start(act):
        prop_node = act.getdownCableset.getdowncable("obj").getnodeset.getNode(0)
        context =act.getcurrentcontext()
        asserted = context.isasserted(prop_node)
        if(asserted):
            return
        else:
            act.stage = agenda.find_plan
            act_stack.push(act)
            r1 = relation.plan
            r2 = relation.goal
            wire = []
            wire.append(add_wire(r1,x))
            wire.append(add_wire(r2,x))
            #build new moleculer node with this new wire
            #added it to new node set called planGaols
    def find_plan(act):
        plans = []
        plans.append(act.process_reports)
        if plans:
            act.stage  = agenda.done
            wire = []
            r1 = relation.do
            r2 = relation.action
            for i in len(plans):
                wire.append(new_wire(r1,plan[i]))
            
            #build new action node here then the following
            
            wire.append(new_wire(r2,"new_action_node"))
            #build new moleculer node with the wire
            new_actnode= agenda.start
            actstack.push(new_actnode)
        
        else:
            return "plans are in planning algorithm" 
           
                
            
        
                
            
         
                
            
            