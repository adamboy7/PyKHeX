import random

max_EV = 510

def substruct_E(HP = 0, Attack = 0, Defense = 0, Speed = 0, Special_Attack = 0, Special_Defence = 0, Coolness = 0, Beauty = 0, Cuteness = 0, Smartness = 0, Toughness = 0, Feel = 0):
    error = 0
    if type(HP) == int and HP > 255 or type(HP) == int and HP < 0:
        error = 1
        print ("Invalid \"HP\" int, 0 -> 255")
    if type(Attack) == int and Attack > 255 or type(Attack) == int and Attack < 0:
        error = 1
        print ("Invalid \"Attack\" int, 0 -> 255")
    if type(Defense) == int and Defense > 255 or type(Defense) == int and Defense < 0:
        error = 1
        print ("Invalid \"Defense\" int, 0 -> 255")
    if type(Speed) == int and Speed > 255 or type(Speed) == int and Speed < 0:
        error = 1
        print ("Invalid \"Speed\" int, 0 -> 255")
    if type(Special_Attack) == int and Special_Attack > 255 or type(Special_Attack) == int and Special_Attack < 0:
        error = 1
        print ("Invalid \"Special_Attack\" int, 0 -> 255")
    if type(Special_Defence) == int and Special_Defence > 255 or type(Special_Defence) == int and Special_Defence < 0:
        error = 1
        print ("Invalid \"Special_Defence\" int, 0 -> 255")
    if type(Coolness) == int and Coolness > 255 or type(Coolness) == int and Coolness < 0:
        error = 1
        print ("Invalid \"Coolness\" int, 0 -> 255")
    if type(Beauty) == int and Beauty > 255 or type(Beauty) == int and Beauty < 0:
        error = 1
        print ("Invalid \"Beauty\" int, 0 -> 255")
    if type(Cuteness) == int and Cuteness > 255 or type(Cuteness) == int and Cuteness < 0:
        error = 1
        print ("Invalid \"Cuteness\" int, 0 -> 255")
    if type(Smartness) == int and Smartness > 255 or type(Smartness) == int and Smartness < 0:
        error = 1
        print ("Invalid \"Smartness\" int, 0 -> 255")
    if type(Toughness) == int and Toughness > 255 or type(HP) == Toughness and Toughness < 0:
        error = 1
        print ("Invalid \"Toughness\" int, 0 -> 255")
    if type(Feel) == int and Feel > 255 or type(Feel) == int and Feel < 0:
        error = 1
        print ("Invalid \"Feel\" int, 0 -> 255")
    if error == 1:
        return (None)
    if type(HP) != int:
        HP = random.randint(0, 85)
    if type(Attack) != int:
        Attack = random.randint(0, 85)
    if type(Defense) != int:
        Defense = random.randint(0, 85)
    if type(Speed) != int:
        Speed = random.randint(0, 85)
    if type(Special_Attack) != int:
        Special_Attack = random.randint(0, 85)
    if type(Special_Defence) != int:
        Special_Defence = random.randint(0, 85)
    if type(Coolness) != int:
        Coolness = random.randint(0, 255)
    if type(Beauty) != int:
        Beauty = random.randint(0, 255)
    if type(Cuteness) != int:
        Cuteness = random.randint(0, 255)
    if type(Smartness) != int:
        Smartness = random.randint(0, 255)
    if type(Toughness) != int:
        Toughness = random.randint(0, 255)
    if type(Feel) != int:
        Feel = random.randint(0, 255)
    EV = HP + Attack + Defense + Speed + Special_Attack + Special_Defence
    if EV > max_EV:
        print ("EV total:", EV, "too high! Possible Bad Egg?")
    return (hex(HP)[2:].zfill(2).upper() + hex(Attack)[2:].zfill(2).upper() + hex(Defense)[2:].zfill(2).upper() + hex(Speed)[2:].zfill(2).upper() + hex(Special_Attack)[2:].zfill(2).upper() + hex(Special_Defence)[2:].zfill(2).upper() + hex(Coolness)[2:].zfill(2).upper() + hex(Beauty)[2:].zfill(2).upper() + hex(Cuteness)[2:].zfill(2).upper() + hex(Smartness)[2:].zfill(2).upper() + hex(Toughness)[2:].zfill(2).upper() + hex(Feel)[2:].zfill(2).upper())
