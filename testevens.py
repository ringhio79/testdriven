from byotest import *


def even_number_of_evens(numbers):
    number_of_evens = 0
    
    for n in numbers:
        if type(n) != int:
            continue
        if n % 2 == 0:
            number_of_evens += 1
    
    if number_of_evens == 0:
        return False
    
    return number_of_evens % 2 == 0
    
# assert_equal(even_number_of_evens([2,3,4]), True)
# assert_equal(even_number_of_evens([2,3,5]), False)
# assert_equal(even_number_of_evens([1,3]), False)
# assert_equal(even_number_of_evens([]), False)

assert_true(even_number_of_evens([2,3,4]))
assert_false(even_number_of_evens([2,3,5]))
assert_false(even_number_of_evens([1,3]))
assert_false(even_number_of_evens([]))
assert_false(even_number_of_evens(["Hello", "World"]))
assert_false(even_number_of_evens(["Hello", "World", "Hi"]))


print("OK")