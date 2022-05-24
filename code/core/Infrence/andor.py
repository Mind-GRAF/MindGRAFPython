def andor(RuleNode):
    min = RuleNode.downCableS.min
    max = RuleNode.downCableS.max
    counter = 0
    for e in RuleNode.downCableS.antecedents:
        for i in RuleNode.downCableS.antecedents(e).supports:
            if RuleNode.downCableS.antecedents(e).supports(i).sign == True:
                counter += 1
                if counter == max:
                    RuleNode.downCableS.consequents = (
                        RuleNode.downCableS.antecedents.iter(max)
                    )
                    return RuleNode.downCableS.consequents
                elif counter == min:
                    RuleNode.downCableS.consequents = (
                        RuleNode.downCableS.antecedents.remove(
                            RuleNode.ant.iter(RuleNode.size - min)
                        )
                    )
                    return RuleNode.downCableS.consequents
