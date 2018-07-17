

def assert_equal(a,b):
    assert a == b, "Expected {0} and {1} to be the same, but they were different".format(a, b)
    
    
def assert_true(a):
    assert a, "not true"
    
def assert_false(a):
    assert not a, "not false"
    