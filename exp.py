import subprocess
import re
#import pwntools

proc = subprocess.Popen(['python', 'rocket.py', 'pe-Windows-x86-cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

rocket_commands = "Z\nP\n"

#output = proc.stdout.readline()
#print(output)

#out, _ = proc.communicate(bytes("Z\nP\n"))
#print(out.decode('utf-8'))

proc.stdin.write(rocket_commands.encode())
output = proc.stdout.read()
print(output)