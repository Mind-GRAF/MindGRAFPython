from multiprocessing import context
import re
from urllib import request
from Filter import Filter
from Proposition import Proposition
from ReportSet import ReportSet
from Switch import Switch
import ChannelType

class Channel:
    global count
    count = 0
    global filter
    filter = Filter()
    global switch
    switch = Switch()
    global reportBuffer
    reportBuffer = ReportSet()

    def __init__ (channel,id,source,destination,status,type,context):
        channel.id = count
        channel.source = source
        channel.destination = destination
        channel.status = status
        channel.type = type
        channel.context = context
    count +1
    
    def reportToSend(self,report):
        canPass = filter.canPass(report)
        if canPass: # and isAsserted(report)
            Switch.switchReport(report)
            requester = self.getSource()
            Proposition.recieveReport(self)
            self.getReportsBuffer().addReport(report)

    def getId(channel):
        return channel.id

    def setSubstitution(channel,substitution):
        channel.substitution = substitution

    def getSupport(channel):
        return channel.support

    def getFilter(channel):
        return channel.filter
        
    def getType(channel):
        return channel.type

    def setFilter(channel,filter):
        channel.filter = filter

    def getDestination(channel):
        return channel.destination

    def setDestination(channel,destination):
        channel.destination = destination

    def getSource(channel):
        return channel.source

    def setSource(channel,source):
        channel.source = source

    def setReportsBuffer(self,reportsBuffer):
        self.reportsBuffer = reportBuffer

    def getReportsBuffer():
        return reportBuffer

    def clearReportsBuffer(self,reportsBuffer):
        self.getReportsBuffer().clearReports()

    def getContext(channel):
        return channel.context