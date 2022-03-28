import os.path
from os import path
from pk3_Info import pk3_Info
from PID_Search import PID_Search
from substruct_G import substruct_G
from substruct_A import substruct_A
from substruct_E import substruct_E
from translate import translate
from dex_Search import dex_Search
from item_Search import item_Search

if not path.exists("config.txt"):
        print ("Error: config.txt does not exist!")
        print ("config.txt requires line: 'Name = YourNameHere'")
        print ("config.txt requires line: 'Trainer ID = #####'")
        print ("config.txt requires line: 'Secret ID = #####'")
        exit()

PID = "F0700EDA"
pokemon = "Torchic"
item = None
EXP = 221
friendship = 84

print (pk3_Info(pokemon, PID))
print (substruct_G(pokemon, item, EXP, friendship))
print (substruct_A("Scratch", 35, "Growl", 40))
print (substruct_E(None, None, None, None, None, None, 0, 1, 2, 3, 4, 5))
print (PID_Search(PID))
print (translate("Hello world!"))
print (dex_Search("Torchic", Internal_or_National = "National"))
print (item_Search("Potion"))
