class andor :
    pass

def andor(node  ):
    min = node.i
    max = node.j
    counter = 0
    for e in node.downCableS.antecedents:
        if(antecedents(e)==True):
            counter+=1
            if(counter==max):
                node.downCableS.consequents=node.downCableS.antecedents.iter(max)
                return node.downCableS.consequents
            elif(counter==min):
                node.downCableS.consequents=node.downCableS.antecedents.remove(node.ant.iter(node.size-min))
                return node.downCableS.consequents