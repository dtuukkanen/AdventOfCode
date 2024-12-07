def evaluate(result, values):
    temp_results = [values[0]]  # Initialize with first value

    for i in range(1, len(values)):
        new_results = []
        for prev_result in temp_results:
            # Add current value to previous results
            new_results.append(prev_result + values[i])
            # Multiply current value with previous results
            new_results.append(prev_result * values[i])
            # Concatenate current value to previous results
            new_results.append(int(str(prev_result) + str(values[i])))
        temp_results = new_results

    if result in temp_results:
        return True
    return False




def main():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            splitted = line.split(": ")
            result = int(splitted[0])
            values = list(map(int, splitted[1].split(" ")))
            if evaluate(result, values):
                total += result
    print(total)

if __name__ == '__main__':
    main()
