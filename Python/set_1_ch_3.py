'''
Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
'''
from binascii import unhexlify

def XOR_against(string, char):
    '''
    Input byte type and character. Output the XOR.
    '''
    xord = ""
    for byte in string:
        xord += chr(byte ^ char)
    return bytes(xord, 'utf-8')

def rate(xord, rate_dic):
    '''
    This function outputs an int based on the "score" that the rate_dic assigns it.
    '''
    score = 0
    for char in xord:
        score += rate_dic.get(char, 0) #if char isn't in dic, return 0.
    return score

def main(b):
     
    common_chars = 'etaoinshrdlcumwf' #most used characters in the English language
    rate_dic = {} 
    str_scores = {}
    highest_rating = len(common_chars)

    for i in range(highest_rating):
        rate_dic[common_chars[i]] = highest_rating - i #more common characters get higher scores
    for i in range(256): #xor against all ASCII chars
        xord = XOR_against(b, i).decode("utf-8")
        str_scores[xord] = rate(xord, rate_dic) #adds the score of xord to the key xord
    return max(str_scores, key=str_scores.get)

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
b = unhexlify(s)
print(main(b))

