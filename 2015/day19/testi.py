def init():
    replacements = {}
    with open("input.txt") as file:
        data = file.read().strip().split("\n")
        molecule = data.pop()
        data.pop() # Remove empty line
        for row in data:
            key = row.split(" => ")[0]
            value = row.split(" => ")[1]
            if key not in replacements:
                replacements[key] = []
            replacements[key].append(value)
    return replacements, molecule

def main():
    replacements, molecule = init()
    molecules = set()
    for key in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(key)] == key:
                for replacement in replacements[key]:
                    new_molecule = molecule[:i] + replacement + molecule[i+len(key):]
                    molecules.add(new_molecule)
    print(len(molecules))

main()