from numerical_entailment import numerical_entailment
from or_entailment import or_entailment
from and_entailment import and_entailment
from andor import andor
from thresh import thresh


def apply(node,context):
    if(isSupported(node,context[node])):
        checkcontext(context)
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
        if(checkcombatiblesubstitutions(c)):
            combinesupports(node.supports)
            report(c,node.supports,node.name,node.source,node.destination)

def combinesupports(n):
    #this is a stub or a driver
    return True
def checkcombatiblesubstitutions(x):
    #this is a stub or a driver
    return True

def isSupported(x,z):
    #this is a stub or a driver
    return True

def checkcontext(f):
    #this is a stub or a driver
    return True
def report(c,supports,name,source,destination):
    print(c,supports,name,source,destination)
