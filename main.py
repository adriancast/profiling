from sieve import * # Contains the sieve algorithms

PRIME_NUMBERS = 9999

def main(argv):
    print "Doing profiling searching "+str(PRIME_NUMBERS)+" prime numbers"
    print "Starting fast_sieve..."
    fast_sieve(PRIME_NUMBERS)
    print "DONE"
    print "Starting medium_sieve..."
    medium_sieve(PRIME_NUMBERS)
    print "DONE"
    print "Starting slow_sieve..."
    slow_sieve(PRIME_NUMBERS)
    print "DONE"
    pass

if __name__ == "__main__":
    main(sys.argv)


