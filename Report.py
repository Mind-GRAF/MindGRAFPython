from Substitutions import Substitutions
from supportSet import supportSet
from Node import Node
from Report import Report
class Report:
    def __init__(self,substitution: Substitutions,support: supportSet,inference: str,source: Node,
    destination: Node,attitude: str):
        self.substitution = substitution
        self.support = support
        self.inference = inference
        self.destination = destination
        self.source = source
        self.attitude = attitude

    def getSubstitution(self):
        return self.substitution

    def setSubstitution(self,substitution: Substitutions):
        self.substitution = substitution

    def getSupport(self):
        return self.support

    def getInference(self): 
        return self.inference

    def setInference(self,inference: str):
        self.inference = inference

    def getDestination(self):
        return self.destination

    def setDestination(self,destination: Node):
        self.destination = destination

    def getSource(self):
        return self.source

    def setSource(self,source: Node):
        self.source = source

    def computeReportFromDifferencesToSend(self,report: Report):
        instanceInfType = self.getInferenceType()
        reportInfType = report.getInferenceType()
        instanceSupport = self.getSupport()
        reportSupport = report.getSupport()
        supportCheck = instanceSupport is reportSupport
        if(instanceInfType == "BACKWARD" and reportInfType == "FORWARD"):
            return report
        elif(not supportCheck):
            if(instanceInfType == "FORWARD" and reportInfType == "BACKWARD"):
                report.setInferenceType("FORWARD")
            return report
        return None

#report = Report(15,5,5,5,5)
#print(report.getSubstitution())