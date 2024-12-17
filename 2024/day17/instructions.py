def _division_operation(registers, combo_operand):
    numerator = registers["A"]
    if combo_operand in ["A", "B", "C"]:
        denominator = 2 ** registers[combo_operand]
    else:
        denominator = 2 ** combo_operand
    result = int(numerator / denominator)
    return result


def adv(registers, combo_operand):
    registers["A"] = _division_operation(registers, combo_operand)


def bxl(registers, literal_operand):
    result = registers["B"] ^ literal_operand
    registers["B"] = result


def bst(registers, combo_operand):
    if combo_operand in ["A", "B", "C"]:
        result = registers[combo_operand] % 8
    else:
        result = combo_operand % 8
    registers["B"] = result


def jnz(registers, literal_operand):
    if registers["A"] != 0:
        return literal_operand
    return None


def bxc(registers, literal_operand): # Takes operand, but ignores it for legacy reasons
    result = registers["B"] ^ registers["C"]
    registers["B"] = result


def out(registers, combo_operand):
    if combo_operand in ["A", "B", "C"]:
        result = registers[combo_operand] % 8
    else:
        result = combo_operand % 8
    return result


def bdv(registers, combo_operand):
    registers["B"] = _division_operation(registers, combo_operand)


def cdv(registers, combo_operand):
    registers["C"] = _division_operation(registers, combo_operand)
