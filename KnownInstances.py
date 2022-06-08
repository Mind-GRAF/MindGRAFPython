from Report import Report
from ReportSet import reportSet
from Substitutions import Substitutions
from Substitutions import Substitutions
from supportSet import supportSet
from Node import Node


class KnownInstances(Report):
    global knowninstances
    knowninstances = {
            'Substitutions' : reportSet
    }

    def __init__(self,substitution: Substitutions, support: supportSet ,source: Node ,destination: Node,attitude: str):
        super.__init__(substitution, support,source,destination,attitude)
     

    def addReport(self,report: Report):
        reportSubs: Substitutions
        reportSubs = report
        report.getSubstitution()
        reportSet = self.pop(reportSubs)
        if reportSet == None: 
            reportSet = []
        reportSet.append(report)
        self.update(reportSubs,reportSet)


    def getReportBySubs(self):
        return self.getSubstitution()
    
    def getSubstitution(self,report: Report):
        pass
