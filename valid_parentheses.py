#Check for valid parenthesis

def isValid(s):
        dictionary = {'(':')','[':']','{':'}'}
        temp=[]
        for i in s:
            if i in dictionary.keys():
                temp.append(i)
            elif len(temp)!=0 and (dictionary[temp[-1]]==i):
                temp.pop(i)
            else:
                return False
        return len(temp)==0
