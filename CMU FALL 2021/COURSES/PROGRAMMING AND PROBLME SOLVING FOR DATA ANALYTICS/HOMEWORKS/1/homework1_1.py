"""
Author: Jean Paul Nishimirwe
Andrew Id: jnishimi
Date created: On 14th Sept 2021

About a program:
--------------
1. A program takes any kind of input and store them in a list.
2. If a user enters "-1", a program stops prompting a user to enter data.
3. A program filters all data stored in an array and extract only positive odd integers without duplicates.
4. For those extracted data (positive odd integers), it calculates the sum and average of those numbers.
5. A program prints the sum and average calculated on the screen.

"""
# My two helper variables (loop & save) and initialize both to true
loop=True
save=True
my_list=list() 
while loop: # The loop will loop until loop as long as loop variable is still True
    value=input("Enter Data: ") 
    if value == "-1": # I am checking is a user enters "-1". The following two lines of codes will be executed if they enter "-1"
        loop=False # This will stop a loop to loop again
        save=False # This will make me not save the entered -1 because I do not need it.
    if save: # Only save is true if a user does not enter "-1"
        my_list.append(value) 
        
"""
Up to here, I have saved all data entered except last -1 that used to stop a loop.
I am going to extract only positive odd integers and store them in "allowed_values" list
"""
allowed_values=[]
for i in my_list:
    # the following if Checks three things: value is a digit, if a value is not creating duplicates and a value is odd
    i=i.strip()
    if i.isdigit() and int(i) not in allowed_values and int(i)%2 != 0: 
        allowed_values.append(int(i)) 
print(f"Sum: {sum(allowed_values)} , Average: {sum(allowed_values)/len(allowed_values)}")  # Use in-built function to find sum, avg