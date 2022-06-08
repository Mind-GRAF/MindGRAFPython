from itertools import count
from lib2to3.pytree import Node
from queue import Empty
from Channel import Channel
from Proposition import Proposition


class Runner():

    global highQ
    highQ = []
    global lowQ
    lowQ = []
    global actQ
    actQ = []

    def run():
        while(highQ.count != 0 or lowQ.count != 0 or actQ.count != 0):  
            while(highQ.count != 0):
                print("In HighQ")
                runNext = highQ.pop(0)
                print(runNext)
                Proposition.processReports(runNext)

            while(lowQ.count != 0):
                print("In LowQ")
                runNext = lowQ.pop(0)
                print(runNext)
                runNext = Channel("Node.getSource","Node.getDest","Node.getType","Node.getCont")
                if highQ:
                    Runner.run() 
                                
            while(actQ.count != 0):
                print("In ActQ")
                runNext = actQ.pop()
                print(runNext)
                if highQ or lowQ:
                    Runner.run()
        
    def addToHighQ(node: Node):
        highQ.append(node)
    def addToLowQ(node: Node):
        lowQ.append(node)    
    def addToActQ(node: Node):
        actQ.append(node)