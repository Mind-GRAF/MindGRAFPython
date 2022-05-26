from Report import report
class Filter:

    def __init__(filter: Filter,report: Report):
        filter.report = report
    
    def canPass(report: Report,attitude: Node):
        for i in self.substitution.cardinality():
            currentFilterBinding: Bindings  
            currentFilterBinding = substitution.getBinding(i)
            currentReportBinding: Bindings  
            currentReportBinding = report.getSubstitutions().getBindingByVariable(currentFilterBinding.getVariable())
            System.out.println("Bindings " + currentFilterBinding + " " + report.getSubstitutions())
                if currentReportBinding is not None and currentFilterBinding.getNode() is not currentReportBinding.getNode() and report.attitude is not attitude :
                    return false
            
		return true
#x = Filter(1)
#print(x.canPass())

