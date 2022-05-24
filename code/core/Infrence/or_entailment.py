def or_entailment(RuleNode):
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).supports:
            if RuleNode.ant(e).supports(i).sign == True:
                return RuleNode.cq
