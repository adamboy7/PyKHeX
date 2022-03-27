from dex_Search import dex_Search
from item_Search import item_Search

def substruct_G(pokemon, item = 0, EXP = 0, friendship = 0, PP_Boost = 0, Internal_or_National = "National", generation = 3):
    # - - - Sanitize inputs - - -
    error = 0
    if dex_Search(pokemon) == None:
        print ("Invalid \"pokemon\" str/int:", pokemon)
        error = 1
    if item_Search(item) == None:
        print ("Invalid \"item\" str/int:", item)
        error = 1
    if type(EXP) != int:
        print ("Invalid \"EXP\" int:", EXP)
        error = 1
    if type(EXP) == int and EXP > 4294967295 or type(EXP) == int and EXP < 0:
        print ("\"EXP\" out of range 0 -> 4294967295:", EXP)
        error = 1
    if type(PP_Boost) != int and type(PP_Boost) != str:
        print ("Invalid \"PP_Boost\" int/str:", PP_Boost)
        error = 1
    if type(PP_Boost) == int and PP_Boost > 255 or type(PP_Boost) == int and PP_Boost < 0:
        print ("\"PP_Boost\" out of range 0 -> 255:", PP_Boost)
        error = 1
    if type(PP_Boost) == str and len(PP_Boost) != 4:
        print ("\"PP_Boost\" string length != 4:", PP_Boost)
        error = 1
    if type(PP_Boost) == str and len(PP_Boost) == 4:
        for character in PP_Boost:
            if character != "0" and character != "1" and character != "2" and character != "3":
                print ("Invalid int (0 -> 3):", character, "in \"PP_Boost\" string", PP_Boost)
                error = 1
    if type(friendship) != int:
        print ("Invalid \"friendship\" int:", friendship)
        error = 1
    if type(friendship) == int and friendship > 255 or type(friendship) == int and friendship < 0:
        print ("\"friendship\" int out of range 0 -> 255:", friendship)
    if Internal_or_National.lower() != 'national' and Internal_or_National.lower() != 'internal':
        print ("Invaid \"Internal_or_National\" str:", Internal_or_National)
        error = 1
    if error == 1:
        print ("Input: substruct_G(" + str(pokemon) + ", " + str(item) + ", " + str(EXP) + ", " + str(friendship) + ", " + str(PP_Boost) + ", " + str(Internal_or_National) + str(generation) + ")")
        return None
    # - - - Done sanitizing inputs - - -
    exp_Little = str()
    for EXP_Byte in (EXP.to_bytes(4, 'little')):
        exp_Little = exp_Little + hex(EXP_Byte)[2:].zfill(2)
    if type(PP_Boost) == str:
        PP_Str = PP_Boost[3] + PP_Boost[2] + PP_Boost[1] + PP_Boost[0]
    if type(PP_Boost) == int:
        PP_Str = hex(PP_Boost)[2:].zfill(2)
    return (dex_Search(pokemon, Internal_or_National)[1].upper() + item_Search(item, generation) + exp_Little.upper() + PP_Str.upper() + hex(friendship)[2:].zfill(2).upper() + "0000")
