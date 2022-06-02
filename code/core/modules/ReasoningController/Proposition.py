from concurrent.futures import process
from Channel import Channel
from ChannelSet import ChannelSet
from ReasoningController import ReasoningController
from Runner import Runner


import ChannelSet
import supportSet
class Proposition():
    global outgoingChannels
    outgoingChannels = ChannelSet
    global incomingChannels
    incomingChannels = ChannelSet
    global supports
    supports = supportSet


    def __init__(self):
        pass

    def processReports():
        for x in incomingChannels:
            ReasoningController.ProcessReportChannel(x)
            
    def recieveReport(channel):
        Runner.addToHighQ(channel)
            

    #Attributes class (supportSet, channelSet)