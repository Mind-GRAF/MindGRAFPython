class or_entailment:
    pass

def or_entailment(node ):
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).propositionset:
            if (antecedents(e).propositionset(i).sign==True):
                return node.downCableS.consequents