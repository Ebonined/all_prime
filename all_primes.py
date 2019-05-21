def allprimes(number=997):
    """
    Function to help get all the prime number from 1 to the intended number in the function
    """
    oddnum = [2]
    for num in range(2,number+1):
        if num%2 != 0:
            oddnum.append(num)

    size = len(oddnum)-1 # lenght of the list oddnum-1

    for num in oddnum:
        templist = []
        for div in oddnum:
            if num != div and num%div != 0:
                templist.append(num)
        if len(templist) == size: # runs is the number is not divided as much as the number of times of the size variable
            yield templist[0]    # appends that number to the list

def primfact(number):
    """
    #----example-----#
    print(primfact(55))

    #----outputs-----#
    {5: 1, 11: 1} # equivalent to 5^1*11^1
    """
    from collections import Counter
    primefactlist =[]
    check = 0
    g = allprimes(number)

    while number != 1:
        if check == 0:
            divider = next(g)
            check = 1
        if number%divider != 0:
            check = 0
            continue
        number /= divider
        primefactlist.append(divider)
    
    countprime = Counter(primefactlist)
    indexnot = dict(countprime)
        
    return indexnot # returns a dictionary in which the keys are the prime numbers and the values are the power of the index notation
            
#----example-----#
# print(primfact(55))

#----outputs-----#
# {5: 1, 11: 1} # equivalent to 5^1*11^1