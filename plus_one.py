#Given a non-empty array of digits representing a non-negative integer, add plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list,
#and each element in the array contain a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.
def plusOne(digits):
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1
            if digits[i]%10==0:
                digits[i]=0
                continue
            else:
                return digits
        digits=[1]+[0]*len(digits)
        return digits
