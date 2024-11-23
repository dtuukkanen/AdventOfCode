input = 36000000

def sum_of_divisors(n):
    # Get divisors up to sqrt(n) and their pairs
    divisors = set()
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            divisors.add(j)
            divisors.add(n // j)
    return sum(divisors) * 10

i = 1
while True:
    presents = sum_of_divisors(i)
    if presents >= input:
        print("SOLUTION FOUND!")
        print("Solution -", "house:", i, "presents:", presents)
        break
    i += 1
