from Bindings import Bindings
from Report import Report
from Substitutions import Substitutions
class Switch():
    def __init__(self,substitutions: Substitutions):
        self.substitutions = substitutions 
    
    def switchReport(self,report: Report):
        subs = self.substitutions.cardinality()
        for x in range(subs):
            bindings: Bindings
            bindings = report.getSubstitution().getBinding()
            if(bindings is not None):
                bindings.setVariable()
            else:
                report.getSubstitution()
    	
#x=Switch(1)
#print(x.switchReport())