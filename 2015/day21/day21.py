from itertools import combinations


boss = {
    'hp': 109,
    'damage': 8,
    'armor': 2
}

player = {
    'hp': 100,
    'damage': 0,
    'armor': 0
}

weapons = [
    {'name': 'Dagger', 'cost': 8, 'damage': 4, 'armor': 0},
    {'name': 'Shortsword', 'cost': 10, 'damage': 5, 'armor': 0},
    {'name': 'Warhammer', 'cost': 25, 'damage': 6, 'armor': 0},
    {'name': 'Longsword', 'cost': 40, 'damage': 7, 'armor': 0},
    {'name': 'Greataxe', 'cost': 74, 'damage': 8, 'armor': 0}
]

armor = [
    {'name': 'None', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'Leather', 'cost': 13, 'damage': 0, 'armor': 1},
    {'name': 'Chainmail', 'cost': 31, 'damage': 0, 'armor': 2},
    {'name': 'Splintmail', 'cost': 53, 'damage': 0, 'armor': 3},
    {'name': 'Bandedmail', 'cost': 75, 'damage': 0, 'armor': 4},
    {'name': 'Platemail', 'cost': 102, 'damage': 0, 'armor': 5}
]

rings = [
    {'name': 'None', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'Damage +1', 'cost': 25, 'damage': 1, 'armor': 0},
    {'name': 'Damage +2', 'cost': 50, 'damage': 2, 'armor': 0},
    {'name': 'Damage +3', 'cost': 100, 'damage': 3, 'armor': 0},
    {'name': 'Defense +1', 'cost': 20, 'damage': 0, 'armor': 1},
    {'name': 'Defense +2', 'cost': 40, 'damage': 0, 'armor': 2},
    {'name': 'Defense +3', 'cost': 80, 'damage': 0, 'armor': 3}
]

def fight(player, boss):
    player_hp = player['hp']
    boss_hp = boss['hp']
    while True:
        boss_hp -= max(1, player['damage'] - boss['armor'])
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss['damage'] - player['armor'])
        if player_hp <= 0:
            return False
        
def buy(player, weapon, armor_item, rings):
    player['damage'] = weapon['damage']
    player['armor'] = armor_item['armor']  # Changed parameter name
    player['cost'] = weapon['cost'] + armor_item['cost']
    for ring in rings:
        player['damage'] += ring['damage']
        player['armor'] += ring['armor']
        player['cost'] += ring['cost']
    return player

def try_equipment(player, boss, weapon, armor_item, ring_combo):
    # Create a new player state for each attempt
    current_player = player.copy()
    current_player = buy(current_player, weapon, armor_item, ring_combo)
    return fight(current_player, boss)

# Replace the main loop section with:
min_cost = float('inf')
max_cost = 0

# Try all possible combinations
for weapon in weapons:
    for armor_item in armor:
        for num_rings in range(3):
            for ring_combo in combinations(rings[1:], num_rings):
                # Create new player state and buy equipment
                current_player = player.copy()
                current_player = buy(current_player, weapon, armor_item, ring_combo)
                
                # Simulate fight and track costs
                if fight(current_player, boss):
                    min_cost = min(min_cost, current_player['cost'])
                else:
                    max_cost = max(max_cost, current_player['cost'])

print(f"Minimum cost to win: {min_cost}")
print(f"Maximum cost to lose: {max_cost}")
