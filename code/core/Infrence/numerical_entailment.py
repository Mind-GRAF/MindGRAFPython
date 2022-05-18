def numerical_entailment(node  ):
    min = node.downCableS.min
    counter = 0
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).supports:
            if (node.downCableS.antecedents(e).supports(i).sign==True) :
                counter+=1
                if counter>= min:
                    return node.downCableS.consequents