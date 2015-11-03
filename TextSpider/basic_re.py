import re

secret_code = 'sadskfjdslkjfklsdjfxxIxxdajkldsjfkdjxxlovexxsdfsdkljfkdsxxyouxxsdfdsfsdf'

# a = 'xz123'
# b = re.findall('x...', a)
# print(b)

# a = 'xyxy123'
# b = re.findall('x*', a)
# print(b)

# b = re.findall('xx.*xx', secret_code)
# print b
# c = re.findall('xx.*?xx', secret_code)
# print c
# d = re.findall('xx(.*?)xx', secret_code)
# print d
# for each in d:
#     print each,

s = '''hdkfhksxxhello
xxkjdshkjfhsihxxworldxxkdshkfjhsk'''
e = re.findall('xx(.*?)xx', s, re.S)
print e

