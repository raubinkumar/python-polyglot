def is_prime_number(num):
    is_prime = False
    if num > 1:
        # check for factors
        for i in range(2, num//2 + 1):
            if (num % i) == 0:
                is_prime = False
                break
        else:
            is_prime = True
    else:
        is_prime = False
    return is_prime

def is_number_two_sided_prime(num):
    num_str = str(num)
    two_sided_prime = is_prime_number(num)
    for i in range(1, len(num_str)):
        if(two_sided_prime and (not is_prime_number(int(num_str[i:])) or not is_prime_number(int(num_str[:i])))):
            two_sided_prime = False 
            break
    
    return two_sided_prime
