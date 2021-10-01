import itertools
from z3 import *
import math
def test():
    chars = "0013AABEEFGHMMNNPRTUUY._LKZT"
    l = list(chars)
    ll = []
    for k in l:
        ll.append(ord(k))
    print(ll)
    a = [Real(f'{i}') for i in range(28)]
    s = Solver()
    s.add(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27] == 2024)
    #s.add(a[0]^a[1]^a[2]^a[3]^a[4]^a[5]^a[6]^a[7]^a[8]^a[9]^a[10]^a[11]^a[12]^a[13]^a[14]^a[15]^a[16]^a[17]^a[18]^a[19]^a[20]^a[21]^a[22]^a[23]^a[24]^a[25]^a[26]^a[27] == 126)
    s.add(a[0] - a[1] == 1)
    # s.add(a[0] == ord('L'))
    # s.add(a[1] == ord('K'))
    # s.add(a[2] == ord('Z'))
    s.add(ToInt(a[1] * a[2] * a[3] / 1846) == 277)
    s.add(a[4] + a[5] - a[6] + a[7] == 114)
    s.add(ToInt(a[8] * a[9] / a[10] * a[11]) == 3249)
    s.add(ToInt(a[13] / a[12] / a[14] * a[15]) == 1)
    s.add(a[18] == ord('T'))
    s.add(a[6] == a[17])
    s.add(ToInt(a[19] * a[20] / a[21]) == 46)
    s.add(a[22] + a[23] - a[24] == 116)
    s.add(a[25] + a[26] + a[27] == 138)
    p = 0
    for i in range(0,28):
        s.add(a[i] in ll)
        print(i)
    # for i in range(0,28):
    #     p = p<<5 - p + a[i]
    # s.add(p == -685590366)
    print(s.check())
    model = s.model()
    print(model)
    # flag = ''.join([chr(int(str(model[a[i]]))) for i in range(len(model))])
    # print(flag)
def solve():
    sum = 0
    x = 0
    # chars = "0013AABEEFGHMMNNPRTUUY._LKZT"
    chars = "ZYPH.BFHT00AHL030FT.10UM...."
    # final ="LKZ"
    # final[18] = "T"
    # perm = itertools.permutations(chars, 6)
    # for i in perm:
    #     if ord(i[0])*ord(i[1])/ord(i[2])==46 and ord(i[3])+ord(i[4])-ord(i[5])==116 and ord(i[6])+ord(i[7])+ord(i[8])==138:
    #         print(i)

    for i in chars:
        sum+=ord(i)
        x=x^ord(i)
    print(sum, x)
solve()
