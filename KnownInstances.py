from Report import Report
from ReportSet import reportSet
from Substitutions import Substitutions
from Substitutions import Substitutions
class KnownInstances(Report):
    global knowninstances
    knowninstances = {
            'Substitutions' : reportSet
    }

    def __init__(knowninstances: KnownInstances ,substitution: Substitutions, support: supportSet ,source: Node ,destination: Node):
        super.__init__(substitution, support,source,destination)
     

    def addReport(report: Report):
        reportSubs: Substitutions
        reportSubs = report
        report.getSubstitution()
        reportSet = knowninstances.pop(reportSubs)
        if reportSet == None: 
            reportSet = []
        reportSet.append(report)
        knowninstances.update(reportSubs,reportSet)


    def getReportBySubs(Subs: Substitutions):
        return knowninstances.get('Substitutions')
    
    def getSubstitution(report: Report):
        pass
