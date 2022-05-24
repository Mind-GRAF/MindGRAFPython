def numerical_entailment(RuleNode):
    min = RuleNode.min
    counter = 0
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).supports:
            if RuleNode.ant(e).supports(i).sign == True:
                counter += 1
                if counter >= min:
                    return RuleNode.cq
