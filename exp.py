import subprocess
import re
import sys
#import pwntools

n = len(sys.argv)
#print("Total arguments passed:", n)

if n <= 1:
	print("exiting...")
	sys.exit()

try:
	proc = subprocess.Popen(['python', 'rocket.py', sys.argv[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
except:
	print("Check file name, exiting...")
	sys.exit()

rocket_commands = "Z\nP\n"

#output = proc.stdout.readline()
#print(output)

try:
	out, _ = proc.communicate(bytes("Z\nP\n"))
except:
	print("Exiting...")
	sys.exit()

proc.terminate()
sys.exit()
#print(out.decode('utf-8'))

#proc.stdin.write(rocket_commands.encode())
#output = proc.stdout.read()
