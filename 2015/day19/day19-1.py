def init():
    replacements = {}
    with open("input.txt") as file:
        data = file.read().strip().split("\n")
        molecule = data.pop()
        data.pop() # Remove empty line
        for row in data:
            key, value = row.split(" => ")
            if key not in replacements:
                replacements[key] = []
            replacements[key].append(value)
    return replacements, molecule

def generate_distinct_molecules(replacements, molecule):
    distinct_molecules = set()
    for key in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(key)] == key:
                for replacement in replacements[key]:
                    new_molecule = molecule[:i] + replacement + molecule[i+len(key):]
                    distinct_molecules.add(new_molecule)
    return distinct_molecules

def main():
    replacements, molecule = init()
    distinct_molecules = generate_distinct_molecules(replacements, molecule)
    print(len(distinct_molecules))

main()
