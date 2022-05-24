def andor(RuleNode):
    min = RuleNode.min
    max = RuleNode.max
    counter = 0
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).supports:
            if RuleNode.ant(e).supports(i).sign == True:
                counter += 1
                if counter == max:
                    RuleNode.downCableS.consequents = RuleNode.ant.iter(max)
                    return RuleNode.downCableS.consequents
                elif counter == min:
                    RuleNode.downCableS.consequents = RuleNode.ant.remove(
                        RuleNode.ant.iter(RuleNode.size - min)
                    )
                    return RuleNode.cq
