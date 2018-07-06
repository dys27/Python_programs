#checks if a number is a power of 2 or not

def isPowerOfTwo(n):
        if n==1 or n==2:
            return True
        elif n<1:
            return False
        else:
            while n%2==0:
                n=n/2
                if n==2:
                    return True
            return False
