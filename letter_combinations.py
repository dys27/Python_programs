'''
Creates letter combinations of digits of a phone number.
1 corresponds to no letter.
'''

def letterCombinations(digits):
        letters = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result=[]
        if len(digits) == 0:
            return result
        for i in letters[(int(digits[0])-2)]:
            result.append(i)
        for j in digits[1:]:
            temp=[]
            for k in range(len(result)):
                for l in letters[int(j)-2]:
                    temp.append(result[k]+l)
            result=temp
        return result
