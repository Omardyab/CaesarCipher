"""to import download it using this command => pip3 install -U nltk"""
import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()

""" Refered to this https://www.w3schools.com/charsets/ref_html_ascii.asp """
def encrypt(text,key): 
    encrypted_text=""
    for char in text: 
        char_num=ord(char)
        if char.isupper():
            encrypted_text += chr((char_num + key-65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((char_num + key-97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text
        
def decrypt(encrypted, key):
    return encrypt(encrypted,-key)

def count_words(txt):
    words = txt.split()
    counter = 0 
    for word in words:
        exisitng_word = re.sub(r'[^A-Za-z]+','', word)
        if exisitng_word.lower() in name_list or exisitng_word in word_list:
            counter += 1
    return counter

def crack(encrypted_txt):
    length=len(encrypted_txt.split())
    decrypt_word="the percentage was less than 50%"
    for i in range(length):
        decrypted = decrypt(encrypted_txt, i)
        word_count = count_words(decrypted)
        # print("words are now ",word_count)
        length_decrypted=len(decrypted.split())
        # print("len of dec",length_decrypted)
        perc = int(word_count / length_decrypted * 100)
        # print("percentage is ",perc)
        if perc > 50:
            decrypt_word = decrypted
    return decrypt_word

if __name__ == "__main__":
    txt=encrypt("It was the best of times, it was the worst of times",7)
    print(txt)
    decrtxt=decrypt(txt,3)
    print(decrtxt)
    cwords=count_words("It was the best of times, it was the worst of times")
    print(cwords)
    cwords2=count_words(decrtxt)
    print(cwords2)
    print(crack(decrtxt))

