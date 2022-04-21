from code.core.Infrence.numerical_entailment import numerical_entailment
from code.core.Infrence.numerical_entailment import or_entailment
from code.core.Infrence.numerical_entailment import and_entailment
from code.core.Infrence.numerical_entailment import andor
from code.core.Infrence.numerical_entailment import thresh

class apply:
    pass
def apply(node,context):
    if(issupported(node,context)):
        checkcontext(context)
        match node.name:
            case "or":
                c = or_entailment(node,context)
            case "and":
                c = and_entailment(node,context)
            case "andor":
                c = andor(node,context)
            case "thresh":
                c = thresh(node,context)
            case "numerical_entailment":
                c = numerical_entailment(node,context)
        if(checkcombatiblesubstitutions(c)):
            combinesupports(context.supports)
            report(c,node.supports,node.name,node.source,node.destination)

def combinesupports(n):
    #this is a stub or a driver
    return True
def checkcombatiblesubstitutions(x):
    #this is a stub or a driver
    return True

def issupported(x,z):
    #this is a stub or a driver
    return True

def checkcontext(f):
    #this is a stub or a driver
    return True
def report(c,supports,name,source,destination):
    print(c,supports,name,source,destination)
