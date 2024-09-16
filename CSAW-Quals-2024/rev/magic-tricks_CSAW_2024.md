I started by running the challenge file, which produced an `output.txt` containing the flag encrypted by a magic box algorithm. I tested this by giving `csawctf{` as input, which worked—producing the same output as in `output.txt`. This led me to believe the challenge involved **angr**, so I asked ChatGPT to write a Python script for bruteforcing:

```python
pythonCopy codeimport itertools
import subprocess
import filecmp

# Define characters to bruteforce
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
prefix = 'csawctf{'
suffix = '}'

# Generate possible input combinations
def bruteforce_input():
    for length in range(1, 20):  # Adjust as needed
        for attempt in itertools.product(charset, repeat=length):
            yield prefix + ''.join(attempt) + suffix

# Run the challenge program
def run_chall(input_str):
    process = subprocess.Popen(['./chall', input_str], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate()

# Compare output.txt with sus.txt
def compare_output():
    return filecmp.cmp('output.txt', 'sus.txt', shallow=False)

# Main bruteforce loop
def main():
    for attempt in bruteforce_input():
        print(f"Trying: {attempt}")
        run_chall(attempt)
        if compare_output():
            print(f"Found matching input: {attempt}")
            break

if __name__ == "__main__":
    main()
```

### Issues with the Script

The approach didn't work well. Although it fuzzed through, I realized it would take too long, and angr might crash.

### Switching to Ghidra

I installed the **Goland extension for Ghidra** and began analyzing the challenge. I encountered this snippet of Go code:

```go
goCopy codefor (lVar3 = 0; lVar3 < extraout_RAX_00; lVar3 = lVar3 + 1) {
    iVar1 = *(int *)(extraout_RAX_01 + lVar3 * 4);
    *(int *)(extraout_RAX_01 + lVar3 * 4) =
        (int)((long)((long)iVar1 + 0x17U ^ (long)(iVar1 + -1) << 1) % 4) + iVar1 * 2 + -0x20;
}
```

I asked ChatGPT for a summary, and the logic became clearer:

- Adds 23 to the input.
- XORs it with the previous element.
- Applies modulo 4, adds the result to the element multiplied by 2, and subtracts 32.

I then asked ChatGPT to write a reverse script for this encoding, and here's what I got:

```python
pythonCopy codedef reverse_encoding(target):
    decoded_chars = []
    for target_value in target:
        for possible_input in range(32, 127):  # Printable ASCII range
            encoded_value = ((possible_input + 23) ^ (possible_input - 1) << 1) % 4 + possible_input * 2 - 32
            if encoded_value == target_value:
                decoded_chars.append(chr(possible_input))
                break
    return ''.join(decoded_chars)

def main():
    with open('sus.txt', 'r', encoding='utf-8') as f:
        target_data = [ord(c) for c in f.read().strip()]
    
    decoded_string = reverse_encoding(target_data)
    print("Decoded string:", decoded_string)

if __name__ == "__main__":
    main()
```

```bash
alias@LAPTOP-VBFDDHQB:/mnt/c/Users/Aayush/Downloads/CSAW/Mys$ python3 solve.py
Decoded string: csawctf{tHE_runE5_ArE_7H3_k3y_7O_th3_G0ph3r5_mA91C}
alias@LAPTOP-VBFDDHQB:/mnt/c/Users/Aayush/Downloads/CSAW/Mys$
```



magic !!!!!!!!!

### Conclusion

I learned that sometimes you gotta go the hardway and look for ghidra extentions and acutally reverse engineer stuff.
Golang stripped binary is not something easy to play with but this plugin helped a lot 

[mooncat-greenpy/Ghidra_GolangAnalyzerExtension: Analyze Golang with Ghidra (github.com)](https://github.com/mooncat-greenpy/Ghidra_GolangAnalyzerExtension)

