# Dhruvin Bhayani
# 105170206

def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


#just for testing this function

# str = "racecar"
# print(palindrome(str))

# str = "python"
# print(palindrome(str))

# str = "madam"
# print(palindrome(str))