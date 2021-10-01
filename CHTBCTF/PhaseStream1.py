from Crypto.Util.number import *;

def xor(bstr1,bstr2):
    ans = ""
    for i,j in zip(bstr1,bstr2):
        ans += chr(i^j)
    return ans


ct = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"
ct = int(ct,16)
ct = long_to_bytes(ct)
key = chr(ct[0]^ord('C')) + chr(ct[1]^ord('H')) + chr(ct[2]^ord('T'))+chr(ct[3]^ord('B'))+chr(ct[4]^ord('{'))
pt = ""
for i in range(len(ct)):
    pt += chr(ct[i] ^ ord(key[i%5]))
print(pt)
