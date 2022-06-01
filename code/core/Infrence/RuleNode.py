from numerical_entailment import numerical_entailment
from or_entailment import or_entailment
from and_entailment import and_entailment
from andor import andor
from thresh import thresh
from PropositionNode import PropositionNode


class RuleNode(PropositionNode):
    name = ""
    ant = []
    cq = []
    downCableS = []
    min = 0
    max = 0
    source = ""
    destination = ""
    # this constructur is only for testing purposes input and output signatures should be taken from the Main constructor
    def __init__(self, name, ant, cq, downCableS, source, destination):
        self.source = source
        self.destination = destination
        self.name = name
        self.ant = ant
        self.cq = cq
        self.downCables = downCableS
        self.source = source
        self.destination = destination
        apply(self, "NULL")

    def __init__2(self, name, ant, cq, downCableS, min, max, source, destination):
        self.source = source
        self.destination = destination
        self.name = name
        self.ant = ant
        self.cq = cq
        self.downCables = downCableS
        self.min = min
        self.max = max

    # this is the main and offical constructor of Rule node
    def __init__3(self, downCableS, source, destination):
        self.source = source
        self.destination = destination
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
        if checkcombatiblesubstitutions(RuleNode.ant):
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
            print(c)
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


# Testing stuff below (beware) ;
RuleNode.__init__(
    self=RuleNode,
    name="or",
    ant=["p", "q"],
    cq=["p"],
    downCableS=["ant", "cq"],
    source="source",
    destination="destination",
)
print(RuleNode.name)
# RuleNode.__init__("and", ["p", "p->q"], ["q"], ["&ant", "cq"])
# RuleNode.__init__("numerical_entailment", ["p", "p->q"], ["q"], ["&ant", "cq", "i"], 1)
# RuleNode.__init__("andor", ["p", "p->q"], ["q"], ["args", "min", "max"], 1, 2)
# RuleNode.__init__("thresh", [], [], ["args", "thresh", "threshmax"], 0, 1)
