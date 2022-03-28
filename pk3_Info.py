from dex_Search import dex_Search
from PID_Search import PID_Search
from translate import translate

accepted_languages = ["international", "english", "0202", "french" "0203", "italian", "0204", "german", "0205", "spanish", "0207", "japanese", "0201"]

def pk3_Info(pokemon, pokemon_ID, OT_Name = None, trainer_ID = None, trainer_SID = None, language = "0202", nickname = None, circle = False, square = False, triangle = False, heart = False):
    # - - - Sanitize inputs - - -
    error = 0
    if dex_Search(pokemon) == None:
        print ("Invalid \"pokemon\" str/int:", pokemon)
        error = 1
    if (PID_Search(pokemon_ID)[1])[0] == None:
        print ("Invalid \"pokemon_ID\" int/str:", pokemon_ID)
        error = 1
    if OT_Name == None:
        config = open("config.txt", "r")
        for line in config:
            line = line.split("=")
            if line[0].strip() == "Name":
                try:
                    OT_Name = line[1].strip()
                except:
                    print ("Invalid Trainer Name of", line[1].strip())
    if OT_Name == None:
        print ("config.txt requires line: 'Name = YourNameHere'")
        error = 1
    if translate(OT_Name) == None:
        print ("Invalid \"OT_Name\" str:", OT_Name)
        error = 1
    if trainer_ID == None:
        config = open("config.txt", "r")
        for line in config:
            line = line.split("=")
            if line[0].strip() == "Trainer ID":
                try:
                    trainer_ID = int(line[1].strip())
                except:
                    print ("Invalid Trainer ID of", line[1].strip())
    if trainer_ID == None:
        print ("config.txt requires line: 'Trainer ID = #####'")
        error = 1
    if trainer_ID != None and type(trainer_ID) != int:
        print ("Invalid \"trainer_ID\" int:", trainer_ID)
    if trainer_SID == None:
        config = open("config.txt", "r")
        for line in config:
            line = line.split("=")
            if line[0].strip() == "Secret ID":
                try:
                    trainer_SID = int(line[1].strip())
                except:
                    print ("Invalid Secret ID of", line[1].strip())
    if trainer_SID == None:
        print ("config.txt requires line: 'Secret ID = #####'")
        error = 1
    if trainer_SID != None and type(trainer_SID) != int:
        print ("Invalid \"trainer_SID\" int:", trainer_ID)
    if language.lower() not in accepted_languages:
        print ("Invalid \"language\" string:", language)
        error = 1
    if language.lower() == "japanese":
        language = "0201"
    if language.lower() == "international" or language == "english":
        language = "0202"
    if language.lower() == "french":
        language = "0203"
    if language.lower() == "italian":
        language = "0204"
    if language.lower() == "german":
        language = "0205"
    if language.lower() == "spanish":
            language = "0207"
    if nickname != None and translate(nickname) == None:
        print("Invalid \"nickname\" str:", nickname)
        error = 1
    if type(circle) != bool:
        print("Invalid Circle mark bool:", circle)
        error = 1
    if type(square) != bool:
        print("Invalid Square mark bool:", square)
        error = 1
    if type(triangle) != bool:
        print("Invalid Triangle mark bool:", triangle)
        error = 1
    if type(heart) != bool:
        print("Invalid Heart mark bool:", heart)
        error = 1
    if error == 1:
        print ("Input: pk3_Info(" + str(pokemon) + ", " + str(pokemon_ID) + ", " + str(OT_Name) + ", " + str(trainer_ID) + ", " + str(trainer_SID) + ", " + str(language) + ", " + str(nickname) + ", " + str(circle) + ", " + str(square) + ", " + str(triangle) + ", " + str(heart) + ")")
        return None
    # - - - Done sanitizing inputs - - -
    PID_Little = str()
    for PID_Byte in (int((PID_Search(pokemon_ID)[1])[0], 16).to_bytes(4, 'little')):
        PID_Little = PID_Little + hex(PID_Byte)[2:].zfill(2)
    TID_Full = hex(trainer_SID)[2:] + hex(trainer_ID)[2:]
    TID_Little = str()
    for TID_Byte in (int(TID_Full, 16).to_bytes(4, 'little')):
        TID_Little = TID_Little + hex(TID_Byte)[2:].zfill(2)
    markings = 0
    if circle == True:
        markings = markings + 0
    if square == True:
        markings = markings + 0
    if triangle == True:
        markings = markings + 0
    if heart == True:
        markings = markings + 0
    if nickname == None:
        return (PID_Little.upper() + TID_Little.upper() + translate(dex_Search(pokemon, return_Upper = True)[0], 10, language).upper() + language.upper() + translate(OT_Name, 7, language).upper() + hex(markings)[2:].zfill(2).upper() + "CHCK" + "0000".upper())
    if nickname != None:
        return (PID_Little.upper() + TID_Little.upper() + translate(nickname, 10, language).upper() + language.upper() + translate(OT_Name, 7, language).upper() + hex(markings)[2:].zfill(2).upper() + "CHCK" + "0000".upper())
