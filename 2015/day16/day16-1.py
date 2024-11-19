def main():
    with open('input.txt') as file:
        lines = file.readlines()

    sues = []
    for line in lines:
        sue = {}
        parts = line.split()
        sue['number'] = int(parts[1][:-1])
        for i in range(2, len(parts), 2):
            sue[parts[i][:-1]] = int(parts[i + 1].replace(',', ''))
        sues.append(sue)

    for i, sue in enumerate(sues):
        try:
            if three_matches(sue):
                print(sue['number'])
                break
        except KeyError:
            continue # Ignore missing keys

def three_matches(sue):
    matching = 0
    if sue.get("children") == 3:
        matching += 1
    if sue.get("cats") == 7:
        matching += 1
    if sue.get("samoyeds") == 2:
        matching += 1
    if sue.get("pomeranians") == 3:
        matching += 1
    if sue.get("akitas") == 0:
        matching += 1
    if sue.get("vizslas") == 0:
        matching += 1
    if sue.get("goldfish") == 5:
        matching += 1
    if sue.get("trees") == 3:
        matching += 1
    if sue.get("cars") == 2:
        matching += 1
    if sue.get("perfumes") == 1:
        matching += 1
    
    return matching >= 3

main()
