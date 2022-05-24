def thresh(RuleNode):
    min = RuleNode.min
    max = RuleNode.max
    counter = 0
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).supports:
            if RuleNode.ant(e).supports(i).sign == True:
                counter += 1
                if counter < max & counter >= min:
                    return RuleNode.cq
