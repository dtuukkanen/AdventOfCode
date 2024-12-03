def isGradual(levels):
    for i in range(len(levels) - 1):
        curr = levels[i]
        next = levels[i + 1]
        if curr > next or differTooMuch(curr, next):
            return False
    return True

def isDecreasing(levels):
    for i in range(len(levels) - 1):
        curr = levels[i]
        next = levels[i + 1]
        if curr < next or differTooMuch(curr, next):
            return False
    return True

def differTooMuch(current, next):
    difference = abs(current - next)
    if difference < 1 or difference > 3 :
        return True
    return False

safe_reports = 0
with open("input.txt") as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        levels = list(map(int, line.split(" ")))
        if isGradual(levels) or isDecreasing(levels):
            safe_reports += 1
print(safe_reports)
