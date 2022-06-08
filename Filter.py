from Report import Report
from Bindings import Bindings
from Substitutions import Substitutions
class Filter:

    def __init__(self,report: Report):
        self.report = report
    
    def canPass(self,report: Report,attitude: str):
        for x in self.substitution.cardinality():
            currentFilterBinding: Bindings  
            currentFilterBinding = Substitutions.getBinding(x)
            currentReportBinding: Bindings  
            currentReportBinding = report.getSubstitutions().getBindingByVariable(currentFilterBinding.getVariable())
            print("Bindings " + currentFilterBinding + " " + report.getSubstitutions())
            if (currentReportBinding is not None and currentFilterBinding.getNode() is not currentReportBinding.getNode() and report.attitude is not attitude) :
                    return False
        return True
#x = Filter(1)
#print(x.canPass())

