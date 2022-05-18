class thresh:
    pass

def thresh(node):
    min = node.i
    max = node.j
    counter = 0
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).supports:
            if(node.downCableS.antecedents(e).supports(i).sign==True):
                counter+=1
                if(counter<max&counter>=min):
                    return node.downCableS.consequents