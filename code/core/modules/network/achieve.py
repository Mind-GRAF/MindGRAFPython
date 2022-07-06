from array import array

from agenda import agenda
from controlaction import controlAction



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
        prop_node = act.Cable().getdownCableset.getdowncable("obj").getnodeset.getNode(0)
        context =act.get_context()
        plans_goal=[]
        asserted = context.isSupported(prop_node)
        if(asserted):
            return
        else:
            act.stage = agenda.find_plan
            Runner.addToActQ(act)
            r1 = relation.plan
            r2 = relation.goal
            wire = []
            wire.append(add_wire(r1,x))
            wire.append(add_wire(r2,x))
            plan_goal =node().add_moleculer_node(wire,act)
            plans_goal.append(plan_goal)
            #acttopropchannel = channel().addChannel(act,plan_goal,True)
            #plan_goal.Node().receive_request(acttopropchannel)
            #act.getplansChannel().addChannel(acttoprop)
            
            
            
            
    def find_plan(act):
        plans = []
        plans.append(ReasonController.BackwardChain(act,Controller().getCurrentContext(),"ACT"))
        if plans:
            act.stage  = agenda.done
            wire = []
            r1 = relation.do
            r2 = relation.action
            for i in len(plans):
                wire.append(new_wire(r1,plan[i]))
            
            
            action_node = Node().add_new_node("oneplan","do one")
            wire.append(new_wire(r2,action_node))
            node().add_moleculer_node(wire,action_node)
            
            new_actnode= agenda.start
            Runner.addToActQ(new_actnode)
        
        else:
            return "plans are in planning algorithm" 
           
                
            
        
                
            
         
                
            
            