from typing import Type
from numerical_entailment import numerical_entailment
from or_entailment import or_entailment
from and_entailment import and_entailment
from andor import andor
from thresh import thresh


class RuleNode:
    Type = str
    antecedents = list
    consequents = list
    downCableS = list
    min = int
    max = int


def __init__(self, downCableS):
    self.downCableS = downCableS
    self.antecedents = self.downCableS.antecedents
    self.consequents = self.downCableS.consequents

    if self.downCableS.min & self.downCableS.max:
        self.Type = "andor,thresh"
    elif self.downCableS.min:
        self.Type = "numerical"
    else:
        self.Type = "and-Entailment,or-Entailment"


def apply(node, context, attuide):
    if isSupported(node, attuide):
        if checkcombatiblesubstitutions(node.downCableS.antecedents):
            match node.name:
                case "or":
                    c = or_entailment(node)
                case "and":
                    c = and_entailment(node)
                case "andor":
                    c = andor(node)
                case "thresh":
                    c = thresh(node)
                case "numerical_entailment":
                    c = numerical_entailment(node)
        if checkcombatiblesubstitutions(c):
            x = node.downCableS.antecedents.append(c)
            n = combinesupports(x)
            report(c, n, node.name, node.source, node.destination)


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
