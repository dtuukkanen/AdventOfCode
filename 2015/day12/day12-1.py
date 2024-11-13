import json

def sum_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    elif isinstance(data, dict):
        return sum(sum_numbers(value) for value in data.values())
    return 0

def main():
    with open('input.txt') as f:
        data = json.load(f)
    total_sum = sum_numbers(data)
    print(total_sum)

if __name__ == "__main__":
    main()