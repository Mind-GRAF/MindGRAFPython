#from path to proposition
class PropositionSet(Proposition):
        def __init__(self, id):
            self.id   = id
            
     
    #creating list 
    
        propSet = []
        
    
    #appending instances of class proposition to this proposition set     
        def addToPropSet(Proposition p):
            propSet.append(p.id)
        
        def isEmpty():
            if len(propSet)==0:
                print('the proposition set is empty')
                
        def remove(prop):
            propSet.remove(p)
        
            