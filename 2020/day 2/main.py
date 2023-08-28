with open("input.txt") as f:
    inp = f.readlines()
inp = [x.strip().replace(':','').replace('-',' ').split(' ') for x in inp]
#firstpart
# c = 0
# for e in inp:
#     if int(e[0])<= e[3].count(e[2]) <= int(e[1]): c+=1

#secondpart
# c = 0
# for e in inp:
#     try:
#         k = e[-1][int(e[0]) - 1]
#     except IndexError:
#         k = ' '
#     try:
#         l = e[-1][int(e[1])-1]
#     except IndexError:
#         l = ' '
#     if (e[2]==k)^(e[2]==l):c+=1
# print(c)