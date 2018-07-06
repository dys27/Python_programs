#A strobogrammatic number is a number that looks the same when rotated 180 degree (looked at upside down).
def isStrobogrammatic(num):
        dic = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i = 0
        j = len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in dic:
                return False
            i += 1
            j -= 1
        return True
