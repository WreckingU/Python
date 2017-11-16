from random import randint

list1 = ["artless", "bawdy", "bootless", "churlish", "clouted", "craven", "dissembling", "errant", "fawning", "fobbing", "frothy", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "paunchy" ,"rank" ,"saucy", "spleeny" ,"spongy" ,"villainous", "wayward", "yeasty"]
list2 = ["base-court", "bat-fowling", "beetle-headed", "boil-brained", "clay-brained", "common-kissing", "dizzy-eyed", "dread-bolted", "earth-vexing", "elf-skinned", "fen-sucked", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "ill-breeding" ,"onion-eyed" ,"reeling-ripe","rough-hewn" ,"rude-growing" ,"tardy-gaited", "toad-spotted", "weather-bitten",]
list3 = ["apple-john", "baggage", "bladder", "boar-pig", "bum-bailey", "canker-blossom", "coxcomb", "death-token", "dewberry", "flap-dragon", "flirt-gill", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "lout" ,"minnow" ,"nut-hook", "pigeon-egg" ,"pignut" ,"strumpet", "vassal", "wagtail"]

print "Shakespearean Insults:"

for i in range(20):
    print "Thou", list1[randint (0, (len(list1)) -1)], list2[randint (0, (len(list2)) -1)], list3[randint (0, (len(list3)) -1)]
