# -*- coding: UTF-8 -*-
from Dictionaries.international_Characterset import *
from Dictionaries.japanese_Characterset import *

international_Strings = ["international", "english", "0202", "french" "0203", "italian", "0204", "german", "0205", "spanish", "0207"]
japanese_Strings = ["japanese", "0201"]

def translate(string, byte_Length = None, language = "International", smart_Character = True):
    # - - - Sanitize inputs - - -
    error = 0
    if type(string) != str: #Why would you pass a number? I guess you can do that if you want..?
        string = str(string)
    if byte_Length != None and type(byte_Length) != int:
        print ("Invalid \"byte_Length\" int:", byte_Length)
        error = 1
    if type(language) != str or language.lower() not in international_Strings and language.lower() not in japanese_Strings:
        print ("Invalid \"language\" string:", language)
        error = 1
    if smart_Character != True and smart_Character != False:
        print ("Invalid \"smart_Character\" bool:", smart_Character)
        error = 1
    if error == 1:
        print ("Input: translate(" + str(string) + ", " + str(byte_Length) + ", " + str(language) + ", " + str(smart_Character) + ")")
        return None
    # - - - Done sanitizing inputs - - -
    string_Hex = str()
    string_Position = 0
    apostrophe = 0
    quote = 0
    for character in string:
        if language.lower() in international_Strings:
            if character == "*":
                string_Position = string_Position + 1
                if (string[(string_Position - 1):(string_Position + 2)]) not in character_Encoding_International_Special:
                    print ('Invalid character', string[(string_Position - 1):(string_Position + 2)], 'found, setting ▯!')
                    string_Hex = string_Hex + character_Encoding_International["▯"]
                    continue
                string_Hex = string_Hex + character_Encoding_International_Special[string[(string_Position - 1):(string_Position + 2)]]
                print (string[(string_Position - 1):(string_Position + 2)])
                continue
            if string_Position >= 1 and string[(string_Position - 1)] == "*" or string_Position >= 2 and string[(string_Position - 2)] == "*":
                string_Position = string_Position + 1
                continue
            if character == "\"" and smart_Character == True:
                string_Position = string_Position + 1
                if quote == 0:
                    string_Hex = string_Hex + character_Encoding_International["“"]
                    quote = 1
                    continue
                if quote != 0:
                    string_Hex = string_Hex + character_Encoding_International["”"]
                    quote = 0
                    continue
            if character == "\'" and smart_Character == True:
                string_Position = string_Position + 1
                if apostrophe == 0:
                    string_Hex = string_Hex + character_Encoding_International["‘"]
                    apostrophe = 1
                    continue
                if apostrophe != 0:
                    string_Hex = string_Hex + character_Encoding_International["’"]
                    apostrophe = 0
                    continue
            if character not in character_Encoding_International:
                print ('Invalid character', character, 'found in international character set, setting ▯!')
                string_Hex = string_Hex + character_Encoding_International["▯"]
                string_Position = string_Position + 1
                continue
            string_Hex = string_Hex + character_Encoding_International[character]
            string_Position = string_Position + 1
        if language.lower() in japanese_Strings:
            if character == "*":
                string_Position = string_Position + 1
                if (string[(string_Position - 1):(string_Position + 2)]) not in character_Encoding_Japanese_Special:
                    print ('Invalid character', string[(string_Position - 1):(string_Position + 2)], 'found, setting as space!')
                    string_Hex = string_Hex + character_Encoding_Japanese[" "]
                    continue
                string_Hex = string_Hex + character_Encoding_Japanese_Special[string[(string_Position - 1):(string_Position + 2)]]
                print (string[(string_Position - 1):(string_Position + 2)])
                continue
            if string_Position >= 1 and string[(string_Position - 1)] == "*" or string_Position >= 2 and string[(string_Position - 2)] == "*":
                string_Position = string_Position + 1
                continue
            if character not in character_Encoding_Japanese:
                print ('Invalid character', character, 'found in international character set, setting as space!')
                string_Hex = string_Hex + character_Encoding_Japanese[" "]
                string_Position = string_Position + 1
                continue
            string_Hex = string_Hex + character_Encoding_Japanese[character]
            string_Position = string_Position + 1
    if byte_Length != None:
        while len(string_Hex) < (byte_Length * 2):
            string_Hex = string_Hex + "FF"
        return string_Hex[:(byte_Length * 2)]
    return string_Hex
