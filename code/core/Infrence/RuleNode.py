from typing import Type
from numerical_entailment import numerical_entailment
from or_entailment import or_entailment
from and_entailment import and_entailment
from andor import andor
from thresh import thresh
from PropositionNode import PropositionNode


class RuleNode(PropositionNode):
    name = str
    Type = str
    antecedents = list
    consequents = list
    downCableS = list
    min = int
    max = int


def __init__(self, downCableS, name):
    self.name = name
    self.downCableS = downCableS
    self.antecedents = self.downCableS.antecedents
    self.consequents = self.downCableS.consequents

    if self.downCableS.min & self.downCableS.max:
        self.Type = "andor,thresh"
    elif self.downCableS.min:
        self.Type = "numerical"
    else:
        self.Type = "and-Entailment,or-Entailment"


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
