class Report:
    def __init__(report,substitution, support,inference,source,destination):
        report.substitution = substitution
        report.support = support
        report.inference = inference
        report.destination = destination
        report.source = source

    def getSubstitution(report):
        return report.substitution

    def setSubstitution(report,substitution):
        report.substitution = substitution

    def getSupport(report):
        return report.support

    def getInference(report):
        return report.inference

    def setInference(report,inference):
        report.inference = inference

    def getDestination(report):
        return report.destination

    def setDestination(report,destination):
        report.destination = destination

    def getSource(report):
        return report.source

    def setSource(report,source):
        report.source = source

#report = Report(15,5,5,5,5)
#print(report.getSubstitution())