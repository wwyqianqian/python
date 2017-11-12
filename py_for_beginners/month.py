months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("input[1:13] : ")
pos = (int(n)-1) * 3
monthAbbrev = months[pos:pos+3]
print(monthAbbrev)
