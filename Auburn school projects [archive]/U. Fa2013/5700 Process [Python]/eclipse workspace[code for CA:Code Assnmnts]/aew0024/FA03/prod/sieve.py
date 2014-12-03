import math
        
        # CITATION: Sieve of Eratosthenes
        # Create list of all numbers up to max
        # Start with first prime
        # Strike all multiples 
        # repeat for next un-struck number in list


#this is the driver method for determining the primality of numbers within a certain range
#
#PARAM: The ceiling to the range of numbers for which you want all primes
#RETURNS: the list of primes in that range, after calling all associated methods in correct order
def determinePrimality(ceilingOfNumbersToTest):

    if ceilingOfNumbersToTest < 2: #if the ceiling is less than 2, then there are no primes to display (0 and 1 are not prime) 
        return []
    else:
        #set up initial matrix
        originalListOfNumbers = buildListOfNumbersForTesting(ceilingOfNumbersToTest)
        countOfPrimesAfterCheckingRange = determinePrimesAndComposites(originalListOfNumbers)
        return buildOutputListOfPrimes(countOfPrimesAfterCheckingRange, originalListOfNumbers)
        
#Given a ceiling to a range of numbers, instantiates a list/matrix of boolean values to help
# with further Sieve of Eratosthenes processing. The first two values in the list -- 0 and 1 --
# are treated as non-prime, and as such are marked as false. All other values are marked as true,
# and as such will be tested with methods later in the sequence.
#
#PARAM: the ceiling of the range of numbers that must be tested
#RETURNS: the initialized list of numbers with corresponding TRUE values in all but first two slots
def buildListOfNumbersForTesting(ceilingOfNumbersToTest):
    listOfNumbers = [False, False] #marks 0 and 1 as false -- i.e., NOT as primes
    currentIterationOfLoop = 1 #Iteration zero is a valid iteration, consistent with indices in Python
    while currentIterationOfLoop < ceilingOfNumbersToTest + 1: #for the rest of the numbers
        listOfNumbers.append(True)
        currentIterationOfLoop = currentIterationOfLoop + 1
        
    return listOfNumbers

#From a given initialized list indicating the range of numbers to be tested,
# determines which are primes and which are composites, 
# storing FALSE at the index of a non-prime, and TRUE at the index of a prime
#
#PARAMETER: the list, with each entry initialized to TRUE (except for the initial two elements!
#RETURNS: the total count of primes determined from the input list of numbers        
def determinePrimesAndComposites(originalListOfNumbers):
    #mark out all multiples, leaving the primes as FALSE, and determine count of primes
    
    ceilingOfNumbersToTest = originalListOfNumbers.__len__() - 1
    
    countOfPrimesAfterCheckingRange = ceilingOfNumbersToTest - 2 #we will decrement this number every time
    for currentIndexInTotalRange in range(2, int(math.sqrt(ceilingOfNumbersToTest) + 1)): #
        if originalListOfNumbers[currentIndexInTotalRange]: #
            firstMultipleToCheck = 2 * currentIndexInTotalRange
            for multipleOfPrime in range(firstMultipleToCheck, ceilingOfNumbersToTest, currentIndexInTotalRange): #must set the multiples of the prime as NOT PRIME -- false
                if originalListOfNumbers[multipleOfPrime]:
                    originalListOfNumbers[multipleOfPrime] = False
                    countOfPrimesAfterCheckingRange = countOfPrimesAfterCheckingRange - 1 #
        #all multiples should have been set as prime -- FALSE -- while primes remain as TRUE
        #we should also have a count of the number of primes available to us, which we will return
    return countOfPrimesAfterCheckingRange

#From a given list of numbers, with each index properly set to indicate prime (TRUE) or not prime (FALSE),
# builds a list of the primes in that range of numbers (it must know the count of primes available).
# This list of primes will be the return value.
#
#PARAM 1:countOfPrimesAfterCheckingRange: The number of primes in the input list of numbers, determined in a previous step
#PARAM 2:originalListOfNumbers: The input list of numbers, indicating the range of numbers to be checked as well as what is or isn't prime
#RETURNS: a list of primes in the given range of numbers
def buildOutputListOfPrimes(countOfPrimesAfterCheckingRange, originalListOfNumbers):
    
    ceilingOfNumbersToTest = originalListOfNumbers.__len__() - 1 #done to de-couple the methods a bit from one another
    
    #create an empty list into which we will store
    finalListOfPrimes = [] #create empty list...
    currentIterationOfLoop = 0 #Iteration zero is a valid iteration, consistent with indices in Python
    while currentIterationOfLoop < countOfPrimesAfterCheckingRange: #...and for all the numbers...
        finalListOfPrimes.append(0) #...add a zero, one by one, to instantiate the array of primes
        currentIterationOfLoop = currentIterationOfLoop + 1
    #the array should now be instantiated with zeroes

    indexInfinalListOfPrimes = 0 #
    for eachNumberInTheOriginalRange in range (0, ceilingOfNumbersToTest): #
        if originalListOfNumbers[eachNumberInTheOriginalRange]: #
            finalListOfPrimes[indexInfinalListOfPrimes] = eachNumberInTheOriginalRange #
            indexInfinalListOfPrimes = indexInfinalListOfPrimes + 1 #
            
    return finalListOfPrimes #return the list of primes


if __name__ == '__main__':
    userInput = int(raw_input("input a value "))    
    print "The primes are "
    print determinePrimality(userInput)

                
