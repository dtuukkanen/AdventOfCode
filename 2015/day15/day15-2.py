import itertools

ingredients = []
with open('input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split(' ')
        capacity = int(parts[2][:-1])
        durability = int(parts[4][:-1])
        flavor = int(parts[6][:-1])
        texture = int(parts[8][:-1])
        calories = int(parts[10])
        ingredients.append((capacity, durability, flavor, texture, calories))

max_score = 0
# Generate all possible combinations of ingredient amounts that sum to 100
for amounts in itertools.product(range(101), repeat=len(ingredients)):
    if sum(amounts) == 100:
        capacity = sum(amounts[i] * ingredients[i][0] for i in range(len(ingredients)))
        durability = sum(amounts[i] * ingredients[i][1] for i in range(len(ingredients)))
        flavor = sum(amounts[i] * ingredients[i][2] for i in range(len(ingredients)))
        texture = sum(amounts[i] * ingredients[i][3] for i in range(len(ingredients)))
        
        # Ignore negative values
        if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
            score = capacity * durability * flavor * texture
            if sum(amounts[i] * ingredients[i][4] for i in range(len(ingredients))) == 500:
                max_score = max(max_score, score)

print(max_score)
