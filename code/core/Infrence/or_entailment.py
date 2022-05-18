class or_entailment:
    pass

def or_entailment(node ):
    for e in node.downCableS.antecedents:
        if (antecedents(e)==True):
            return node.downCableS.consequents