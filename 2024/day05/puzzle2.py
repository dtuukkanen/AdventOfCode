def is_valid_sequence(rules_graph, sequence):
    # Check each pair of pages in the sequence
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            page1, page2 = sequence[i], sequence[j]

            # If there's a rule saying page2 should come before page1,
            # this sequence is invalid
            if page2 in rules_graph and page1 in rules_graph[page2]:
                return False

    return True

def fix_sequence(rules_graph, sequence):
    sequence = list(sequence)  # Make a copy to modify
    changed = True
    while changed:
        changed = False
        for i in range(len(sequence)-1):
            for j in range(i+1, len(sequence)):
                # If we find a violation, swap the elements
                if sequence[j] in rules_graph and sequence[i] in rules_graph[sequence[j]]:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                    changed = True
    return sequence

def build_graph(rules):
    graph = {}
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if before not in graph:
            graph[before] = set()
        graph[before].add(after)
    return graph

def solve_puzzle(input_text):
    # Split input into rules and sequences
    parts = input_text.strip().split('\n\n')
    rules = parts[0].split('\n')
    sequences = [list(map(int, seq.split(','))) for seq in parts[1].split('\n')]

    # Build the rules graph
    rules_graph = build_graph(rules)

    # Process each sequence
    total = 0
    for sequence in sequences:
        if not is_valid_sequence(rules_graph, sequence):
            fixed_sequence = fix_sequence(rules_graph, sequence)
            # Find middle page number
            middle_idx = len(fixed_sequence) // 2
            total += fixed_sequence[middle_idx]

    return total


def main():
    with open('input.txt') as f:
        input_text = f.read()
    print(solve_puzzle(input_text))

main()
