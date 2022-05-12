from Report import report
from ReportSet import reportSet
from Substitutions import Substitutions
from Substitutions import Substitutions
class KnownInstances(report):
    global knowninstances
    knowninstances = {
            'Substitutions' : reportSet
    }

    def __init__(knowninstances,substitution, support,source,destination):
        super.__init__(substitution, support,source,destination)
     

    def addReport(report):
        reportSubs = Substitutions
        reportSubs = report
        report.getSubstitution()
        reportSet = knowninstances.pop(reportSubs)
        if reportSet == None: 
            reportSet = []
        reportSet.append(report)
        knowninstances.update(reportSubs,reportSet)


    def getReportBySubs(Subs):
        return knowninstances.get('Substitutions')
    
    def getSubstitution(report):
        pass
