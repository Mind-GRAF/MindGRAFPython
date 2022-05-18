class numerical_entailment:
    pass
def numerical_entailment(node  ):
    min = node.i
    counter = 0
    for e in node.node.downCableS.antecedents:
        if (antecedents(e)==True) :
            counter+=1
            if counter>= min:
                return node.downCableS.consequents