def andor(node):
    min = node.downCableS.min
    max = node.downCableS.max
    counter = 0
    for e in node.downCableS.antecedents:
        for i in node.downCableS.antecedents(e).supports:
            if(node.downCableS.antecedents(e).supports(i).sign==True):
                counter+=1
                if(counter==max):
                    node.downCableS.consequents=node.downCableS.antecedents.iter(max)
                    return node.downCableS.consequents
                elif(counter==min):
                    node.downCableS.consequents=node.downCableS.antecedents.remove(node.ant.iter(node.size-min))
                    return node.downCableS.consequents