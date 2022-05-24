def and_entailment(RuleNode):
    flag = False
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).supports:
            if RuleNode.ant(e).supports(i).sign == True:
                flag = True
            else:
                flag = False
                break
    if flag == True:
        return RuleNode.cq
