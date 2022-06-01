def and_entailment(RuleNode):
    flag = False
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).channels:
            if RuleNode.ant(e).channels(i).report.sign == True:
                flag = True
            else:
                flag = False
                break
    if flag == True:
        return RuleNode.cq
