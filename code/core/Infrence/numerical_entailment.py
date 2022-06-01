def numerical_entailment(RuleNode):
    min = RuleNode.min
    counter = 0
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).channels:
            if RuleNode.ant(e).channels(i).report.sign == True:
                counter += 1
                if counter >= min:
                    return RuleNode.cq
