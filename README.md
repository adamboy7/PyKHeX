# PyKHeX
A work in progress, worse implementation of PKHeX in Python. It started off as a bit of deep dive into pokemon data structures, the goal is to batch find compatible PID's and batch create pokemon based on facotors like shininess, natures, abilities, etc. At which point you could then pump any of your newly generated PID's into something like EonTimer or import a generated pokemon file directly into your save using PKHeX (But like, the real one.) Currently the main focus of the project is generation 3 and under, but plans are to include as much compatibility for as many generations as possible.

# Features
2 way PID searching, you can either give the program an exisitng PID and it can spit out everything about it, or you can define specific traits and the program will brute-force a PID for you.

Various tools and libraries to generate each "GAEM" substructure of a given pokemon, eg. Converting textnames and strings to properly encoded hexadecimal, converting names to pokedex numbers and vice versa, move lookups, etc. Each module is able to be imported as a function for use in other projects or components.

# Examples
*Required arguments in bold*

PID_Search, returns an array of pokemon information based on provided arguments, also returns true or false if the PID matches the supplied arguments:

PID_Search(**PID**, gender, ability, nature, gender_Ratio, shiny, letter, wurmple, mirage, generation)
```
print (PID_Search("F0700EDA"))
#Output: (True, ('f0700eda', 'Male', 0, 'quirky', 15389, 'K', 'silcoon', 3802, 'GEAM', 1794549825))
```

pk3_Info, returns the first 32 bytes of a pokemon data structure based on the provided arguments and information entered in "config.txt" if things like name, trainer ID, and trainer Secret ID are not specified. **Checksum not yet implimented**:

pk3_Info(**pokemon**, **pokemon_ID**, OT_Name, trainer_ID, trainer_SID, language, nickname, circle, square, triangle, heart)

```
print (pk3_Info("Torchic", "F0700EDA"))
#Output: DA0E70F041A8F66ACEC9CCBDC2C3BDFFFFFF0202BBD8D5E1FFFFFF00CHCK0000
```

substruct_G, returns the 12 byte "Growth" block of a pokemon data sub-structure based on the provided arguments:

substruct_G(**pokemon**, item, EXP, friendship, PP_Boost, Internal_or_National, generation)

```
print (substruct_G("Torchic", item = None, EXP = 221, friendship = 84))
#Output: FF000000DD00000000540000
```

substruct_A, returns the 12 byte "Attacks" block of a pokemon data sub-structure based on the provided arguments:

substruct_A(**attack1**, attack1_PP, attack2, attack2_PP, attack3, attack3_PP, attack4, attack4_PP, generation)
```
print (substruct_A("Scratch", 35, "Growl", 40))
#Output: 0A002D000000000023280000
```

substruct_E, returns the 12 byte "EVs & Condition" block of a pokemon sub-data structure based on the provided arguments, or randomly generated stats if None type provided:

substruct_E(HP, Attack, Defense, Speed, Special_Attack, Special_Defence, Coolness, Beauty, Cuteness, Smartness, Toughness, Feel)
```
print (substruct_E(None, None, None, None, None, None, 0, 1, 2, 3, 4, 5))
#Output: 4A1F32070848000102030405
```

substruct_M, returns the 12 byte "Miscellaneous" block of a pokemon sub-data structure based on the provided arguments, **WIP**:

substruct_M(PID, Pokerus_days, Pokerus_strain, location, OT_gender, pokeball, game, Level_met, HP, Attack, Defense, Speed, Special_Attack, Special_Defence, egg, ability, ribbons, obedience)
```
print (substruct_M("F0700EDA", game = "Emerald", location = "Victory Road"))
```
