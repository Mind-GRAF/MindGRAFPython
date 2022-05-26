from Substitutions import Substitutions
class Report:
    def __init__(report: Report,substitution: Substitutions,support: supportSet,inference: str,source: Node,
    destination: Node,attitude: Node):
        report.substitution = substitution
        report.support = support
        report.inference = inference
        report.destination = destination
        report.source = source
        report.attitude = attitude

    def getSubstitution(report: Report):
        return report.substitution

    def setSubstitution(report: Report,substitution: Substitutions):
        report.substitution = substitution

    def getSupport(report: Report):
        return report.support

    def getInference(report): Report:
        return report.inference

    def setInference(report: Report,inference: str):
        report.inference = inference

    def getDestination(report: Report):
        return report.destination

    def setDestination(report: Report,destination: Node):
        report.destination = destination

    def getSource(report: Report):
        return report.source

    def setSource(report: Report,source: Node):
        report.source = source

#report = Report(15,5,5,5,5)
#print(report.getSubstitution())