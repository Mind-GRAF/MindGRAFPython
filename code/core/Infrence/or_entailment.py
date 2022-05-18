class or_entailment:
    pass

def or_entailment(node ):
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).supports:
            if (node.downCableS.antecedents(e).supports(i).sign==True):
                return node.downCableS.consequents