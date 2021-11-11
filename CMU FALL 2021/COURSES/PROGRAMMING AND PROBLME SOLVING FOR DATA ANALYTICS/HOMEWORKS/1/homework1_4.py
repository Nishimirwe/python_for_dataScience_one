"""
Author: Jean Paul Nishimirwe
Andrew Id: jnishimi
Date Created : On 14th Sept 2021

About a program
----------------
1. A program loops throug a list of all python built-in functions
2. For each function, a program prints a documentation about that function.
3. A program appends all those documentations in an output file names output_hw1.txt
4. A program writes in a file using a format provided in assignment instructions.


Hint: 1. Documentations of each function is stored in "__doc__" attribute
      2. built-ins can be accessed using builtins module
      3. To get a list of all built-ins functions, you may use "dir(builtins)"
"""
import builtins
all_built_in=dir(builtins) # Storing all builtins
f = open("output_hw1_3.txt", "w")
for fun in all_built_in:
    f.write("---------------------------------\n")
    f.write(f"{fun.capitalize()}: {type(eval(fun))}\n")
    f.write("---------------------------------\n")
    f.write(f"\n{eval(fun).__doc__} \n")
    f.write(f"Where: {type(eval(fun))} is the the type of {eval(fun)}, \n")
    f.write(f"Retrieved by type({fun}) \n  \n")
f.close()