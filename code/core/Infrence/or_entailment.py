def or_entailment(RuleNode):
    for e in RuleNode.ant:
        for i in RuleNode.ant(e).channels:
            if RuleNode.ant(e).channels(i).report.sign == True:
                return RuleNode.cq
