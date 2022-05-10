class ContextController(Context):
      
      def __init__(self, contextSet, attitudeSet, id):
        super().__init__(self, contextSet, attitudeSet)
        
        
      
      setOfAttitudes = ["Beliefs", "Desires", "Intentions", ]
      
      setOfContexts = []
     
     
def removeContext(Context c): 
  setOfContexts.remove(c.id)
    

#helper method to get key

def get_key(val):
    for key, value in hyps.items():
         if val == value:
             return key
 
    return "key doesn't exist"


def checkContext(Proposition p): 
  
  keys = hyps.keys()
  values = hyps.values()
  if p in values: 
    get_key(p)
  
  
  
  
  