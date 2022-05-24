def thresh(RuleNode):
    min = RuleNode.downCableS.min
    max = RuleNode.downCableS.max
    counter = 0
    for e in RuleNode.downCableS.antecedents:
        for i in RuleNode.downCableS.antecedents(e).supports:
            if RuleNode.downCableS.antecedents(e).supports(i).sign == True:
                counter += 1
                if counter < max & counter >= min:
                    return RuleNode.downCableS.consequents
