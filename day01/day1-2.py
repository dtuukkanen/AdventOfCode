import regex


def word_to_digit(word):
    word_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    return word_to_number.get(word, None)


def find_digits(s):
    # Find all matches of either words or digits
    matches = regex.findall(
        r"zero|one|two|three|four|five|six|seven|eight|nine|\d", s, overlapped=True
    )
    # Convert words to digits
    if matches:
        first_digit = (
            word_to_digit(matches[0]) if matches[0].isalpha() else int(matches[0])
        )
        last_digit = (
            word_to_digit(matches[-1]) if matches[-1].isalpha() else int(matches[-1])
        )
    return str(first_digit) + str(last_digit)


def count_sum(words):
    calibration_value = 0

    for word in words:
        calibration_value += int(find_digits(word))

    return calibration_value


if __name__ == "__main__":
    with open("input.txt") as input_file:
        words = [line.strip() for line in input_file]
    print(count_sum(words))
