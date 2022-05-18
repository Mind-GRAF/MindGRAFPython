def and_entailment(node):
    flag=False
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).supports:
            if (node.downCableS.antecedents(e).supports(i).sign==True):
                flag=True
            else:
                flag=False
                break
    if(flag==True):
        return node.downCableS.consequents