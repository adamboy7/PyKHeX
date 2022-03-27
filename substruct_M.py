import random
from PID_Search import PID_Search

accepted_pokeballs = {
"master":1
"ultra":2
"great":3
}

def substruct_M(PID, Pokerus_days, Pokerus_strain, location, OT_gender, pokeball = 3, Game, Level_met, HP = None, Attack = None, Defense = None, Speed = None, Special_Attack = None, Special_Defence = None, egg = False, ability = None, ribbons = None, obedience = 0):
    error = 0
    if pokeball not <= 12 and not >= 1:
        print ("Invalid \"pokeball\" int:", pokemon, "Expected 1 -> 12")
        error = 1
    if type(egg) != bool:
        print ("Invalid \"egg\" bool:", egg)
    if type(ribbons) != None and type(ribbons) != int:
        print ("Invalid \"ribbons\" int:", ribbons)
        error = 1
    if error == 1:
        return (None)
    if ribbons == None:
        ribbons = 0
    if ability == None:
        print (PID_Search(PID))
    if type(HP) != int:
        HP = random.randint(0, 31)
    if type(Attack) != int:
        Attack = random.randint(0, 31)
    if type(Defense) != int:
        Defense = random.randint(0, 31)
    if type(Speed) != int:
        Speed = random.randint(0, 31)
    if type(Special_Attack) != int:
        Special_Attack = random.randint(0, 31)
    if type(Special_Defence) != int:
        Special_Defence = random.randint(0, 31)
