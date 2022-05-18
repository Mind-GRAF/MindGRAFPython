class and_entailment:
    pass

def and_entailment(node):
    flag=False
    for e in node.downCableS.antecedents:
        if (antecedents(e)==True):
            flag=True
        else:
            flag=False
            break
    if(flag==True):
        return node.downCableS.consequents