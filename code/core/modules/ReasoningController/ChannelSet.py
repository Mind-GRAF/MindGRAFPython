from Channel import Channel
import ChannelType
class ChannelSet(Channel):
   
    def __init__(channel,id,filter,switch,source,destination,status,type):
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

    def addChannel(channel):
        channelSourceId = channel.source.id
        channelDestinationId= channel.destination.id
        filtersubs = channel.filter.substitutions
        switchsubs = channel.channel.substitutions
        channelType = channel.getChannelType(channel)
        
    def removeChannel(channel):
        channelSourceId = channel.source.id
        channelDestinationId= channel.destination.id
        filtersubs = channel.filter.substitutions
        switchsubs = channel.channel.substitutions
        channelType = channel.getChannelType(channel)

    def getChannelType(channel):
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