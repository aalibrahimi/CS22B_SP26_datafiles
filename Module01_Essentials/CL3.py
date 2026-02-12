### This template is for the class exercises covered in M01_L03_review-objects for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL3.1: List comprehension. Given:
NL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## Write a list comprehension to collect the diagonal items from matrix NL
# Enumerate: [(0, [1, 2, 3]), (1, [4, 5, 6]), (2, [7, 8, 9])]
diag = [item[idx] for (idx, item) in enumerate(NL)]
print(diag)

##### CL3.2: Using my_list, create a list of tuples where tuple is (n, n**3) where n is each number in the list.
my_list = [1, 2, 3, 4, 5]
new_list = [(n, n**3) for n in my_list]
print(new_list)



##### CL3.3: Multiple all the values of the items in a dictionary 
num_dict = {'num1':100, 'num2':346, 'num3':-24}
res = 1
for n in num_dict.values():
    res *= n

print(res)
