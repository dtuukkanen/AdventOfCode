import itertools

input = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]

def find_combinations(input, target):
    for i in range(1, len(input) + 1):
        for combination in itertools.combinations(input, i):
            if sum(combination) == target:
                yield combination

combinations = list(find_combinations(input, 150))
containers = [len(combination) for combination in combinations]
minimum_containers = min(containers)
print(containers.count(minimum_containers))
