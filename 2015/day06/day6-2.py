led_matrix = [[0 for x in range(1000)] for y in range(1000)]

def main():
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if line.startswith('turn on'):
                x1, y1 = map(int, line.split()[2].split(','))
                x2, y2 = map(int, line.split()[4].split(','))
                turn_on(x1, y1, x2, y2)
            elif line.startswith('turn off'):
                x1, y1 = map(int, line.split()[2].split(','))
                x2, y2 = map(int, line.split()[4].split(','))
                turn_off(x1, y1, x2, y2)
            elif line.startswith('toggle'):
                x1, y1 = map(int, line.split()[1].split(','))
                x2, y2 = map(int, line.split()[3].split(','))
                toggle(x1, y1, x2, y2)
    print(sum([sum(row) for row in led_matrix]))

def turn_on(x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            led_matrix[x][y] += 1

def turn_off(x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if led_matrix[x][y] > 0:
                led_matrix[x][y] -= 1
            else:
                led_matrix[x][y] = 0

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            led_matrix[x][y] += 2

main()
