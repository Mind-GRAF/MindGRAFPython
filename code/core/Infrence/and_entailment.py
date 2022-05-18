class and_entailment:
    pass

def and_entailment(node):
    flag=False
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).propositionset:
            if (antecedents(e).propositionset(i).sign==True):
                flag=True
            else:
                flag=False
                break
    if(flag==True):
        return node.downCableS.consequents