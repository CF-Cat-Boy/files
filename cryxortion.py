import random
encrypt = bool()
text = str()
key = int()
text = input("Text: ").replace("\\n","\n")
encrypt = input("En/Decrypt? (en/de):").lower()=="en"
skey = input("Cryption Key: ")
if skey=="rand":
    key = random.randint(255,511)
    print(f"key = {key:X}")
else:
    key = int(skey,base=16)
out = list[str]()
def do():
    if encrypt:
        for i in text:
            out.append(f"{((ord(i)+key)^key):X}")
        '''
        if not "".join(out).isprintable():
            for ii in out:
                if not ii.isprintable():
                    iii = out.index(ii)
                    print(iii)
                out[iii] = chr(ord(out[iii]))
        '''
        sout = "".join(out).replace("\x9f","Ÿ").replace("\x89","‰")
    else:
        for i in range(0,len(text),2):
            j = int(text[i:i+2],base=16)
            out.append(chr(((j)^key)-key))
        sout = "".join(out).replace("ᾱ","\n").replace("ù"," ")
    return sout
'''h = do()
encrypt = False
text = h'''
print(do())