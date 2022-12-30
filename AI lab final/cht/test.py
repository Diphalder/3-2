s = "ABCDEFGH"
print(s)
print(s[3])
print(s[1:3])   #1 the 3 er age porjonto
print(s[:3])    #3 er age porjonto
print(s[4:])    #4 theke baki shob
print(s[:3] + "C" + s[4:])
print(s[3:5])   #3 the 5 er age porjonto
print(s[:])
print(s[::2])   #shuru theke 2 ta por por shesh porjonto
print(s[::3])   #shuru theke 3 ta por por shesh porjonto
print(s[-2:2:-1])   #start end inc/dec
print(s[-1:3:-1])   #-1(shesh) theke shuru kore first theke 3 er porer ta porjonto 1 kore kombe

s = 'okay, there\'s a samll one'    #special character er age back-slash'\' boshate hobe
print(s)

s = '\"I love my country\"'    #special character er age back-slash'\' boshate hobe
print(s)

print("Hello\n\tWorld")     #new line & tab

s_len = len("GATTACA")      #length
print(s_len)

s = "GAT" + "TACA"      #concatenation
print(s)

s = "A" * 10    #repeat
print(s)

print("G" in "GATTACA")

print("AGT" in "GATTACA")

print("GATTACA".find("ATT"))    #substring location

print("GATTACA".count("T"))     #substring count

print(int("38"))            #printing integer

print(int("38") + 5)        #integer addition

print("38" + str(5))        #string addition

print(int("38"), str(5))    #appending ineger & string side by side

print(float("2.71828"))     #printing float

print("GATTACA".lower())    #lower banai

print("gattaca".upper())    #upper banai

print("GATTACA".replace("G", "U"))      #'G' ke 'U' die replace kori

print("GATTACA".replace("C", "U"))      #'C' ke 'U' die replace kori

print("GATTACA".replace("AT", "**"))    #'AT' ke '**' die replace kori

print("GATTACA".startswith("G"))

print("GATTACA".startswith("g"))



