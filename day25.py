import math

def is_prime(number):
    if number < 2:
        return False
    elif number==2:
        return True
    r_number = math.ceil(math.sqrt(number))
    for j in range(2, r_number + 1):
        if number % j == 0:
            return False
    return True

test_case = int(input())
for i in range(test_case):
    number = int(input())
    if is_prime(number):
        print("Prime")
    else:
        print("Not prime")
