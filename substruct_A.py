import importlib

generations_List = [1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII"]
roman_Numerals = [None, "I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
roman_Dict = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8}
attack_Dict = {}

def substruct_A(attack1, attack1_PP = 0, attack2 = None, attack2_PP = 0, attack3 = None, attack3_PP = 0, attack4 = None, attack4_PP = 0, generation = 3):
    output_attack = str()
    output_PP = str()
    generation_Dict = 1 # Start at generation 1 and import attacks untill specified generation is reached.
    error = 0
    if generation not in generations_List:
        print ("Invalid \"generation\" int/str:")
        error = 1
    if type(generation) == str: # supplied generation was a roman numeral, convert to a number for math.
        generation = roman_Dict[generation]
    # I was too stubborn to restructure my dictionary and didn't want to import every generation's attacks. I shouldn't have been stubborn.
    # Dynamically import the generation's availible attacks and iterate through all previous generations. Because "efficiency"?
    while generation >= generation_Dict:
        attacks_Dictonary = importlib.import_module("Dictionaries." + str("attacks_" + str(roman_Numerals[generation_Dict])))
        new_Attacks = [x for x in attacks_Dictonary.__dict__ if not x.startswith("_")]
        globals().update({k: getattr(attacks_Dictonary, k) for k in new_Attacks})
        attack_Dict.update(globals()["attacks_" + str(roman_Numerals[generation_Dict])])
        generation_Dict = generation_Dict + 1
        # End of being stubborn
    if type(attack1_PP) != int or attack1_PP > 255 or attack1_PP < 0:
        print ("Invalip PP count on attack 1", "\"" + str(attack1_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack2_PP) != int or attack2_PP > 255 or attack2_PP < 0:
        print ("Invalip PP count on attack 2", "\"" + str(attack2_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack3_PP) != int or attack3_PP > 255 or attack3_PP < 0:
        print ("Invalip PP count on attack 3", "\"" + str(attack3_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if type(attack4_PP) != int or attack4_PP > 255 or attack4_PP < 0:
        print ("Invalip PP count on attack 4", "\"" + str(attack4_PP) + "\",", "Expected int 0 -> 255")
        error = 1
    if attack1 != None and attack1 not in attack_Dict:
        print ("Invalid attack 1:", attack1)
        error = 1
    if attack2 != None and attack2 not in attack_Dict:
        print ("Invalid attack 2:", attack2)
        error = 1
    if attack3 != None and attack3 not in attack_Dict:
        print ("Invalid attack 3:", attack3)
        error = 1
    if attack4 != None and attack1 not in attack_Dict:
        print ("Invalid attack 4:", attack4)
        error = 1
    if error == 1:
        print ("Input: substruct_A(" + str(generation) + ", " + str(attack1) + ", " + str(attack1_PP) + ", " + str(attack2) + ", " + str(attack2_PP) + ", " + str(attack3) + ", " + str(attack3_PP) + ", " +  str(attack4) + ", " + str(attack4_PP) + ")")
        return None
    attack_Slot = 0
    padding = 0
    while attack_Slot <= 3:
        attack_Slot = attack_Slot + 1
        if vars()["attack" + str(attack_Slot)] == None:
            padding = padding + 1
            continue
        if type(vars()["attack" + str(attack_Slot)]) == str:
            for item in (attack_Dict[vars()["attack" + str(attack_Slot)]]).to_bytes(2, "little"):
                output_attack = output_attack + (hex(item)[2:].zfill(2))
            output_PP = output_PP + str(hex(vars()["attack" + str(attack_Slot) + "_PP"])[2:].zfill(2))
        if type(vars()["attack" + str(attack_Slot)]) == int:
            for item in (vars()["attack" + str(attack_Slot)]).to_bytes(2, "little"):
                output_attack = output_attack + (hex(item)[2:].zfill(2))
            output_PP = output_PP + str(hex(vars()["attack" + str(attack_Slot) + "_PP"])[2:].zfill(2))
    while padding > 0:
        output_attack = output_attack + "0000"
        output_PP = output_PP + "00"
        padding = padding - 1
    return (str(output_attack).upper() + str(output_PP).upper())
