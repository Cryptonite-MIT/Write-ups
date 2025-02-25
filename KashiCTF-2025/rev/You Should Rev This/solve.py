from subprocess import Popen, PIPE, STDOUT
import string
import sys

# Build the command; sys.argv[1] is the target executable.
command = "perf stat -x : -e instructions:u " + sys.argv[1] + " 1>/dev/null"

password = ''

while True:
    ins_count = 0
    count_chr = ''
    for i in string.printable:
        # Set text=True to work with strings directly.
        target = Popen(command, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True, text=True)
        # Send the current guess (password + candidate character) as input.
        target_output, _ = target.communicate(input=f'{password + i}\n')
        # Split the output by ':' and convert the first field to int.
        instructions = int(target_output.split(":")[0])
        if instructions > ins_count:
            count_chr = i
            ins_count = instructions
    password += count_chr
    print(password)
