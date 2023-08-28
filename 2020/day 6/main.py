with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]

# part1
# grpans = []
# res = 0
#
# def getuniquefrommultiset(grpans):
#     unitedgrpans = ""
#     uniqueset = ""
#     for x in grpans:
#         unitedgrpans += x
#     for k in unitedgrpans:
#         if k not in uniqueset:
#             uniqueset += k
#     return len(uniqueset)
#
#
# for x, i in enumerate(inp):
#     if i:
#         grpans.append(i)
#         if x == len(inp)-1:
#             res += getuniquefrommultiset(grpans)
#         continue
#     if not(i):
#         res += getuniquefrommultiset(grpans)
#         grpans = []

# part2
# grpans = []
# res = 0
#
# def getcommonvalue(grpans):
#     j = []
#     for e in grpans:
#         g = []
#         for k in e:
#             g.append(k)
#         j.append(g)
#     return len(list(set.intersection(*map(set, j))))
#
#
# for x, i in enumerate(inp):
#     if i:
#         grpans.append(i)
#         if x == len(inp)-1:
#             res += getcommonvalue(grpans)
#         continue
#     if not(i):
#         res += getcommonvalue(grpans)
#         grpans = []

