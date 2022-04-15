import subprocess
import re
import sys
#import pwntools

n = len(sys.argv)
#print("Total arguments passed:", n)

if n <= 1:
	print("exiting...")
	sys.exit()

proc = subprocess.Popen(['python', 'rocket.py', sys.argv[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

rocket_commands = "Z\nP\n"

#output = proc.stdout.readline()
#print(output)

out, _ = proc.communicate(bytes("Z\nP\n"))
#print(out.decode('utf-8'))

#proc.stdin.write(rocket_commands.encode())
#output = proc.stdout.read()
