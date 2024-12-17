import instructions

def read_input():
    registers = {}
    with open("input.txt") as file:
        lines = file.readlines()
        register_input = lines[:3]
        program_input = lines[4]

        # Handle register input
        for line in register_input:
            splitted = line.strip().split(": ")
            register = splitted[0].split(" ")[1]
            value = int(splitted[1])
            registers[register] = value

        # Handle program input
        splitted = program_input.strip().split(": ")
        program = list(map(int, splitted[1].split(",")))

    return registers, program

def run_program(registers, program):
    i = 0
    outputs = []
    while i < len(program) - 1:
        opcode = program[i]
        literal_operand = program[i + 1]
        combo_operand = find_operand(literal_operand)

        if opcode == 0:
            instructions.adv(registers, combo_operand)
        elif opcode == 1:
            instructions.bxl(registers, literal_operand)
        elif opcode == 2:
            instructions.bst(registers, combo_operand)
        elif opcode == 3:
            jump = instructions.jnz(registers, literal_operand)
            if jump is not None:
                i = jump
                continue
        elif opcode == 4:
            instructions.bxc(registers, literal_operand)
        elif opcode == 5:
            output = instructions.out(registers, combo_operand)
            outputs.append(output)
        elif opcode == 6:
            instructions.bdv(registers, combo_operand)
        elif opcode == 7:
            instructions.cdv(registers, combo_operand)

        i += 2
    return list(map(int, outputs))

def find_operand(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return "A"
    elif operand == 5:
        return "B"
    elif operand == 6:
        return "C"
    elif operand == 7:
        return "reserved"
    return operand


def grow_i(index, output, target):
    for i in range(1, len(target) + 1):
        if output[-i] != target[-i]:
            return index + 2 ** ((len(target) - i) * 3)
    return index


def main():
    registers, program = read_input()
    target = program

    start = 2 ** ((len(target) - 1) * 3)
    end = 2 ** (len(target) * 3)

    i = start
    while i < end:
        registers["A"] = i
        output = run_program(registers, program)

        if output == target:
            print("Found!")
            print(i)
            break
        else:
            i = grow_i(i, output, target)


main()
