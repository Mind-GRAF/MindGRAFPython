def thresh(RuleNode):
    min = RuleNode.min
    max = RuleNode.max
    counter = 0
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).channels:
            if RuleNode.ant(e).channels(i).report.sign == True:
                counter += 1
                if counter < max & counter >= min:
                    return RuleNode.cq
