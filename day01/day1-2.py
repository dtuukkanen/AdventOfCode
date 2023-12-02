digits = {
        "one": 1,
        "two": 2,
        "three": 3, 
        "four": 4,
        "five": 5,
        "six": 6,
        "seven":7, 
        "eight": 8,
        "nine": 9
        }

def trebuchet(words):
    calibration_value = 0

    for word in words:
        if word in digits:
            calibration_value += digits[word]


    return calibration_value

if __name__ == "__main__":

