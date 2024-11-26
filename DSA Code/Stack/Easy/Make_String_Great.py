# https://leetcode.com/problems/make-the-string-great/
#
# time-O(n)
# space-O(n)
#
# Code:
# (Using Stack)
def makeGood(self, s: str) -> str:
    stack = []
    for letter in s:
        if stack and abs(ord(stack[-1]) - ord(letter)) == 32:
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)