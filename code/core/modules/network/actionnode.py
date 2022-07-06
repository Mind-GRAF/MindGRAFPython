
from node import node,abstractmethod
class  actionnode(node):
    def __init__(self,primitve):
        self._primitive = primitve
        
    
    def __init__(self,identity):
        super().__init__(identity)
    
    @abstractmethod
    def perform (act):
        pass        
    
    def get_primitive(self):
        return self._primitive
    def set_primitive(self,x):
        self._primitive=x
    
    
        