reindeer = {}

with open("input.txt") as file:
    data = file.read().splitlines()
    for line in data:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer[name] = (speed, fly_time, rest_time)

def distance(name, time):
    speed, fly_time, rest_time = reindeer[name]
    cycle_time = fly_time + rest_time
    cycles = time // cycle_time
    remaining_time = time % cycle_time
    distance = cycles * fly_time * speed
    distance += min(remaining_time, fly_time) * speed
    return distance

time = 2503
max_distance = 0
for name in reindeer:
    max_distance = max(max_distance, distance(name, time))
print(max_distance)
