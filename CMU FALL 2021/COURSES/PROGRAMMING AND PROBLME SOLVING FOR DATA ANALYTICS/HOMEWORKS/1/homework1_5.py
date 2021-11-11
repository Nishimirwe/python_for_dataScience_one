"""
Author: Jean Paul Nishimirwe
Andrew Id: jnishimi
Date created: On 14th Sept 2021

About a program
----------------
 1. A program intends to take a sequence of sentences from the user, 
 2. converts those sentences to title case and
 3. sort them descendingly
 
"""
print("Enter sentences. Use enter to start a new Sentece. Use double enter to quit inputing: \n")
lines = []
while True:
    line = input()
    if line: # if a user entere something
        lines.append(line) # add it in lines list
    else: # if user do not enter anything, we quit the entering process (Means, the user pressed enter twice)
        break

to_title_case= lambda sentence: sentence.title()  # This lambda function will take any string and turn it to title case
title_case=[to_title_case(line) for line in lines] # Convert all lines entered to title case using my lambda function above 
title_case.sort(reverse=True) # Sorting my sentences descendingly
converted_sentences='\n'.join(title_case) # Join all lines as a paragraph from their list

print("-------------OUTPUT--------------------\n")
print(f"{converted_sentences}\n") # showing the output