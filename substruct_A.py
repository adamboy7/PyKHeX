from Dictionaries.attacks_I import attacks_I
from Dictionaries.attacks_II import attacks_II
from Dictionaries.attacks_III import attacks_III
from Dictionaries.attacks_IV import attacks_IV
from Dictionaries.attacks_V import attacks_V
from Dictionaries.attacks_VI import attacks_VI
from Dictionaries.attacks_VII import attacks_VII
from Dictionaries.attacks_VIII import attacks_VIII

generations_List = [1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII"]
roman_Dict = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8}
_attack_dicts = {
    1: attacks_I, 2: attacks_II, 3: attacks_III, 4: attacks_IV,
    5: attacks_V, 6: attacks_VI, 7: attacks_VII, 8: attacks_VIII,
}

def substruct_A(attack1, attack1_PP = 0, attack2 = None, attack2_PP = 0, attack3 = None, attack3_PP = 0, attack4 = None, attack4_PP = 0, generation = 3):
    output_attack = str()
    output_PP = str()
    error = 0
    if generation not in generations_List:
        print ("Invalid \"generation\" int/str:")
        error = 1
    if type(generation) == str: # supplied generation was a roman numeral, convert to a number for math.
        generation = roman_Dict[generation]
    attack_dict = _attack_dicts[generation]
    if type(attack1_PP) != int or attack1_PP > 255 or attack1_PP < 0:
        print ("Invalid PP count on attack 1", "\"" + str(attack1_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack2_PP) != int or attack2_PP > 255 or attack2_PP < 0:
        print ("Invalid PP count on attack 2", "\"" + str(attack2_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack3_PP) != int or attack3_PP > 255 or attack3_PP < 0:
        print ("Invalid PP count on attack 3", "\"" + str(attack3_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack4_PP) != int or attack4_PP > 255 or attack4_PP < 0:
        print ("Invalid PP count on attack 4", "\"" + str(attack4_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if attack1 != None and attack1 not in attack_dict:
        print ("Invalid attack 1:", attack1)
        error = 1
    if attack2 != None and attack2 not in attack_dict:
        print ("Invalid attack 2:", attack2)
        error = 1
    if attack3 != None and attack3 not in attack_dict:
        print ("Invalid attack 3:", attack3)
        error = 1
    if attack4 != None and attack4 not in attack_dict:
        print ("Invalid attack 4:", attack4)
        error = 1
    if error == 1:
        print ("Input: substruct_A(" + str(generation) + ", " + str(attack1) + ", " + str(attack1_PP) + ", " + str(attack2) + ", " + str(attack2_PP) + ", " + str(attack3) + ", " + str(attack3_PP) + ", " +  str(attack4) + ", " + str(attack4_PP) + ")")
        return None
    attacks = [attack1, attack2, attack3, attack4]
    pps = [attack1_PP, attack2_PP, attack3_PP, attack4_PP]
    for attack, pp in zip(attacks, pps):
        if attack is None:
            output_attack = output_attack + "0000"
            output_PP = output_PP + "00"
            continue
        if type(attack) == str:
            attack = attack_dict[attack]
        for item in attack.to_bytes(2, "little"):
            output_attack = output_attack + (hex(item)[2:].zfill(2))
        output_PP = output_PP + str(hex(pp)[2:].zfill(2))
    return (str(output_attack).upper() + str(output_PP).upper())
