### CS 22B Module 02 - Homework 2
### Name: Ali Alibrahimi

##### Homework practicing Control flow and Regular expression #####

## Import library
import re

##### Problem 1 - if/elif/else
## You are given a list of log lines. Classify each line into one of these buckets:
## - "ERROR": contains ERROR and an error code like E1234
## - "WARN": contains WARN and a module tag in brackets like [auth]
## - "INFO": contains INFO and a user id like user=ab_12
## - "SKIP": anything else
## Return a dictionary with counts per bucket.

lines = [
    "2026-02-11 10:00:01 ERROR E1042 [db] user=ab_12 msg=timeout",
    "2026-02-11 10:00:02 WARN [auth] user=xy_77 msg=bad password",
    "2026-02-11 10:00:03 INFO user=ab_12 msg=login ok",
    "2026-02-11 10:00:04 ERROR [api] msg=missing code",
    "garbage line"
]

### step 1: Define the count variables
error_count = re.compile(r"\bERROR\b.*\b(E\d{4})\b")
warn_count = re.compile(r"WARN.*(\[\w+\])")
info_count = re.compile(r"INFO.*user=(\w+)")

### step 2: Initialize the count dictionary
counts = {"ERROR": 0, "WARN": 0, "INFO": 0, "SKIP": 0}

### step 3: Loop throught the dictionary with if-elif-else
for line in lines:
    if error_count.search(line):
        counts["ERROR"] += 1
    elif warn_count.search(line):
        counts["WARN"] += 1
    elif info_count.search(line):
        counts["INFO"] += 1
    else:
        counts["SKIP"] += 1

print(counts)

##### Problem 2 - Check passwords with boolean logic and regex
## Write a function check_password(pw) that returns one of:
# "STRONG" if:
# - length ≥ 10
# - contains at least 1 lowercase, 1 uppercase, 1 digit, 1 symbol from !@#$%^&*
# - does not contain whitespace
# otherwise "WEAK"
## Test the function on a list of passwords using a loop

test_pw = ["Short7!", "LongerPass7!", "GoodPassw0rd!", "Bad Passw0rd!",
           "N0SymbolHereAAA"]

### step 1: Define variables
strong_pattern = re.compile(r"([A-Z])?(?(1)[a-z]|[A-Z])+\w+[!@#$%^&*]+")
whitespace_pattern = re.compile(r"\s")

### step 2: Write a function that check password (str) to test cases
def check_password(password):
    strong = (len(password) >= 10 and strong_pattern.search(password)
              is not None and not whitespace_pattern.search(password))
    return "STRONG" if strong else "WEAK"


### step 3: Use case. Test list test_pw
for pw in test_pw:
    print(check_password(pw))
