import sys
year = 2020

with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]
inp = [int(x) for x in inp]
inp = list(set(inp))
inp = sorted(inp)
helper = []
for number in inp:
    helper = [number]
    for number2 in inp:
        helper.append(number2)
        for number3 in inp:
            helper.append(number3)
            somme = sum(helper)
            if somme == year:
                result = 1
                for correct in helper:
                    result = correct * result
                print(helper, somme, result)
                sys.exit(0)
            del helper[-1]
        del helper[-1]

