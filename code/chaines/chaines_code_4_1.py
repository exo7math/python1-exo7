# A la machine
code = [80,121,116,104,111,110,32,101,115,116,32,115,121,109,112,64]
phrase = ""
for c in code:
    phrase = phrase + chr(c)
print(phrase)