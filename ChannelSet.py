from Channel import Channel
from Filter import Filter
from Switch import Switch
from Node import Node
import ChannelType
class ChannelSet(Channel):
   
    def __init__(channel: Channel,id,filter: Filter ,switch: Switch,source: Node ,destination: Node,status: bool,type):
        global channels
        super().__init__(id,filter,switch,source,destination,status,type)
        MatchedChannels = {
            'Matched' : channel
        } 
        AntToRuleChannels = {
            'AntToRule' : channel
        }  
        RuletoConsChannels = {
            'RuleToCons' : channel
        } 

    def addChannel(channel: Channel):
        channelSourceId = channel.source.id
        channelDestinationId= channel.destination.id
        filtersubs = channel.filter.substitutions
        switchsubs = channel.channel.substitutions
        channelType = channel.getChannelType(channel)
        
    def removeChannel(channel: Channel):
        channelSourceId = channel.source.id
        channelDestinationId= channel.destination.id
        filtersubs = channel.filter.substitutions
        switchsubs = channel.channel.substitutions
        channelType = channel.getChannelType(channel)

    def getChannelType(channel: Channel):
        channeltype =''
        if (ChannelType.RULEANT):
            channeltype = 'AntecedentToRule Channel'
        if (ChannelType.RULECONS):
            channeltype = 'RuleToConsequent Channel'
        else:
            channeltype = 'Matched Channel'
        return channeltype
#x=ChannelSet(0,0,0,0,0,0,0)
#print(x.getChannelType())