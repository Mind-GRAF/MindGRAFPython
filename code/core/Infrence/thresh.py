class thresh:
    pass

def thresh(node):
    min = node.i
    max = node.j
    counter = 0
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).propositionset:
            if(antecedents(e).propositionset(i).sign==True):
                counter+=1
                if(counter<max&counter>=min):
                    return node.downCableS.consequents