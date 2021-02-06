# Dhruvin Bhayani
# 105170206

def palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(str)-i-1]:
            return False
    return True


#just for testing this function

# str = "racecar"
# print(palindrome(str))

# str = "python"
# print(palindrome(str))

# str = "madam"
# print(palindrome(str))