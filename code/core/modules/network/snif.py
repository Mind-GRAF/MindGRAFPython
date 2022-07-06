
import array
from tracemalloc import stop
from agenda import agenda

from controlaction import controlaction


class snif(controlaction):# controlAction,act
    
    
    def __init__(self) -> None:
        super().__init__()
        
        
    def __init__(self, identity):
        super().__init__(identity)
    
    def perform(act):
        guards =[]
        if act.stage == agenda.start:
            act.start()
        elif act.stage == agenda.test_precondition:
            act.test()
        else:
            return        
           
    def start(act):
        guards = []
        act.stage = agenda.test_precondition
        Runner.addtoActQ(act)
       
        for n in act.Cable().getDownCableSet().getDownCable("obj").getNodeSet():
            guards.append(n.Cable().getDowncableset().getdowncable("guard").getNOdeset())
            break
        
        for guard in guards:
            #acttopropchannel = Channel().add_new_channel(Controller().getcurrentcontext(),act,guard,True)
            #guard.Node().recieverequest(acttopropchannel)
            #act.Channel().getassertingpreconditionChannel().addChannel(acttopropChannel)
            break    
        
    def test(act):
        possible_acts = []
        satisfied_guards = []
        satisfied_guards.append(Controller().backword_chaining(act))
        act.stage = agenda.done
        all_guard_acts = Cable(act).getDownCableSet().getDownCable("obj").getNodeSet()
        for guard_act in all_guard_acts:
            contain_all = True
            for n in guard_act.getDownCableSet().getDownCable("guard").getNodeSet():
                if (not satisfied_guards.__contains__(n)):
                    contain_all = False
            
            if  contain_all:
                possible_acts.append(guard_act.getDownCableSet().getDownCable("act").getNodeSet().getNOde(0))
                
                
        
      
        wire =[]

        r1 = relation.do
        r2 = relation.action
        i=0
        
        while (i < len(possible_acts)):
            wire.append({r1,possible_acts[i]})
            i=i+1
            
        doaction = node().build_new_node("doone","doone")
        
        wire.append({r2,doaction}) #add a new node called action node
        doOne = Node().add_new_moleculer_node(wire,act)
        doOne.stage = agenda.start
        Runner.addtoActQ(doOne)
       
    
   
    #these comments should change to code lines when their implementation is complete        
            
        
        
        
    
    
                                                                                    