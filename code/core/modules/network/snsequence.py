


#from act import act
#from agenda import agenda
#from controlaction import controlAction


class SNSequence ():#take a control action
    def __init__(self) -> None:
        super().__init__()
        
    def __init__(self, identity):
        super().__init__(identity)
     
            
        
    
    def perform  (): #take an act
        #acts = []
        acts = ["one","two","three","four","five"]
    
        #acts.append(act.getDownCableSet().getDownCable("obj").getNodeSet())
        while not len(acts) is 0:
            #next_act = acts.getNode(acts.size()-1)
            next_act = acts[len(acts)-1]
            #act.stage = agenda.start
            #actStack.push(next_act)
            #acts.remove_node(next_act)
            print(next_act)
            acts.remove(next_act)
            
            
    
    perform()    