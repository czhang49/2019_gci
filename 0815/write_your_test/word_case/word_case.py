def isupper(input_string):
    for char in input_string:
        if char.islower():
            return False
    return True

def islower(input_string):
    for char in input_string:
        if char.isupper():
            return False
    return True

def ismixed(input_string):
    for char in input_string:
        if char.isupper():
            return False
    return True
