with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip() for x in inp]
# part1
# r = 0
# for c, x in enumerate(inp):
#     print(x[:(3*c)%31] + "O" + x[(3*c)%31 + 1:])
#     if x[(3*c)%31] == "#":
#         r+=1

# part2
# def getTreesSlope(input, right, down):
#     r = 0
#     c = 0
#     s = 1
#     for x in input:
#         if s == 1:
#             s = down
#         else:
#             s -= 1
#             continue
#         print(x[:(right*c)%31] + "O" + x[(right*c)%31 + 1:])
#         if x[(right*c)%31] == "#":
#             r+=1
#         c += 1
#     return r
#
# res = 1
# for i in range(1, 10, 2):
#     res *= getTreesSlope(inp, i%8, (i//8)+1)

