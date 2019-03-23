"""Check if a string palindrome."""

s = input('Enter a string \n').lower().strip()

if s == s[::-1]:
    print(s, ' is palindrome.')
else:
    print(s, ' is not palindrome.')
