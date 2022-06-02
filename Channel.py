from multiprocessing import context
import re
from urllib import request
from Filter import Filter
from Proposition import Proposition
from ReportSet import ReportSet
from Switch import Switch
import ChannelType
from Substitutions import Substitutions
from Node import Node
from Context import Context
from Report import Report

class Channel:
    global count
    count = 0
    global filter
    filter: Filter
    global switch
    switch: Switch
    global reportBuffer
    reportBuffer: ReportSet

    def __init__ (self,id,source: Node,destination: Node,status: bool ,type: str ,context: Context):
        self.id = count
        self.source = source
        self.destination = destination
        self.status = status
        self.type = type
        self.context = context
    count +1
    
    def reportToSend(self,report: Report):
        canPass = filter.canPass(report)
        if canPass: # and isSupported(report)
            Switch.switchReport(report)
            requester = self.getSource()
            Proposition.recieveReport(self)
            self.getReportsBuffer().addReport(report)
            return True
        
        return False


    def getId(self):
        return self.id

    def setSubstitution(self,substitution: Substitutions):
        self.substitution = substitution

    def getSupport(self):
        return self.support

    def getFilter(self):
        return self.filter
        
    def getType(self):
        return self.type

    def setFilter(self,filter: Filter):
        self.filter = filter

    def getDestination(self):
        return self.destination

    def setDestination(self,destination: Node):
        self.destination = destination

    def getSource(self):
        return self.source

    def setSource(self,source: Node):
        self.source = source

    def setReportsBuffer(self,reportsBuffer: ReportSet):
        self.reportsBuffer = reportBuffer

    def getReportsBuffer():
        return reportBuffer

    def clearReportsBuffer(self,reportsBuffer: ReportSet):
        self.getReportsBuffer().clearReports()

    def getContext(self):
        return self.context