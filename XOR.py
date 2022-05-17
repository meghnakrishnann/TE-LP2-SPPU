str = 'HelloWorld';

result = ''.join(format(ord(x), '08b') for x in str)

val = '1111111';

y = int(result,2) ^ int(val,2)

print('{0:b}'.format(y))
