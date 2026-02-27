#morse code encoder demo (Words must be put in all caps)
MorseCodeDictionary = {
"A" : ".- ",
"B" : "-.... ",
"C" : "-.-. ",
"D" : "_.. ",
"E" : ". ",
"F" : "..-. ",
"G" : "--. ",
"H" : ".... ",
"I" : ".. ",
"J" : ".--- ",
"K" : "-.- ",
"L" : ".-.. ",
"M" : "-- ",
"N" : "-. ",
"O" : "--- ",
"P" : ".__. ",
"Q" : "--.- ",
"R" : ".-. ",
"S" : "... ",
"T" : "- ",
"U" : "..- ",
"V" : "...- ",
"W" : ".-- ",
"X" : "-..- ",
"Y" : "-.-- ",
"Z" : "--.. ",
" " : "/ ", #Space between words
"1" : ".---- ",
"2" : "..--- ",
"3" : "...-- ",
"4" : "....- ",
"5" : "..... ",
"6" : "-.... ",
"7" : "--... ",
"8" : "---.. ",
"9" : "----. ",
"0" : "----- ",
}

Encode = input("Encode in all caps: ")
for i in Encode:
    if i in MorseCodeDictionary:
        print(MorseCodeDictionary[i],end='')