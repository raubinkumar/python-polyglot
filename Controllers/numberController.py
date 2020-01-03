from Helpers.numberHelper import is_number_two_sided_prime, is_prime_number
from Models.numberDetails import numberdetails

def number_details(num):
    #Just for learning to set the values in model.
    details = numberdetails(num)
    details.isPrime = is_prime_number(num)
    details.isEven = num % 2 == 0
    details.isTwoSidedPrime = is_number_two_sided_prime(num)
    return details.__dict__
    
def is_two_sided_prime(num):
    return is_number_two_sided_prime(num)
