
from act import act
from agenda import agenda
from controlaction import controlaction


class withsome(controlaction):
    def __init__(self) -> None:
        super().__init__()
        
    def __init__(self, identity):
        super().__init__(identity)
        
        
    
    def perform (act):
        if act.stage == agenda.start:
            act.start
        elif act.stage == agenda.identify_objects:
            act.itentifyObjects
        else:
            return    
            
    
    
    def start(act):
        act.stage = agenda.identify_objects
        Runner.addtoactQ (act)
        node = act.cable.getDownCableSet().getDownCable("like as").getNodeSet().getNode(0)
        acttopropchannel = acttopropchannel.addchannel(Controller().getcurrentconttext,act,node,True)
        node.recieverequest(acttopropchannel)
        act.addChannel(acttopropchannel)
        
    
    def itentifyObjects (act):
         constants = act.controller.processReports()
         act.stage= agenda.done
         wire = []
         r1 = relaton.action
         r2 = relation.doo
		 
   
   

            
        
        