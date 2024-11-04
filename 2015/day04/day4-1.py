import hashlib

puzzle_input = "bgvyzdsv"

i = 0
while True:
    if hashlib.md5((puzzle_input + str(i)).encode()).hexdigest().startswith("00000"):
        print(i)
        break
    i += 1
