from typing_extensions import Self
from Channel import Channel
from KnownInstances import KnownInstances
from Report import Report
from Channel import Channel
from ChannelSet import ChannelSet
from ReportSet import ReportSet
from Substitutions import Substitutions
from Proposition import Proposition
from PropositionSet import PropositionSet
from supportSet import supportSet
from Matcher import Matcher
from ChannelType import ChannelType
from RuleNode import RuleNode
from NodeSet import NodeSet
from Runner import Runner
from MindGRAFController import MindGRAFController
class ReasoningController:
    def ApplySubstitution ():
        pass
    def CheckCompatiableSubstitution ():
        pass
    
    """ 
    Receiving a request opens a new channel 
    
    Parameters: 
    source: node with the request
    destination: node to be sent the report to
    status: status of the channel open or closed
    type: inference type BackwardChain or ForwardChain

    """
    def Request (source: Node,destination: Node,status: bool,type,context: Context):
        request = Channel(source,destination,status,type,context)
    def SendReport(report: Report,channel: Channel):
        channel = Channel
        if channel.reportToSend(report):
            print("Report:", report , "was sent from" , channel.getSource(), "to", channel.getDestination )
        else:
            print("Report:", report , "could not be sent from" , channel.getSource(), "to", channel.getDestination )
        channel.clearReportsBuffer()

    def AddToKnownInstances(report: Report):
        instances = KnownInstances
        instances.addReport(report)

    def ForwardChain(node: Node, context: Context, attitude: Node):
        Runner.run()
        report = Report
        contextName = MindGRAFController.get
        ReasoningController.getNodesToSendReport(ChannelType.RULEANT, contextName, None, "FORWARD" ,report.getSource,report.getDestination)
        ReasoningController.getNodesToSendReport(ChannelType.MATCHED, contextName, None, "FORWARD" ,report.getSource,report.getDestination)
        return "nodeSet"
    def BackwardChain(node: Node, context: Context, attitude: Node):
        return "nodeSet"
    def ProcessReportChannel(channel: Channel):
        channel = Channel
        reports = Report
        reports = [channel.getReportsBuffer]        
        currReport = Report
        for currReport in reports:
            report = Report(currReport.getSubstitution,currReport.getSupport,currReport.getInference,currReport.getSource,currReport.getDestination)
            knownInstances = KnownInstances
            if report in knownInstances:
                continue
            outgoingChannels = KnownInstances
            for outChannel in outgoingChannels:
                outChannel = KnownInstances
                outChannel.addReport(report)
            channel.clearReportsBuffer
        channel.clearReportsBuffer


    def getNodesToSendReport(self,type, context: Context, substitutions: Substitutions, inferenceType,source: Node,destination: Node):
        suppSet = supportSet()
        suppSet.add(suppSet.getId())
        report = Report(substitutions,suppSet,inferenceType,source,destination)
        match type:
            case 'MATCHED': 
                matches = [Matcher.Match]
                if matches: 
                    ReasoningController.sendReportToMatches(matches,report,context)
            case 'RULEANT':
                if isinstance(self,RuleNode):
                    antNodes = NodeSet.getDownAnt()
                    ReasoningController.sendReportToNodeSet(antNodes,report,context,type)

    
    def sendReportToMatches(matched: Matcher,report: Report,context: Context):
        for currentMatch in matched:
            reportSubs= Substitutions
            reportSubs.getSubs()
            currentMatch = Matcher
            #matchType = currentMatch.getMatchType()
            newChannel = Channel(currentMatch,"destinaion","status",ChannelType.MATCHED,context)
            ReasoningController.sendReport(report,newChannel)

    def sendReportToNodeSet(nodeSet: NodeSet, report: Report, context: Context, type,source: Node, destination: Node):
        for sent in nodeSet:
            report = Report
            reportSubs = report.getSubstitution()
            newChannel = Channel(source,destination,type,"status",type,context)
            ReasoningController.SendReport(report,newChannel)

    def isAsserted(context: Context):
        pass
