from Dictionaries.items_III import *

generations_List = [1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII"]

def item_Search(ID, generation = 3):
    error = 0
    if ID == None:
        ID = "none"
    if type(ID) != str and type(ID) != int:
        print ("Invalid \"item\" str/int:", item)
        error = 1
    if generation not in generations_List:
        print ("Invalid generation int/str:", generation)
        error = 1
    if error == 1:
        print ("Input: item_Search(" + str(ID) + ", " + str(generation) + ")")
    try:
        if generation == 1 or generation == "I":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 2 or generation == "II":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 3 or generation == "III":
            if type(ID) == int:
                return items_III[ID]
            if type(ID) == str:
                return items_III[ID.upper()]
        if generation == 4 or generation == "IV":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 5 or generation == "V":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 6 or generation == "VI":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 7 or generation == "VII":
            print ("Unfinished generation item list:", generation)
            return "0000"
        if generation == 8 or generation == "VIII":
            print ("Unfinished generation item list:", generation)
            return "0000"
    except:
        print ("Invalid \"item\" str/int:", ID)
        return None
