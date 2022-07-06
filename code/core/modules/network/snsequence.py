


#from act import act
#from agenda import agenda
#from controlaction import controlAction


from controlaction import controlaction


class SNSequence (controlaction):#take a control action
    def __init__(self) -> None:
        super().__init__()
        
    def __init__(self, identity):
        super().__init__(identity)
     
            
        
    
    def perform  (act): #as Node set class in not finished we us lists but hashtags will work if we have node set class
        acts=[]
        acts.append(act.cable.getDownCableSet().getDownCable("obj").getNodeSet())
        while not len(acts) is 0:
            #next_act = acts.getNode(acts.size()-1)
            next_act = acts[len(acts)-1]
            act.stage = agenda.start
            Runner.addtoActQ(next_act)
            #acts.remove_node(next_act)
            
            acts.remove(next_act)    