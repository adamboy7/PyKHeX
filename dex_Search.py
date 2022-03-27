from Dictionaries.dex_National import *
from Dictionaries.dex_Internal import *

def dex_Search(ID, Internal_or_National = "National", return_Upper = False):
    # - - - Sanitize inputs - - -
    error = 0
    if type(ID) != int and type(ID) != str:
        print ("Invalid ID str/int:", ID)
        error = 1
    if Internal_or_National.lower() != 'national' and Internal_or_National.lower() != 'internal':
        print ("Invaid \"Internal_or_National\" str:", Internal_or_National)
        error = 1
    if return_Upper != True and return_Upper != False:
        print ("Invalid \"return_Upper\" bool:", return_Upper)
        error = 1
    if error == 1:
        print ("Input: dex_Search(" + str(ID) + ", " + str(Internal_or_National) + ", " + str(return_Upper) + ")")
        return None
    # - - - Done sanitizing inputs - - -
    if Internal_or_National.lower() == 'national':
        try:
            if type(ID) == int:
                if return_Upper == False:
                    return dex_National[ID], hex(ID.to_bytes(2, "little")[0])[2:].zfill(2).upper() + hex(ID.to_bytes(2, "little")[1])[2:].zfill(2).upper()
                if return_Upper == True:
                    return dex_National[ID].upper(), hex(ID.to_bytes(2, "little")[0])[2:].zfill(2).upper() + hex(ID.to_bytes(2, "little")[1])[2:].zfill(2).upper()
            if type(ID) == str:
                if return_Upper == False:
                    return dex_National[dex_National[ID.upper()]], hex(dex_National[ID.upper()].to_bytes(2, "little")[0])[2:].zfill(2).upper() + hex(dex_National[ID.upper()].to_bytes(2, "little")[1])[2:].zfill(2).upper()
                if return_Upper == True:
                    return dex_National[dex_National[ID.upper()]].upper(), hex(dex_National[ID.upper()].to_bytes(2, "little")[0])[2:].zfill(2).upper() + hex(dex_National[ID.upper()].to_bytes(2, "little")[1])[2:].zfill(2).upper()
        except:
            if type(ID) == str:
                print ("Invalid pokemon str:", ID)
            if type(ID) == int:
                print ("Invalid pokemon national ID:", ID)
            return None
    if Internal_or_National.lower() == 'internal':
        try:
            if type(ID) == int:
                if return_Upper == False:
                    return dex_National[ID], dex_Internal[ID]
                if return_Upper == True:
                    return dex_National[ID].upper(), dex_Internal[ID]
            if type(ID) == str:
                if return_Upper == False:
                    return dex_National[dex_National[ID.upper()]], dex_Internal[ID.upper()]
                if return_Upper == True:
                    return dex_National[dex_National[ID.upper()]].upper(), dex_Internal[ID.upper()]
        except:
            if type(ID) == str:
                print ("Invalid pokemon str:", ID)
            if type(ID) == int:
                print ("Invalid pokemon national ID:", ID)
            return None
