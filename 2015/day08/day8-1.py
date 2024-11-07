import re

with open('input.txt') as f:
    lines = f.readlines()
    code = sum([len(x) for x in lines])
    memory = sum([len(x.encode('utf-8').decode('unicode_escape')) - 2 for x in lines])
    print(code - memory)
