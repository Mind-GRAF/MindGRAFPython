from Report import report
from ReportSet import reportSet

class KnownInstances(report):
    def __init__(knowninstances,substitution, support,source,destination):
        super.__init__(substitution, support,source,destination)
        knowninstances = {
            'Substitutions' : reportSet
        }
        
    def AddToKnownInstances(report):
        reportSubs = report.getSubstitution()