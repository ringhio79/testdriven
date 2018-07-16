# Write a function compare that accepts 2 values x and y.
# When x is less than y, the function returns -1.
# When x equals y, the function returns 0
# When x is greater than y, the function returns 1

def compare(x, y):
    if x < y:
        return -1
    if x == y:
        return 0
    else:
        return 1


    

assert compare(5, 10)== -1, "when x is less than y return -1"
assert compare(5, 5)== 0, "when x equals  y return 0"
assert compare(15, 10) == 1,  "when x is greater than y return 1"



print("ok")