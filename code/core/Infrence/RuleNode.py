from platform import node
from typing import Type
from numerical_entailment import numerical_entailment
from or_entailment import or_entailment
from and_entailment import and_entailment
from andor import andor
from thresh import thresh
from PropositionNode import PropositionNode


class RuleNode(PropositionNode):
    name = str
    ant = list
    cq = list
    downCableS = list
    min = int
    max = int


def __init__(self, downCableS):
    self.downCableS = downCableS
    for i in len(downCableS):
        if downCableS(i).relation.getname() == "i":
            self.name = "numerical_entailment"
        elif downCableS(i).relation.getname() == "thresh":
            self.name = "thresh"
        elif downCableS(i).relation.getname() == "ant":
            self.name = "or"
        elif downCableS(i).relation.getname() == "max":
            self.name = "andor"
        else:
            self.name = "and"

    if self.name == "and":
        for i in len(self.downCableS):
            if downCableS(i).relation.getname() == "&ant":
                self.ant = downCableS(i).getnodeset()
            else:
                self.cq = downCableS(i).getnodeset()
    elif self.name == "or":
        for i in len(self.downCableS):
            if downCableS(i).relation.getname() == "ant":
                self.ant = downCableS(i).getnodeset()
            else:
                self.cq = downCableS(i).getnodeset()
    elif self.name == "numerical_entailment":
        for i in len(self.downCableS):
            if downCableS(i).relation.getname() == "&ant":
                self.ant = downCableS(i).getnodeset()
            elif downCableS(i).relation.getname() == "cq":
                self.cq = downCableS(i).getnodeset()
            else:
                self.min = downCableS(i).i
    elif self.name == "andor":
        for i in len(self.downCableS):
            if downCableS(i).relation.getname() == "arg":
                self.ant = downCableS(i).getnodeset()
                self.cq = downCableS(i).getnodeset()
            elif downCableS(i).relation.getname() == "max":
                self.max = downCableS(i).max
            else:
                self.min = downCableS(i).min
    elif self.name == "thresh":
        for i in len(self.downCableS):
            if downCableS(i).relation.getname() == "arg":
                self.ant = downCableS(i).getnodeset()
                self.cq = downCableS(i).getnodeset()
            elif downCableS(i).relation.getname() == "threshmax":
                self.max = downCableS(i).threshmax
            else:
                self.min = downCableS(i).thresh


def apply(RuleNode, attuide):
    if isSupported(RuleNode, attuide):
        if checkcombatiblesubstitutions(RuleNode.downCableS.antecedents):
            match RuleNode.name:
                case "or":
                    c = or_entailment(RuleNode)
                case "and":
                    c = and_entailment(RuleNode)
                case "andor":
                    c = andor(RuleNode)
                case "thresh":
                    c = thresh(RuleNode)
                case "numerical_entailment":
                    c = numerical_entailment(RuleNode)
        if checkcombatiblesubstitutions(c):
            x = RuleNode.downCableS.antecedents.append(c)
            n = combinesupports(x)
            report(c, n, RuleNode.name, RuleNode.source, RuleNode.destination)


def combinesupports(n):
    # this is a stub or a driver
    return n


def checkcombatiblesubstitutions(x):
    # this is a stub or a driver
    return True


def isSupported(x, zd):
    # this is a stub or a driver
    return True


def report(c, supports, name, source, destination):
    print(c, supports, name, source, destination)
