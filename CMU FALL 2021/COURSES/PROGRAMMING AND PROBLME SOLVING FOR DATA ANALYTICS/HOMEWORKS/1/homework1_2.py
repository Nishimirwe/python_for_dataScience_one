"""
Author: Jean Paul Nishimirwe
Andrew Id: jnishimi
Date Created: On 14th Sept 2021

About a program
-----------------
1. A program takes comma-separated numbers and keep them in a list and a tuple
2. A program displays alist and a tuple with those numbers.
3. A program sort numbers in a list and tuple respectively and print sorted list and tuple
4. A program dipslays the smallest and the largest value in a list
5. A program displays pair of numbers in a list

For example:
INPUT:
-----
Enter comma separated numbers:
3,2,5


OUTPUT
------
List: [3, 2, 5]
Tuple: (3, 2, 5)
Sorted List: [2, 3, 5]
Sorted Tuple: (2, 3, 5)
Pairs: ({2,3},{2,5},{3,5})

Min: 2
Max: 5
Avg: 3.3333333333333335

"""

values=input("Enter comma separated numbers: \n")
value_list=[int(i) for i in values.split(",")]
value_tuple=tuple(value_list)

print(f"List: {value_list}")
print(f"Tuple: {value_tuple}")


# Print Sorted
#  sort a list, use .sort() function
value_list.sort()
print(f"Sorted List: {value_list}")


#  sorting a tuple, use of sorted(tuple) function
value_tuple=tuple(sorted(value_tuple))
print(f"Sorted Tuple: {value_tuple}")


# Generate a pair of numbers and print those pairs.
print("Pairs: (", end='')
for i in range(len(value_list)):
    for j in range(i+1,len(value_list)):
        print("{"+str(value_list[i])+","+str(value_list[j])+"}",end='')
        if(i+1 != len(value_list)-1):
            print(",",end='')
        
print(")")
print()


#  Print Min, Max, and Average
print(f"Min: {min(value_list)}") # Min
print(f"Max: {max(value_list)}") # Max
print(f"Avg: {sum(value_list)/len(value_list)}") # Average
