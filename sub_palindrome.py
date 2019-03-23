"""Sub palindrome."""

s = input('Enter the string \n').lower().strip()

for i in range(len(s)):
    tmp = ''
    for j in range(i, len(s)):
        tmp += s[j]
        if len(tmp) > 1 and tmp == tmp[:: -1]:
            print(tmp, ' palindrome')
