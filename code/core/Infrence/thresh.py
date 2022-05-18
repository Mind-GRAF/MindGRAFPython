class thresh:
    pass

def thresh(node ):
    min = node.i
    max = node.j
    counter = 0
    for e in node.node.downCableS.antecedents:
        if(antecedents(e)==True):
            counter+=1
            if(counter<max&counter>=min):
                return node.downCableS.consequents