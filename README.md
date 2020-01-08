![alt text](https://github.com/Bw3ll/JOP_ROCKET/blob/master/jopRocket3.jpg)
# JOP ROCKET

The Jump-oriented Programming Reversing Open Cyber Knowledge Expert Tool, or JOP ROCKET, is a tool designed to help facilitate JOP gadget discovery in an x86 Windows environment. This tool has not been released yet.  This tool was released at DEF CON 27, where it was the subject of a talk by Dr. Bramwell Brizendine and Dr. Josh Stroschein.

Please navigate to [https://github.com/Bw3ll/JOP_ROCKET](https://github.com/Bw3ll/JOP_ROCKET/) in order to download this tool. 

The tool is a Python script utilizing the Capstone disassembly enginge as well as other dependencies. This software exploitation tool is a fully featured artifact designed to facilitate Jump-oriented Programming. It is intended to be run on Windows, but can also run on any environment with the dependencies, albeit in a more limited context outside Windows. 

Usage information is not available at this time beyond what is in the help menu. Constructing JOP exploits is not straightforward and is very nuanced, with some parallels but many differences from ROP. Please refer to DEF CON talk to see a brief demo.

This tool has been taught at Dakota State University in the doctoral program, as part of CSC 848: Advanced Software Exploitation, the most challenging course in the program. The students completed exploits that included bypassing DEP and ASLR.

Thank you to Austin Babcock for his help with various issues relating to the JOP ROCKET, including his install instructions. He is a master of JOP. 



## Basic install instructions for JOP ROCKET
### Step 1:
Install Python 2.7. The easiest way to do this will be from the website: https://www.python.org/download/releases/2.7/
If you already have Python 3, you will still need to have Python 2.7 as the tool will not work properly with Python 3.
If you have both, you will need to add the special comment: 

**#!python2**

to the top of rocket.py. Then run with "py rocket.py" rather than "python rocket.py". This will ensure the program is run using Python 2.7.

![alt text](https://github.com/Bw3ll/JOP_ROCKET/blob/master/python.jpg)

### Step 2:
install pip if it isn't already included with Python.
-	https://pip.pypa.io/en/stable/installing/

You will need to save the script provided and run it, as per the instructions on the link. If you run into an error, try using the “alternate” script.

If pip still doesn't work, try adding "C:\python27\Scripts" (or your corresponding directory) to your Path system variable:

-	Start
-	Right click Computer
-	Properties
-	Advanced System Settings
-	Advanced tab
-	Environment Variables

![alt text](https://github.com/Bw3ll/JOP_ROCKET/blob/master/environ.jpg)

### Step 3:
Start installing dependencies with pip!

_Note: Installations with pip should work using the Windows terminal, but may not work in a Cygwin environment. If using Cygwin, you may need to install with source code instead. This can be a more time-consuming endeavor, and you are referred to the latest documentation from the different makers of the dependencies._
-	**pip install capstone**
- **pip install pefile2**

   - You will likely already have pefile installed with Python 2.7, but this version is old.
   - Pefile2 is what you need.

   - You may need to **pip uninstall pefile** to get the program to use pefile2.
-	Etc... A list of dependencies can be found at the bottom of this document. Each must be installed, if they are not already.
-	The two above are likely the only ones you will need to install yourself.

Many of the dependencies already come with Python. To list available modules, open a prompt:


![alt text](https://github.com/Bw3ll/JOP_ROCKET/blob/master/modules.jpg)

Look through the list and see if you have all the dependencies. For those you don't have, install with pip or via source code.

### Dependencies:
-	Capstone
-	Win32file
-	Win32api
-	Pefile2
-	Ctypes

### Errors:
If you are getting errors like "SyntaxError: Missing parentheses in call to 'print'", it is likely running with Python 3. Try doing the fix outlined in Step 1 to make the program use Python 2.
Errors related to “lists” or “ui” likely are caused by the location of the **lists.py** and **ui.py** files. Make sure these files are in the same directory as **rocket.py**.

## More advanced install steps

To utilize this in a Cygwin environment, you likely will need to install Capstone from the source. There are varous ways to do so, and Capstone's documentation provides assistance. Cygwin was used during the development of the tool.

## Basic Usage

More detailed usage information is forthcoming. Refer to the DEF CON 27 talk and the help sub-menu for assistance.

To get started though, you want to have the three Python files in the same directory: rocket.py, ui.py, and lists.py. Then run from command line. You can provide a local file in the install directory, but it will not be able to find modules/DLL's. To find these, the program must be installed, and the absolute path to the application can be supplied as input inside a text file that can be provided as an argument on the command line, e.g.
   python rocket.py input
