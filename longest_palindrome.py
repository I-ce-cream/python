def longest_palindrome (s):
    string = []
    get_str = ""
    for i,c in enumerate(s):
        get_str += c
        if get_str[::-1] in s:
            string.append(get_str)
        else:
            get_str = ""+c
    string = sorted(string,key = lambda i:len(i) , reverse = True)
    for x in string:
        result = x[::-1]
        if result == x :return len(s)
        if s.index(result) - s.index(x) == len(x)-1:
            return len(s)*2-1
        if s.index(result) - s.index(x) == len(x):
            return len(s)*2
        if s.index(result) - s.index(x) == len(x)+1:
            return len(s)*2+1
    return 0

longest_palindrome("baa")

'''
def longest_palindrome(s):
    for c in xrange(len(s), -1, -1):
        for i in xrange(len(s) - c + 1):
            if s[i:i + c] == s[i:i + c][::-1]:
                return c

def longest_palindrome (s):
    longest = 0
    for left in xrange(len(s)):
        for right in xrange(len(s), left, -1):
            if s[left:right] in (s[left:right])[::-1]:
                longest = max(right-left, longest)
                break
    return longest
'''

