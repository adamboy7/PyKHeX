import os.path
from os import path

natures_List = ["hardy", "lonely", "brave", "adamant", "naughty", "bold", "docile", "relaxed", "impish", "lax", "timid", "hasty", "serious", "jolly", "naive", "modest", "mild", "quiet", "bashful", "rash", "calm", "gentle", "sassy", "careful", "quirky"]
Unown_Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?", "!"]
data_Structures = ["GAEM", "GAME", "GEAM", "GEMA", "GMAE", "GMEA", "AGEM", "AGME", "AEGM", "AEMG", "AMGE", "AMEG", "EGAM", "EGMA", "EAGM", "EAMG", "EMGA", "EMAG", "MGAE", "MGEA", "MAGE", "MAEG", "MEGA", "MEAG"]

generations_List = [1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII"]

generation_Gender_Calc = [3, "III", 4, "IV", 5, "IV"]
generation_Ability_Calc = [3, "III", 4, "IV", 5, "IV"]
generation_Nature_Calc = [3, "III", 4, "IV"]
generation_Letter_Calc = [3, "III"]
generation_Wurmple_Calc = [3, "III", 4, "IV", 5, "IV"]
generation_Mirage_Calc = [3, "III"]

# Returns: (Filter True/False), PID, Gender, Ability Slot, Nature, Shiny XOR, Letter, Wurmple Evolution, Mirage Number, Substrugture Order, Encryption key

def PID_Search(PID, gender = None, ability = None, nature = None, gender_Ratio = 127, shiny = None, letter= None, wurmple= None, mirage= None, generation = 3):
    # - - - Sanitize inputs - - -
    error = 0
    if type(PID) == str:
        try:
            PID = int(PID, 16)
        except:
            print ("Invalid \"PID\" hex string:", PID)
            error = 1
    if PID == 0:
        print ("PID can not be 0!")
        error = 1
    if gender != None and gender.lower() != 'male' and gender.lower() !='female' and gender.lower() !='genderless':
        print ("Invalid \"gender\" string:", gender) #I mean, your gender isn't invalid. The pokemon's is.
        error = 1
    if ability != None and type(ability) != int:
        print ("Invalid \"ability\" int:", ability)
        error = 1
    if nature != None and nature.lower() not in natures_List:
        print ("Invaid \"nature\" string:", nature)
        error = 1
    if gender_Ratio != None and type(gender_Ratio) != int:
        print ("Invalid \"gender_Ratio\" int:", gender_Ratio)
        error = 1
    if shiny != None and type(shiny) != int:
        print ("Invalid \"shiny\" int:", shiny)
        error = 1
    if letter != None and letter.upper() not in Unown_Alphabet:
        print ("Invalid \"letter\" str:", letter)
        error = 1
    if wurmple != None and wurmple.lower() != "silcoon" and wurmple.lower() != "cascoon":
        print ("Invalid \"wurmple\" str:", wurmple)
        error = 1
    if mirage != None and type(mirage) != int or mirage != None and mirage < 0 or mirage != None and mirage > 65535:
        print ("Invalid \"mirage\" int 0->65535:", mirage)
        error = 1
    if generation not in generations_List:
        print ("Invalid generation int/str:", generation)
        error = 1
    if gender != None and generation not in generation_Gender_Calc:
        print ("PID gender calculation not supported in generation", str(generation) + ", skipping filter...")
        gender = None
    if ability != None and generation not in generation_Ability_Calc:
        print ("PID ability calculation not supported in generation", str(generation) + ", skipping filter...")
        ability = None
    if nature != None and generation not in generation_Nature_Calc:
        print ("PID nature calculation not supported in generation", str(generation) + ", skipping filter...")
        nature = None
    if letter != None and generation not in generation_Letter_Calc:
        print ("PID letter calculation not supported in generation", str(generation) + ", skipping filter...")
        letter = None
    if wurmple != None and generation not in generation_Wurmple_Calc:
        print ("PID wurmple evolution calculation not supported in generation", str(generation) + ", skipping filter...")
        wurmple = None
    if mirage != None and generation not in generation_Mirage_Calc:
        print ("PID mirage island calculation not supported in generation", str(generation) + ", skipping filter...")
        mirage = None
    if error == 1:
        print ("Input: PID_Search(" + str(PID) + ", " + str(gender) + ", " + str(ability) + ", " + str(nature) + ", " + str(gender_Ratio) + ", " + str(shiny) + ", " + str(letter) + ", " + str(wurmple) + ", " + str(mirage) + ", " + str(generation) + ")")
        return None
    # - - - Done sanitizing inputs - - -
    # - - - Get trainer ID/SID from config file - - -
    if not path.exists("config.txt"):
        print ("Error: config.txt does not exist!")
        print ("config.txt requires line: 'Trainer ID = #####'")
        print ("config.txt requires line: 'Secret ID = #####'")
        exit()
    ID = None
    SID = None
    config = open("config.txt", "r")
    for line in config:
        line = line.split("=")
        if line[0].strip() == "Trainer ID":
            try:
                ID = int(line[1].strip())
            except:
                print ("Invalid Trainer ID of", line[1].strip())
        if line[0].strip() == "Secret ID":
            try:
                SID = int(line[1].strip())
            except:
                print ("Invalid Secret ID of", line[1].strip())
    if ID == None:
        print ("config.txt requires line: 'Trainer ID = #####'")
    if SID == None:
        print ("config.txt requires line: 'Secret ID = #####'")
    if ID == None or SID == None:
        exit()
    # - - - Done getting trainer ID/SID from config file - - -
    TID_XOR = ID ^ SID
    TID_Full = hex(SID)[2:] + hex(ID)[2:]
    if gender != None and gender.lower() == "male" and (PID % 256) >= gender_Ratio and gender_Ratio != 255 or gender == None and (PID % 256) >= gender_Ratio and gender_Ratio != 255:
        if ability == (PID % 2) or ability == None:
            if nature != None and nature.lower() == natures_List[(PID % 25)] or nature == None:
                PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
                PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
                PID_XOR = PID1 ^ PID2
                temp_XOR = TID_XOR ^ PID_XOR
                if shiny == temp_XOR or shiny == None:
                    Unown1 = bin(PID)[2:].zfill(32)[6:8]
                    Unown2 = bin(PID)[2:].zfill(32)[14:16]
                    Unown3 = bin(PID)[2:].zfill(32)[22:24]
                    Unown4 = bin(PID)[2:].zfill(32)[30:32]
                    Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
                    if letter == Unown_Alphabet[Unown_Letter] or letter == None:
                        wurmple_Path = PID1 % 10
                        if wurmple_Path <= 4:
                            evolution = "silcoon"
                        if wurmple_Path > 4:
                            evolution = "cascoon"
                        if wurmple != None and wurmple.lower() == evolution or wurmple == None:
                            if mirage == PID2 or mirage == None:
                                return True, (hex(PID)[2:].zfill(8), "Male", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
    if gender != None and gender.lower() == "female" and (PID % 256) < gender_Ratio and gender_Ratio != 255 or gender == None and (PID % 256) < gender_Ratio and gender_Ratio != 255:
        if ability == (PID % 2) or ability == None:
            if nature != None and nature.lower() == natures_List[(PID % 25)] or nature == None:
                PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
                PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
                PID_XOR = PID1 ^ PID2
                temp_XOR = TID_XOR ^ PID_XOR
                if shiny == temp_XOR or shiny == None:
                    Unown1 = bin(PID)[2:].zfill(32)[6:8]
                    Unown2 = bin(PID)[2:].zfill(32)[14:16]
                    Unown3 = bin(PID)[2:].zfill(32)[22:24]
                    Unown4 = bin(PID)[2:].zfill(32)[30:32]
                    Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
                    if letter == Unown_Alphabet[Unown_Letter] or letter == None:
                        wurmple_Path = PID1 % 10
                        if wurmple_Path <= 4:
                            evolution = "silcoon"
                        if wurmple_Path > 4:
                            evolution = "cascoon"
                        if wurmple != None and wurmple.lower() == evolution or wurmple == None:
                            if mirage == PID2 or mirage == None:
                                return True, (hex(PID)[2:].zfill(8), "Female", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
    if gender != None and gender.lower() == "genderless" or gender_Ratio == 255:
        if ability == (PID % 2) or ability == None:
            if nature != None and nature.lower() == natures_List[(PID % 25)] or nature == None:
                PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
                PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
                PID_XOR = PID1 ^ PID2
                temp_XOR = TID_XOR ^ PID_XOR
                if shiny == temp_XOR or shiny == None:
                    Unown1 = bin(PID)[2:].zfill(32)[6:8]
                    Unown2 = bin(PID)[2:].zfill(32)[14:16]
                    Unown3 = bin(PID)[2:].zfill(32)[22:24]
                    Unown4 = bin(PID)[2:].zfill(32)[30:32]
                    Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
                    if letter == Unown_Alphabet[Unown_Letter] or letter == None:
                        wurmple_Path = PID1 % 10
                        if wurmple_Path <= 4:
                            evolution = "silcoon"
                        if wurmple_Path > 4:
                            evolution = "cascoon"
                        if wurmple != None and wurmple.lower() == evolution or wurmple == None:
                            if mirage == PID2 or mirage == None:
                                return True, (hex(PID)[2:].zfill(8), "Genderless", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
    # Supplied PID did not match supplied filters, return false + details
    if (PID % 256) >= gender_Ratio and gender_Ratio != 255 and gender.lower() != "genderless":
        PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
        PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
        PID_XOR = PID1 ^ PID2
        temp_XOR = TID_XOR ^ PID_XOR
        Unown1 = bin(PID)[2:].zfill(32)[6:8]
        Unown2 = bin(PID)[2:].zfill(32)[14:16]
        Unown3 = bin(PID)[2:].zfill(32)[22:24]
        Unown4 = bin(PID)[2:].zfill(32)[30:32]
        Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
        wurmple_Path = PID1 % 10
        if wurmple_Path <= 4:
            evolution = "silcoon"
        if wurmple_Path > 4:
            evolution = "cascoon"
        return False, (hex(PID)[2:].zfill(8), "Male", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
    if (PID % 256) < gender_Ratio and gender_Ratio != 255 and gender.lower() != "genderless":
        PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
        PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
        PID_XOR = PID1 ^ PID2
        temp_XOR = TID_XOR ^ PID_XOR
        Unown1 = bin(PID)[2:].zfill(32)[6:8]
        Unown2 = bin(PID)[2:].zfill(32)[14:16]
        Unown3 = bin(PID)[2:].zfill(32)[22:24]
        Unown4 = bin(PID)[2:].zfill(32)[30:32]
        Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
        wurmple_Path = PID1 % 10
        if wurmple_Path <= 4:
            evolution = "silcoon"
        if wurmple_Path > 4:
            evolution = "cascoon"
        return False, (hex(PID)[2:].zfill(8), "Female", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
    if gender.lower() == "genderless" or gender_Ratio == 255:
        PID1 = int(bin(PID)[2:].zfill(32)[:16], 2)
        PID2 = int(bin(PID)[2:].zfill(32)[16:], 2)
        PID_XOR = PID1 ^ PID2
        temp_XOR = TID_XOR ^ PID_XOR
        Unown1 = bin(PID)[2:].zfill(32)[6:8]
        Unown2 = bin(PID)[2:].zfill(32)[14:16]
        Unown3 = bin(PID)[2:].zfill(32)[22:24]
        Unown4 = bin(PID)[2:].zfill(32)[30:32]
        Unown_Letter = int(Unown1 + Unown2 + Unown3 + Unown4, 2) % 28
        wurmple_Path = PID1 % 10
        if wurmple_Path <= 4:
            evolution = "silcoon"
        if wurmple_Path > 4:
            evolution = "cascoon"
        return False, (hex(PID)[2:].zfill(8), "Genderless", (PID % 2), natures_List[(PID % 25)], temp_XOR, Unown_Alphabet[Unown_Letter], evolution, PID2, data_Structures[(PID % 24)], (int(TID_Full, 16) % PID))
