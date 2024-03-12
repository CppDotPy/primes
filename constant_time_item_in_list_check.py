from pyon import pyon

# a test to see if i can make an algorithem to check if
# an item is in a list in constant time

class special_list:

    variables = pyon('primes.pyon')
    primes = variables.primes.content
    
    def __init__(self):
        
        self.tracker = 1
        self.internal_list = []

    def append(self, number):
    
        if type(number) != int: raise TypeError('lol no')
        self.tracker *= special_list.primes[number]
        self.internal_list.append(number)
        return self.tracker

    def __contains__(self, value):

        if self.tracker % special_list.primes[value] == 0: return True
        else: return False

