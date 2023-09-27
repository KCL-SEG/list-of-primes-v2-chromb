"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be greater than 0") #Raise error if invalid input
    
    elif number_of_primes == 1: #Weird edge case if only one.
        return [2]

    else:  
        list = [2]  #Initialize list with 2 in it
        numberToCheck = 2 #Variable to track the number that we're currently checking
        while len(list)<number_of_primes:
            numberToCheck += 1
            isPrime = True #Bool used to track if the number has been found as divisible
            for i in range(2,numberToCheck): #check all numbers between 2 and the number we're checking to see if there's any divisors
                if numberToCheck % i == 0:
                    isPrime = False
            if isPrime == True: #If the number is prime, add it to the list
                list.append(numberToCheck)
    return list
