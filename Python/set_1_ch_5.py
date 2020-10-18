'''
Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
'''
from binascii import hexlify, unhexlify
def repeating_key_xor(plain, key):
    '''
    Applies repeated-key XOR on 'plain' with 'key' and outputs the hex representaiton.
    '''
    plainbytes = bytes(plain, "utf-8")
    i=0
    cipher = ""
    for byte in plainbytes:
        cipher += chr(byte^ord(key[i%3]))
        i += 1
    return hexlify(bytes(cipher, "utf-8"))

if __name__ == '__main__':
    print(repeating_key_xor("Burning 'em, if you ain't quick and nimble" + "\n" + "I go crazy when I hear a cymbal", "ICE"))
