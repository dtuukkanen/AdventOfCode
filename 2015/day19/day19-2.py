import random

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

def steps_to_molecule(replacements, target):
    # Create reverse replacements dictionary
    reverse_replacements = {}
    for key, values in replacements.items():
        for value in values:
            reverse_replacements[value] = key
    
    # Start with target molecule
    current = target
    steps = 0
    
    # We should reduce from longest replacements first
    sorted_replacements = sorted(reverse_replacements.keys(), key=len, reverse=True)
    
    # Keep replacing until we get 'e'
    while current != 'e':
        original = current
        
        # Try each replacement in order of length
        for value in sorted_replacements:
            key = reverse_replacements[value]
            if value in current:
                # Always replace leftmost occurrence for deterministic behavior
                current = current.replace(value, key, 1)
                steps += 1
                break
                
        # If no replacement was possible and we're not at 'e', this path failed
        if original == current and current != 'e':
            return float('inf')
            
    return steps


def main():
    replacements, molecule = init()
    print(steps_to_molecule(replacements, molecule))

main()
