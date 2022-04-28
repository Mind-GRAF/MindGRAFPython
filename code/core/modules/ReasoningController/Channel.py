import Filter
import Switch
import ChannelType

class Channel:
    global count
    count = 0
    
    def __init__ (channel,id,filter,switch,source,destination,status,type):
        channel.id = count
        channel.filter = filter
        channel.switch = switch
        channel.source = source
        channel.destination = destination
        channel.status = status
        channel.type = type
    
    count +1
    

    def getId(channel):
        return channel.id

    def setSubstitution(channel,substitution):
        channel.substitution = substitution

    def getSupport(channel):
        return channel.support

    def getFilter(channel):
        return channel.filter

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
