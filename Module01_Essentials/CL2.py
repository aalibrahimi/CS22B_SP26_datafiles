### This template is for the class exercises covered in M01_L02_review-files for CS 22B.
import re

## root folder if applicable
# root='/path/to/folder/'

##### CL1.1: Count the number of T in the sequence.
sequence = "ATTGGCTATACCGG"
t_count = sequence.count("T")
# Can also do ( to be safer ): sequence.lower().count("t")
print(f"[ CL1.1 ]: T Appears: {t_count} times")


##### CL1.2: For the sequence above, convert the sequence from the 4th character to the 9 character to lower case
search_string = sequence[3:9]
pattern = fr"{search_string}"
adjusted_seq = re.sub(pattern, search_string.lower(), sequence)
print(f"[ CL1.2 ]: New Sequence: {adjusted_seq}")


##### CL1.3: Find the noncoding(4th to 9th character) and coding regions(all other characters)
## step 1: open the seq.txt file
with open("seq.txt", "r", encoding="UTF-8") as seq_file:
    seq = seq_file.read()
    
    search_string = seq[3:9]
    pattern = fr"{search_string}"
    adjusted_seq = re.sub(pattern, search_string.lower(), seq)
    seq_file.close()

## step 2: create 2 new files for coding and noncoding
## write to new files sequence 4-9 as lowercase to noncode file and all other sequence as uppercase to code file. Don't forget to close() to save the files.
with open("coding_seq.txt", "w", encoding="UTF-8") as coding_file:
    code_seq = "".join([s if s.isupper() else "" for s in adjusted_seq])
    coding_file.write(code_seq)
    coding_file.close()

with open("noncoding_seq.txt", "w", encoding="UTF-8") as noncoding_file:
    noncoding_file.write(search_string.lower())
    noncoding_file.close()
    
print("[ CL1.3 ]: Complete")


##### CL1.4: Trim the adapter sequence (14 bp seq at front of each line “ATTCGATTATAAGC”)
## step 1: open the adapter_input.txt file
seq_remains: list[str] = []
with open("adapter_input.txt", "r", encoding="UTF-8") as adapt_file:
    for seq in adapt_file.readlines():
        seq_remains.append(seq[14:])
    
    adapt_file.close()

## step 2: create an output file
## step 3: read in each line in the adapter_input file and trim the first 14 characters. Write the remaining sequence to the output file. Do this for each line. Don't forget to close() to save the file.
with open("trimmed_adapter.txt", "w", encoding="UTF-8") as trimmed_file:
    for seq in seq_remains:
        trimmed_file.write(seq)
        
    trimmed_file.close()
    
print("[ CL1.4 ]: Complete")