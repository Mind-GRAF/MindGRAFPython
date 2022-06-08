from concurrent.futures import process
from Channel import Channel
from ChannelSet import ChannelSet
from ReasoningController import ReasoningController
from Runner import Runner


import ChannelSet
import supportSet
class Proposition(Entity):
    global outgoingChannels
    outgoingChannels: ChannelSet
    global incomingChannels
    incomingChannels: ChannelSet
    global supports
    supports: supportSet


    def __init__(self,outgoingChannels: ChannelSet,incomingChannels: ChannelSet,supports: supportSet):
        self.outgoingChannels = outgoingChannels
        self.incomingChannels = incomingChannels
        self.supports = supports
        

    def processReports():
        for x in incomingChannels:
            ReasoningController.ProcessReportChannel(x)
            
    def recieveReport(self,channel: Channel):
        Runner.addToHighQ(channel)
    
    def addToOutgoingChannels(self, channel: Channel):
        outgoingChannels.addChannel(channel)
    
    def addToIncomingChannels(self, channel: Channel):
        incomingChannels.addChannel(channel)
            

    #Attributes class (supportSet, channelSet)