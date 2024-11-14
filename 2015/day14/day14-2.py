reindeer = {}

with open("input.txt") as file:
    data = file.read().splitlines()
    for line in data:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer[name] = {"speed": speed, "fly_time": fly_time, "rest_time": rest_time, "fly_time_left": fly_time, "rest_time_left": rest_time, "distance": 0, "points": 0}

time = 2503

for t in range(time):
    for name in reindeer:
        if reindeer[name]["fly_time_left"] > 0:
            reindeer[name]["distance"] += reindeer[name]["speed"]
            reindeer[name]["fly_time_left"] -= 1
            if reindeer[name]["fly_time_left"] == 0:
                reindeer[name]["rest_time_left"] = reindeer[name]["rest_time"]
        else:
            reindeer[name]["rest_time_left"] -= 1
            if reindeer[name]["rest_time_left"] == 0:
                reindeer[name]["fly_time_left"] = reindeer[name]["fly_time"]
    
    max_distance = 0
    best_reindeer = ""
    for name in reindeer:
        if reindeer[name]["distance"] > max_distance:
            max_distance = reindeer[name]["distance"]
            best_reindeer = name
    reindeer[best_reindeer]["points"] += 1

print(max(reindeer[name]["points"] for name in reindeer))
