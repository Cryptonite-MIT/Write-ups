import random
import string

def decrypt_string(input_string, seed):
    random.seed(seed)
    
    encrypted_string = bytes.fromhex(input_string)


    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=len(input_string)//2))
    
    flag = ''
    
    for i in range(len(encrypted_string)):
        decrypted_char = chr(encrypted_string[i] ^ ord(key[i]))
        flag += decrypted_char
    return flag


seed_value = 202242269
input_string = "5e04610a22042638723c571e1a5436142764061f39176b4414204636251072220a35583a60234d2d28082b"
decrypted = decrypt_string(input_string, seed_value)
print(decrypted)