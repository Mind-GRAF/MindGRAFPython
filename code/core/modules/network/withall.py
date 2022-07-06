from act import act
from actionnode import actionnode
from agenda import agenda
from controlaction import controlaction


class withall(controlaction):
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
         doNode = act.cable.getDowncableset().getDownCable("do").getNodeSet().getNode(0)
         actionNode=doNode.cable.getDowncableset().getDownCable("action").getNodeSet().getNode(0)
         possible_acts = []
         wireaction = []
         wireaction.append({r2,actionNode})
         i =0
         while i < len(constants):
             wireslist = []
             wireslist.append({r1,constants.get(i)})
             wireslist.append(wireaction)
             #build new moleculer act  node from wire List
             possible_acts.append("this new moleculer node")
             i = i+1
             
         
         arrayDoAll = []
         y=0
         while y < len(possible_acts):
             arrayDoAll.append({r2,possible_acts.pop})
             y=y+1
         
         #build an action node 
         #add to arrayDoOne this new action node with relation r1
         #build new moleculer node 
         #restart agenda for this new moleculer node the add it to act stack       
             
		 
   
   

            
        
        