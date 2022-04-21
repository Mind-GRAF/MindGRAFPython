class thresh(apply):
    pass

def thresh(node ,context ):
    min = node.i
    max = node.j
    counter = 0
    for e in node.ant:
        if(e==True):
            counter+=1
            if(counter<max&counter>=min):
                return node.con