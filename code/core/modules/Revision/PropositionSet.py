#from path to proposition
class PropositionSet(Proposition):
        def __init__(self, id, name, propset):
            self.name   = name
            self.id   = id
            self.propSet = propSet
            
     
    #creating list 
    
        propSet = []
        
    
    #appending instances of class proposition to this proposition set     
        def addToPropSet(node):
            propSet.append(node.id)
        
        def isEmpty():
            if len(propSet)==0:
                return True
            else:
                return False
                
        def remove(node):
            self.propSet.remove(node.id)
        
            