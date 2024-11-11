def increment(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        # if the letter is z, change it to a and continue to the next letter
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def has_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 and ord(password[i]) == ord(password[i + 2]) - 2:
            return True
    return False

def has_no_bad_letters(password):
    for letter in password:
        if letter in ['i', 'o', 'l']:
            return False
    return True

def has_two_pairs(password):
    pairs = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs >= 2

password = "cqjxjnds"
found_passwords = 0
while True:
    password = increment(password)
    if has_straight(password) and has_no_bad_letters(password) and has_two_pairs(password):
        found_passwords += 1
        if found_passwords == 2:
            print(password)
            break


