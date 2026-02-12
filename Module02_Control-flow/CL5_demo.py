### This template is for the class exercises covered in M02_L05_control-flow for CS 22B.

##### CL5.1 Boolean logic and evaluation
### Without running Python, determine the value (True or False) for each expression. What is your reasoning for each?
a = 4
b = 7
c = False

(a > 3 and b < 10) or c
not (a == 4 and b != 7)
(a >= 5) == (b <= 7)
(not c and a < b) or (a == b)


##### CL5.2 if-elif-else evaluation
### What will be the value of d?
val = 5
d = 1
if val != d:
    v = val/val-5
    d += val+3
elif -5 < d:
	y = 3+val+d
	y -= 3-val
else:
	x = 2
	d += 4+val
print(d)


##### CL5.3 if-elif-else 
### What is the value of result?
### Will the if statement raise an exception?
x = 0
y = 10

if x != 0 and y / x > 2:
    result = "A"
else:
    result = "B"
print(result)


##### CL5.4: While loop 
### What is the final value of total and n?
### Rewrite the loop so that it stops at exactly when total first exceeds 50

total = 0
n = 1

while total <= 50:
    total += n
    n += 1


##### CL5.5 Infinite loop
### This loop never terminates. Fix it so that the loop will terminate

s = 10

#while s > 0:
#    if s % 2 == 0:
#        continue
#    s -= 1


##### CL5.6 Dictionary comprehension and boolean filtering
### Given the words list below, write a dictionary comprehension that maps each word to its length only if the word contains the letter 'o'.

words = ["data", "logic", "loop", "condition", "flow", "python"]
wdict={}
for w in words:
    if "o" in w:
        wdict[w]:len(w)
print(words)

