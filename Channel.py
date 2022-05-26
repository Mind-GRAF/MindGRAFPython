from multiprocessing import context
import re
from urllib import request
from Filter import Filter
from Proposition import Proposition
from ReportSet import ReportSet
from Switch import Switch
import ChannelType
from Substitutions import Substitutions

class Channel:
    global count
    count = 0
    global filter
    filter: Filter
    global switch
    switch: Switch
    global reportBuffer
    reportBuffer: ReportSet

    def __init__ (channel,id,source: Node,destination: Node,status: bool ,type: String ,context: Context):
        channel.id = count
        channel.source = source
        channel.destination = destination
        channel.status = status
        channel.type = type
        channel.context = context
    count +1
    
    def reportToSend(self,report: Report):
        canPass = filter.canPass(report)
        if canPass: # and isAsserted(report)
            Switch.switchReport(report)
            requester = self.getSource()
            Proposition.recieveReport(self)
            self.getReportsBuffer().addReport(report)

    def getId(channel: Channel):
        return channel.id

    def setSubstitution(channel: Channel,substitution: Substitutions):
        channel.substitution = substitution

    def getSupport(channel: Channel):
        return channel.support

    def getFilter(channel: Channel):
        return channel.filter
        
    def getType(channel: Channel):
        return channel.type

    def setFilter(channel: Channel,filter: Filter):
        channel.filter = filter

    def getDestination(channel: Channel):
        return channel.destination

    def setDestination(channel: Channel,destination: Node):
        channel.destination = destination

    def getSource(channel: Channel):
        return channel.source

    def setSource(channel: Channel,source: Node):
        channel.source = source

    def setReportsBuffer(self,reportsBuffer: ReportSet):
        self.reportsBuffer = reportBuffer

    def getReportsBuffer():
        return reportBuffer

    def clearReportsBuffer(self,reportsBuffer: ReportSet):
        self.getReportsBuffer().clearReports()

    def getContext(channel: Channel):
        return channel.context