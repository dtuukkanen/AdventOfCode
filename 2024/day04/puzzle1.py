pattern = "XMAS"

def horizontal(data):
    found = 0
    for row in data:
        for i in range(len(row)-len(pattern)+1):
            if row[i:i+len(pattern)] == pattern:
                found += 1
            if row[i:i+len(pattern)] == pattern[::-1]:
                found += 1

    return found

def vertical(data):
    found = 0

    # Transpose the data
    data = list(map(list, zip(*data)))
    for row in data:
        row = "".join(row)
        for i in range(len(row)-len(pattern)+1):
            if row[i:i+len(pattern)] == pattern:
                found += 1
            if row[i:i+len(pattern)] == pattern[::-1]:
                found += 1

    return found

def diagonal(data):
    found = 0
    # Diagonal 1
    for i in range(len(data)-len(pattern)+1):
        for j in range(len(data[0])-len(pattern)+1):
            diag4_forward = "".join([data[i+k][j+k] for k in range(len(pattern))])
            if diag4_forward == pattern:
                found += 1
            if diag4_forward == pattern[::-1]:
                found += 1

    # Diagonal 2
    # Reverse the data
    data = data[::-1]
    for i in range(len(data)-len(pattern)+1):
        for j in range(len(data[0])-len(pattern)+1):
            diag4_forward = "".join([data[i+k][j+k] for k in range(len(pattern))])
            if diag4_forward == pattern:
                found += 1
            if diag4_forward == pattern[::-1]:
                found += 1

    return found

def main():
    found_total = 0
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [row.strip() for row in data]
        found_total += horizontal(data)
        found_total += vertical(data)
        found_total += diagonal(data)

    print(found_total)

main()
