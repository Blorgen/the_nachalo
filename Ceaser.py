# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:10:15 2020

@author: Blorgen
"""

def ceaser(text,number,code):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for letter in text:
        if code == 'encrypt':
            if letter not in alphabet:
                result += letter
            else:
                result += alphabet[(alphabet.find(letter) + number) % len(alphabet)]
        elif code == 'decrypt':
            if letter not in alphabet:
                result += letter
            else:result += alphabet[(alphabet.find(letter) - number) % len(alphabet)]
    return result

print(ceaser('Krz duh brx, pdq',3,'decrypt'))
