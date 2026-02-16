### CS 22B Module 01 - Homework 1
### Name: Ali Alibrahimi

import re

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
clean_reads = []
bad_reads = []
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters.
with open("Module01_Essentials/adapter_reads.txt", "r", encoding="UTF-8") as file:
    pattern = re.compile(r"^[ATCG]+$", re.IGNORECASE)
    for line in file: # You can itterate through each line by just lopping through the file
        trimmed_seq = line[14:].strip().upper()
    ## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
    ## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file,  bad_reads.txt. 
        if re.search(pattern, trimmed_seq):
            clean_reads.append(trimmed_seq)
            with open("Module01_Essentials/clean_reads.txt", "a", encoding="UTF-8") as clean_file:
                clean_file.write(f"{trimmed_seq}\r")
        else:
            bad_reads.append(trimmed_seq)
            with open("Module01_Essentials/bad_reads.txt", "a", encoding="UTF-8") as bad_file:
                bad_file.write(f"{trimmed_seq}\r")
    ## 4. Print as output, the number of valid and invalid reads. 
    print(f"Number of valid reads: {len(clean_reads)}\nNumber of bad reads: {len(bad_reads)}")
    



##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read.
clean_read_lengths = [len(seq) for seq in clean_reads] 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length).
clean_read_gc = [((seq.count("G") + seq.count("C")) / len(seq)) * 100 for seq in clean_reads] 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.
tracker = 0
for v in clean_read_lengths:
    tracker += v
avg_read_length = tracker / len(clean_read_lengths)
print(f"Min Length of Valid Read: {min(clean_read_lengths)}\nMax Length of Valid Read: {max(clean_read_lengths)}\nAverage Length of Valid Read: {avg_read_length}")
gc_tracker = 0
for v in clean_read_gc:
    gc_tracker += v
avg_read_gc = gc_tracker / len(clean_read_gc)
print(f"GC% of Valid Reads: {round(avg_read_gc, 3)}")

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads.
base_counts = {base:seq.count(base) for base in ["A", "T", "C", "G"] for seq in clean_reads} 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).
product = 1
for count in base_counts.values():
    product *= count

#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure.
def nucl_perc(seq, nucl):
    count = seq.count(nucl)
    percentage = (count / len(seq)) * 100
    return round(percentage, 2)

## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.
assert nucl_perc("AATT", "A") == 50.00
assert nucl_perc("AATT", "G") == 0.00
assert nucl_perc("AAAA", "A") == 100.00

sequence = "TTATAAGCCGATTATAAGCCCGTAACCGGTTAG"
print(nucl_perc(sequence, "A"))

