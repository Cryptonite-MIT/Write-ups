from Crypto.Util.number import *
known = int("2d0fb3a56aa66e1e44cffc97f3a2e030feab144124e73c76d5d22f6ce01c46e73a50b0edc1a2bd243f9578b745438b00720870e3118194cbb438149e3cc9c0844d640ecdb1e71754c24bf43bf3fd0f9719f74c7179b6816e687fa576abad1955",16)
ct = int("2767868b7ebb7f4c42cfffa6ffbfb03bf3b8097936ae3c76ef803d76e11546947157bcea9599f826338807b55655a05666446df20c8e9387b004129e10d18e9f526f71cabcf21b48965ae36fcfee1e820cf1076f65",16)
known = long_to_bytes(known)
ct= long_to_bytes(ct)
pt = ""
for i,j in zip(known,ct):
    pt += chr(i^j)
known_text = b"I alone cannot change the world, but I can cast a stone across the water to create many ripples"
ans = ""
for i,j in zip(known_text,pt):
    ans += chr(i^ord(j))
print(ans)
