import re

with open("input.txt") as f:
    inp = f.readlines()

# part1
# r = 0
# fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# info = {}
# for l in inp:
#     if l == "\n":
#         if set(fields).issubset(info.keys()):
#             r += 1
#         info = {}
#     else:
#         e = l.strip().split()
#         for i in e:
#             f = i.split(":")
#             info[f[0]] = f[1]
#         if set(fields).issubset(info.keys()):
#             r += 1
#             info = {}

# part2
# r = 0
# fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# b = True
# info = {}
# for l in inp:
#     if l == "\n":
#         info = {}
#         b = True
#     else:
#         e = l.strip().split()
#         for i in e:
#             f = i.split(":")
#             info[f[0]] = f[1]
#         if set(fields).issubset(info.keys()):
#             byr = int(info.get("byr"))
#             if not (2003 > byr > 1919):
#                 b = False
#             iyr = int(info.get("iyr"))
#             if not (2021 > iyr > 2009):
#                 b = False
#             eyr = int(info.get("eyr"))
#             if not (2031 > eyr > 2019):
#                 b = False
#             hgt = info.get("hgt")
#             match = re.match("([0-9]+)((cm|in))", hgt, re.I)
#             if match:
#                 items = match.groups()
#                 if items:
#                     if items[1] == "cm":
#                         if not (194 > int(items[0]) > 149):
#                             b = False
#                     elif items[1] == "in":
#                         if not (77 > int(items[0]) > 58):
#                             b = False
#                     else:
#                         b = False
#                 else:
#                     b = False
#             hcl = info.get("hcl")
#             result = re.match("^#[a-f0-9]{6}", hcl)
#             if not result:
#                 b = False
#             ecl = info.get("ecl")
#             result = re.match("(amb|blu|brn|gry|grn|hzl|oth)", ecl)
#             if not result:
#                 b = False
#             pid = info.get("pid")
#             result = re.match("[0-9]{9}", pid)
#             if not result:
#                 b = False
#             if b is True:
#                 print(info)
#                 r += 1
#             info = {}
#             b = True
