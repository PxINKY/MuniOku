Mods = [
    "HuskyGaming109#0001 - 727555617333444618",
    "Legenragon#9924 - 414485583449161728",
    "MedusaCascade#5247 - 327501211093958656",
    "Project Panthera#5877 - 399944746484760577",
    "SKYs#0666 - 689275889904648420",
    "kodagray#5555 - 703059212124553306",
    "Skew#0001 - 192058244380753920",
    "Aigiaon#7381 - 374426210605727744",
    "bloo the protogen#7508 - 498285954814181377",
    "Callidus Fox#3779 - 248590280637284353",
    "Cooled_Wolfie#3558 - 333468719772729346",
    "CyberTaco#5570 - 368142727298285589",
    "Dr.Mortum#4734 - 496367282667257867",
    "GameBreaker75#2348 - 311653382756499456",
    "IBringOda#6440 - 458542061319094293",
    "Gilded#0552 - 297235990194683905",
    "Tec#1502 - 134869338002948096",
    "LegoshiWolfy208#3506 - 812371946746282014",
    "NullJester#0111 - 426857123146760192",
    "Rig#6917 - 131917598639128577",
    "skrapthehusky#9922 - 350979778746122240",
    "pizzadog#1337 - 268890713872269313",
    "strix#2673 - 456538974794809344",
    "ImTim#7857 - 199929668378427392",
    "Matthew (0\'5\")#0696 - 361922415011430420",
    "Zander da folf#1056 - 808000868057088032",
    "ItsMeAudrey#4313 - 134464739198631945"
]


for mod in Mods:
    moddies = mod.split(" - ")
    print("{")
    format_s = f"\"DiscordTag\": \"{moddies[0]}\",\n\"DiscordID\": \"{moddies[1]}\""
    print(format_s)
    print("},")
