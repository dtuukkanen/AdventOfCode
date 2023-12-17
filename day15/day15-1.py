def hash(word):
    hash = 0
    for c in word:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


def read_input():
    with open("input.txt") as file:
        items = file.read().strip().split(",")
    return items


def main():
    result = 0
    input = read_input()
    for each in input:
        result += hash(each)
    print(result)


main()
