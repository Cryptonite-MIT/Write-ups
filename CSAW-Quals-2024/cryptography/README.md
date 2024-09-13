# Trapdoor

given c1, c2, e, n1, n2. 
Classic RSA challenge. There was nothing similar or vulnerable at first glance. \
Moduli can't be factored either.

But when you GCD the moduli, You find the result is a prime. 
i.e. the moduli are of the form 
`n1 = p * q`
`n2 = p * r`

solve script :
```python
from Crypto.Util.number import *

c1 = 161657267735196834912863135763588255051084768060167522685145600975477606522389267911595494255951389308603585891670155516473228040572472139266242046480464411011926872432857745283026840801445383620653451687523682849171134262795620963422201106957732644189004161198543408780876818402717692426183521358742475772803427948145681912577138151854201287217310388360035006450255979612146528569192238510701666997268424852524879191797074298541592238357746219444160311336448978081899531731524195638715227224903445226248602579764214997719090230906191407229446647313099400956970509035654967405630240939959592998616003498236942092817559461000588623573048030445521863492730870242644395352424593752773001495951737895664115609421618170689951704330184048125307163740226054228480085636314748554185748105182003072934516641741388554856693783207538862673881733984454590126630762754413784860309730736733101522402317095930278893263812433036953457501549714213711757368647750210251899325644773678135753158374375837529620580830355398764871600754340989211159192515899566042173210432362519000596760898915443009768635625263875643978408948502726014770826616858752941269838500371205265923373317700072776319154266968103160778573051363936325056002056286215658714259892131
c2 = 494623168173341363340467373358957745383595056417571755948370162317759417390186160270770025384341351293889439841723113891870589515038055355274713359875028285461281491108349357922761267441245606066321766119545935676079271349094728585175909045924367012097484771776396598141703907624715907730873180080611197080012999970125893693838478647963157490065546947042621326070901482489910203413759703603136944502613002083194569025640046380564488058425650504612206627739749051853591610981053026318569730551988841304231276711969977298162726941928222523464544797141812329957714866356009363861914935745207975118182966833811723664044706845207847731129336219505772833893718601825819419057471717431953601897992835582033908346998397116046369365580899868759006665351628889935594587647946796811554073758809039163703319444890860711787316692186294350180062910771860180483152240985537326837665737974072086105081591429007858987697382766650868798693024212101169297652870122729568327958629779258375463408029863902774673729692698603549762248768090302360950262068792179771304874203556781584256503067131440856389473604578859795120178476492827306744971082872861030028803971595639553063854220185280566575307797482645881434704155764917254239587927218075951473385530833
e = 65537
n1 = 537269810177819460077689661554997290782982019008162377330038831815573146869875494409546502741769078888560119836988893807659619131795600022996155542011901767164659622251852771410530047820953404275439162903782253582402317577272023052873061733154947413969140900242586288282386516940748102303139488999388815366805771566027048823971232923901589854972341140497344922557809346957285480088567527430942352224246175865278666886538920772608403444601667114300055814252644535406924681931233694920723837668899531758291081568304763353729111948368345349994099868469305792181073122419940610781784779666456780500932337154438538720823939250386789917476722260336949625831449027815346423132208841389383282133423240342633209093536658578807788187537292687621305485734565276685038174693348234827761258142100019798785254244633108887403538365377022084266245064851786520352683721896084403163679116876924559581709943841877168418550922700610256010165841228197765129411475811684669156709601802234298096100301516880419138890353002776631827361005170877640327516465104169299292924318171783865084478980121378972145656688829725118773293892358855082049175572479466474304782889913529927629420886850515337785270820884245044809646784251398955378537462225157041205713008379
n2 = 675112413040615754855341368347991520700645749707972662375138119848808538466484973026629442817490775679486087477873647170707728077849174294413106449041183548981099164777126469098349759962366886352375485394430924686294932854410357033579891793697466117311282071223849125728247324019661552591602816412461639181036083039951358738639409104870090776274099206184327026885209301129700589120263558741373320717866973004474880824451611558352986814186406024139122101780061421498582804842387331594088633719788918481809465044314609904522824483927173924396330723272200351268059583559155873089840203176526189465332287149408627146863937339106591410131104971158916770664709755851365697530033135116269758729627681863469646687585133174854282299126206393656205822175860114547244407037919126445577158000448033562711159480289599400271620922791664179514807098083591794558148460941940996477066832640360820650342057071277962750427121243576612067919616033880922920641430414655749007393524344586517489346008845986135281381956392366857764758769758991862758292829265731964283719870708510272500471228442964550074672417445262035130720875562744233719280755235051883245392409892775011413342074824090752055820699150296553380118608786447588243723987854862785887828651597

p = GCD(n1,n2)
q = n1 // p

phi = (p-1)*(q-1)
d = inverse(e,phi)
print(long_to_bytes(pow(c1,d,n1)).decode()) 
# The Euclidean algorithm is the granddaddy of all algorithms,
# because it is the oldest nontrivial algorithm that has
# survived to the present day.

q = n2 // p

phi = (p-1)*(q-1)
d = inverse(e,phi)
print(long_to_bytes(pow(c2,d,n2)).decode())
# csawctf{n0_p0lyn0m1al_t1m3_f4ct0r1ng_n33d3d_t0_0p3n_th1s_tr4pd00r!}
```

***

# hexhex

given is a huge txt with a lines of hexes with different delimeters. \
If you start decoding each line, removing the delimeters \
The first few lines decoded look something like this : 
```
In a distant future, humanity had evolved beyond the confines of Earth. Nations no longer warred over borders or resources, but engaged in an endless contest of intellect\xe2\x80\x94an event that had replaced traditional conflicts, known as the "Cyber Security Awareness Worldwide Capture The Flag," or simply the CSAW CTF. The world\'s brightest minds would gather, competing to solve mind-bending puzzles in code, AI, and philosophy. Winning wasn\xe2\x80\x99t just a badge of honor\xe2\x80\x94it was how civilizations demonstrated dominance, knowledge, and wisdom.
```

but this felt too laborious. then I scrolled a bit down and saw this in the handout \
![image](https://github.com/user-attachments/assets/03441c35-70d9-4189-97cc-e4d8faa9eef0)

unlike the other texts, this was not a direct hex encoded message. as it had characters beyond the hexadecimal `0123456789abcdef`. \
So i put this in dcode. and it was a twin hex cipher. Which on decoding gives the flag. \
![image](https://github.com/user-attachments/assets/5bcab755-9f2d-4d23-a8a5-a85ff9d84267)

`csawctf{hex3d_i7_w3l7_innit_hehe}`

***

# Diffusion Pop Quiz

given was an nc and a script to assist 
```python
# 3 input bits: 000, 001, 010, 011, 100, 101, 110, 111
# Array indexes: 0    1    2    3    4    5    6    7
# f(x1,x2,x3):   0    1    0    0    0    1    1    1

# Customize the following settings to extract specific bits of specific S-Boxes and have a comfortable visualization of terms.

SYMBOL = 'x'
INPUT_BITS = 3
OUTPUT_BITS = 1
SBOX = example
BIT = 1

# Ignore the functions, we've implemented this for you to save your time.
# Don't touch it, it might break and we don't want that, right? ;)

def get_sbox_result(input_int):
    return SBOX[input_int]

def get_term(binary_string):
    term = ""
    i = 1
    for (count,bit) in enumerate(binary_string):
        if bit == "1":
            term += SYMBOL+str(i)+"*"
        i += 1

    if term == "":
        return "1"

    return term[:-1]

def get_poly(inputs, outputs):
    poly = ""
    for v in inputs:
        if outputs[v]:
            poly += get_term(v) + "+"
    return poly[:-1]

def should_sum(u, v, n):
    for i in range(n):
        if u[i] > v[i]:
            return False

    return True

def get_as(vs, f, n):
    a = {}
    for v in vs:
        a[v] = 0
        for u in vs:
            if should_sum(u, v, n):
                a[v] ^= f[u]

    return a

def get_anf(vs, f, n):
    return get_poly(vs, get_as(vs, f, n))

def get_vs_and_fis_from_sbox(which_fi):
    vs = []
    fis = {}
    for input_integer in range(2**INPUT_BITS):
        sbox_output = get_sbox_result(input_integer)
        input_integer_binary = bin(input_integer)[2:].zfill(INPUT_BITS)
        fis[input_integer_binary] = 0
        sbox_output_binary = bin(sbox_output)[2:].zfill(OUTPUT_BITS)

        vs.append(input_integer_binary)
        fis[input_integer_binary] = int(sbox_output_binary[which_fi-1])

    return vs, fis

def get_anf_from_sbox_fi(which_fi):
    vs, fis = get_vs_and_fis_from_sbox(which_fi)
    poly = get_anf(vs, fis, INPUT_BITS)
    return poly

output = get_anf_from_sbox_fi(BIT)
print(output)
```

It was pretty straight forward. You just had to answer the questions in the quiz, with or without the help of the script provided. \
All the material to solve was provided. This challenge was intended to teach players about diffusion and converting boolean truth tables to \
ANF. Which it did pretty well. Answering all the questions correctly gives you the flag. \
![image](https://github.com/user-attachments/assets/17d43d6b-3782-4531-bde7-a9441689c62e)

***

# AES Diffusion

This was another quiz, a continuation of the last challenge kind of. \
Given was an nc and below script \
```python
N_ROWS = 4
N_COLS = 4

def CyclicShift(row, shift):
    return row[shift:] + row[:shift]

def ShiftRows(state):
    for row_index in range(N_ROWS):
        state[row_index] = CyclicShift(state[row_index], row_index)
    return state

def BuildExpressionString(column, matrix_row):
    expression = "("
    for (i,coefficient) in enumerate(matrix_row):
        term = str(coefficient) + "*" + column[i]
        should_insert_plus = i < len(matrix_row) - 1
        expression += term
        
        if should_insert_plus:
            expression += " + "
    return expression + ")"

def GetStateColumn(state, column_index):
    column = []
    for row in state:
        column.append(row[column_index])
    return column

def MultiplyColumn(column):
    matrix = [
                [2, 3, 1, 1],
                [1, 2, 3, 1],
                [1, 1, 2, 3],
                [3, 1, 1, 2]
            ]
    
    new_column = []
    for row in matrix:
        new_element = BuildExpressionString(column, row)
        new_column.append(new_element)
    return new_column

def MixColumns(state):
    new_columns = []
    for column_index in range(N_COLS):
        column = GetStateColumn(state, column_index)
        new_column = MultiplyColumn(column)
        new_columns.append(new_column)
    
    return Transpose(new_columns)

def Transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def PrettyPrint(matrix):
    for row in matrix:
        print(row)

def PrettyPrint2(matrix):
    for row in matrix:
        for element in row:
            print(element)

state = [["x0", "x4", "x8", "x12"], 
         ["x1", "x5", "x9", "x13"], 
         ["x2", "x6", "x10", "x14"],
         ["x3", "x7", "x11", "x15"]]

def AESRound(state):
    return MixColumns(ShiftRows(state))

def AES(state, rounds):
    for r in range(rounds):
        state = MixColumns(state)
    return state

PrettyPrint(AES(state,2))
```

Once again just had to follow along the questions, using the script provided. \
Answering all questions gave the flag. \
![image](https://github.com/user-attachments/assets/41ce75f6-0ce4-4926-bf0a-d65fcdd79b60)

***

# CBC

Given was an nc , the script for it, and a ciphertext.
```python
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os

def decrypt(txt: str) -> (str, int):
    try:
        token = bytes.fromhex(txt)

        c = AES.new(os.environ["AES_KEY"].encode(), AES.MODE_CBC, iv=os.environ["AES_IV"].encode())
        plaintext = c.decrypt(token)
        unpadded = unpad(plaintext, 16)
        
        return unpadded, 1
    except Exception as s:
        return str(s), 0

def main() -> None:
    while True:
        text = input("Please enter the ciphertext: ")
        text.strip()
        out, status = decrypt(text)
        if status == 1:
            print("Looks fine")
        else:
            print("Error...")

if __name__ == "__main__":
    main()
```
so AES CBC. (duh) \
The nc would try to decrypt a plaintext you send and return Error or Looks Good. \
```python
def decrypt(txt: str) -> (str, int):
    try:
        token = bytes.fromhex(txt)

        c = AES.new(os.environ["AES_KEY"].encode(), AES.MODE_CBC, iv=os.environ["AES_IV"].encode())
        plaintext = c.decrypt(token)
        unpadded = unpad(plaintext, 16)
        
        return unpadded, 1
     except Exception as s:
        return str(s), 0
```
the status `1` for `Looks Good` is returned only when the ciphertext is successfullly decrypted and unpadded \
Therefore An error on decrypting could only mean `wrong padding`. \
i.e. \
This was a `padding oracle` challenge. but with 300 blocks lmao. \
Referred to this video to understand padding oracle attack properly. \
https://www.youtube.com/watch?v=O5SeQxErXA4

after a few hours, we ended up with this script 
```python
from pwn import *
from binascii import hexlify, unhexlify

conn = remote('cbc.ctf.csaw.io', 9996)

with open('out.txt', 'r') as file:
    ct = file.read().strip()

ct = unhexlify(ct)
assert len(ct) % 16 == 0
blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
pt = b''

def send(payload):
    conn.sendlineafter(b'Please enter the ciphertext: ', payload)
    response = conn.recvline().strip()
    if b'Looks fine' in response:
        return True
    else: return False

def get_key_byte(ind, c0, c1, c2):
    for guess in range(256):
        modified_c1 = bytearray(c1)
        modified_c1[-ind] = guess
        payload = hexlify(c0 + bytes(modified_c1) + c2)
        if send(payload):
            print(f"ind: {ind}\t guess: {guess}")
            return guess
    return -1

def get_keystream(c0, c1, c2):
    keystream = bytearray(16)
    keystream[-1] = get_key_byte(1, c0, c1, c2) ^ 0x01 ^ c2[-1]
    for ind in range(2, 17):  
        c1 = bytearray(c1)
        for i in range(1, ind):
            c1[-i] = keystream[-i] ^ ind ^ c2[-i]
        c1 = bytes(c1)
        keystream[-ind] = get_key_byte(ind, c0, c1, c2) ^ ind ^ c2[-ind]
        print(f"ind: {ind}\t keystream: {bytes(keystream)}")
    return keystream

for i in range (0, len(blocks)-2):
    keystream = get_keystream(blocks[i], blocks[i+1], blocks[i+2])
    pt = pt + xor(keystream, blocks[i+1], blocks[i+2])
    print(pt)
```

It took a while. But after a few hours of running this script. We got the flag\
![image](https://github.com/user-attachments/assets/b7c38ffd-9df0-4c38-97f7-08c8fca5541b)

`csawctf{I_L0ST_TR4CK_0N_WH3R3_I_W4S_G01NG_W1TH_TH15}`

***
