def main():
    with open('input.txt') as file:
        lines = file.readlines()

    sues = []
    for line in lines:
        sue = {
            "children": -1,
            "cats": -1,
            "samoyeds": -1,
            "pomeranians": -1,
            "vizslas": -1,
            "goldfish": -1,
            "trees": -1,
            "cars": -1,
            "perfumes": -1,
        }
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

    if sue.get("children") == 3 and sue["children"] != -1:
        matching += 1
    if sue.get("cats") > 7 and sue["cats"] != -1:
        matching += 1
    if sue.get("samoyeds") == 2 and sue["samoyeds"] != -1:
        matching += 1
    if sue.get("pomeranians") < 3 and sue["pomeranians"] != -1:
        matching += 1
    if sue.get("akitas") == 0 and sue["akitas"] != -1:
        matching += 1
    if sue.get("vizslas") == 0 and sue["vizslas"] != -1:
        matching += 1
    if sue.get("goldfish") < 5 and sue["goldfish"] != -1:
        matching += 1
    if sue.get("trees") > 3 and sue["trees"] != -1:
        matching += 1
    if sue.get("cars") == 2 and sue["cars"] != -1:
        matching += 1
    if sue.get("perfumes") == 1 and sue["perfumes"] != -1:
        matching += 1
    
    return matching >= 3

main()
