'''

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
0x746865206b696420646f6e277420706c6179L


'''

def fixed_xor(hex1, hex2):
    '''
    Python has an in-built XOR operator, which outputs a decimal integer.
    We convert it to hex and put it in the proper format.
    '''
    return hex(hex1^hex2).rstrip("L").lstrip("0x")

#hex1 = 0x1c0111001f010100061a024b53535009181c
#hex2 = 0x686974207468652062756c6c277320657965
#print(fixed_xor(hex1,hex2))
