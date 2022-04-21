from code.core.Infrence.apply import apply


class or_entailment(apply):
    pass

def or_entailment(node ,context ):
    for e in node.ant:
        if (e==True):
            return node.con