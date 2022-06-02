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
from Context import Context
from MindGRAFController import MindGRAFController
class ReasoningController:
    global knownInstances= KnownInstances()
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
    def Request (self,source: Node,destination: Node,status: bool,type,context: Context):
        request = Channel(source,destination,status,type,context)
        Runner.addToLowQ(request)
    def SendReport(self,report: Report,channel: Channel):
        if channel.reportToSend(report):
            print("Report:", report , "was sent from" , channel.getSource(), "to", channel.getDestination )
        else:
            print("Report:", report , "could not be sent from" , channel.getSource(), "to", channel.getDestination )
        channel.clearReportsBuffer()

    def AddToKnownInstances(self,channel: Channel,report: Report):
        knownInstances.addReport(report)

    def ForwardChain(self,node: Node, context: Context, attitude: str):
        Runner.run()
        contextName = MindGRAFController.getContext()
        self.getNodesToSendReport(ChannelType.RULEANT, contextName, None, "FORWARD" ,None,None)
        self.getNodesToSendReport(ChannelType.MATCHED, contextName, None, "FORWARD" ,None,None)
        #CheckContradiction("Built node: Node") after building
        return "nodeSet"
    def BackwardChain(self, node: Node, context: Context, attitude: str):
        Runner.run()
        contextName = MindGRAFController.getContext()
        self.getNodesToSendReport(ChannelType.RULEANT, contextName, None, "BACKWARD" ,None,None)
        self.getNodesToSendReport(ChannelType.MATCHED, contextName, None, "BACKWARD" ,None,None)
        return "nodeSet"
    def ProcessReportsChannel(self, channel: Channel):
        reports: Report
        reports = [channel.getReportsBuffer]        
        currReport: Report
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
    def processRequestsChannel(self, channel: Channel):
        str currentContextName = channel.getContext()
        desiredContext: Context
        desiredContext = currentContextName
        attitude = desiredContext.getAttitude()
        if(isSupported(desiredContext)):
            int propNodeId = getId()
            supportPropSet = PropositionSet()
            supportPropSet = supportPropSet.add(propNodeId)
            reply = Report("subs".supportPropSet,"BACKWARD",None,None,attitude)
            self.sendReport(reply,channel)
        else
            bool sentAtLeastOne = false
            currentReport: Report
            for(currentReport : knownInstances):
                sentAtLeastOne |= sendReport(currentReport, channel)
            filterSubs = channel.getFilter().getSubstitutions()
            if(not sentAtLeastOne):
                dominatingRules: NodeSet
                dominatingRules=getUpConsNodeSet()
                toBeSentToDom: NodeSet
                toBeSentToDom = self.removeAlreadyWorkingOn(dominatingRules,channel,filterSubs,false)
                self.sendRequestsToNodeSet(toBeSentToDom,filterSubs,currentContextName,ChannelTypes.RULEANT)
                if(not(isinstance(currentChannel,MatchChannel)):
                    matchingNodes: Matcher 
                    matchingNodes.match(this,filterSubs)
                    toBeSentToMatch: Matcher
                    toBeSentToMatch = self.removeAlreadyWorkingOn(matchingNodes,channel)
                    self.sendRequestsToMatches(toBeSentToMatch,currentContextName)



    def getNodesToSendReport(self,type, context: Context, substitutions: Substitutions, inferenceType: str ,source: Node,destination: Node):
        suppSet = supportSet()
        suppSet.add(suppSet.getId())
        report = Report(substitutions,suppSet,inferenceType,source,destination)
        match type:
            case 'MATCHED': 
                matches = [Matcher.Match]
                if matches: 
                    self.sendReportToMatches(matches,report,context)
            case 'RULEANT':
                if isinstance(self,RuleNode):
                    antNodes = NodeSet.getDownAnt()
                    self.sendReportToNodeSet(antNodes,report,context,type)

    
    def sendReportToMatches(self,matched: Matcher,report: Report,context: Context):
        for currentMatch in matched:
            reportSubs= Substitutions
            reportSubs.getSubs()
            currentMatch = Matcher
            #matchType = currentMatch.getMatchType()
            newChannel = Channel(currentMatch,"destinaion","status",ChannelType.MATCHED,context)
            self.sendReport(report,newChannel)

    def sendReportToNodeSet(nself,nodeSet: NodeSet, report: Report, context: Context, type: str,source: Node, destination: Node):
        for sent in nodeSet:
            report = Report
            reportSubs = report.getSubstitution()
            newChannel = Channel(source,destination,type,"status",type,context)
            self.SendReport(report,newChannel)

    def isSupported(self,context: Context):
        pass
