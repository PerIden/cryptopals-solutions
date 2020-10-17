'''
Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it. 
'''

import set_1_ch_3
from binascii import unhexlify

def file_to_list(filename):
    '''
    Reads a filename and puts its contents separated by lines to a list.
    '''
    with open(filename) as file:
        data = file.readlines()
    return data

def make_rate_dic(common_chars):
    '''
    Outputs a dictionary used to rate strings.
    '''
    rate_dic = {} 
    highest_rating = len(common_chars)

    for i in range(highest_rating):
        rate_dic[common_chars[i]] = highest_rating - i #more common characters get higher scores
    return rate_dic

def xor_from_string(hex, rate_dic):
    '''
    Rates hex strings based on how "common" they look according to the rating dictionary.
    '''
    str_scores = {}
    hex_bytes = unhexlify(hex) #xor_against only accepts bytes
    for i in range(256):
        xord = set_1_ch_3.XOR_against(hex_bytes, i).decode("utf-8")
        str_scores[xord] = set_1_ch_3.rate(xord, rate_dic)
    return str_scores

def xor_in_list(list, rate_dic):
    '''
    Uses xor_from_string to find the most likely XOR from a list of hex strings.
    '''
    score_keep = {}
    for entry in list:
        str_scores = xor_from_string(entry.strip(), rate_dic)
        key_highest_score = max(str_scores, key=str_scores.get)
        value_highest_score = str_scores[key_highest_score]
        score_keep[key_highest_score] = value_highest_score
    return(max(score_keep, key=score_keep.get)) #returns the highest rated element in the dictionary

def main(filename):
    list = file_to_list(filename)
    common_chars = 'etaoinshrdlcumwf' #most used characters in the English language
    rate_dic = make_rate_dic(common_chars)
    return xor_in_list(list, rate_dic)
#print(main("4.txt")) #the name of the file containing the hex is "4.txt"
