#1.concatenated and replicated methods

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#output: ab ba aaaaa bbbb

#2. to know a specific character's ASCII/UNICODE code point value

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

#output: a=97 space=32

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#output:bd efg abd e e adf beg
for ch in "abc":
    print(chr(ord(ch) + 1), end='')
 
