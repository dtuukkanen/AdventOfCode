with open('input.txt') as f:
    lines = f.readlines()
    code = sum([len(x) for x in lines])
    extended = sum([len(x.replace('\\', '\\\\').replace('"', '\\"')) + 2 for x in lines])
    print(extended - code)
