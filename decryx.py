import random
text = str()
key = int()
text = input("Text: ").replace("\\n","\n")
skey = input("Cryption Key: ")
if skey=="rand":
    key = random.randint(255,511)
    print(f"key = {key:X}")
else:
    key = int(skey,base=16)
out = list[str]()
def do():
    for i in range(0,len(text),2):
        j = int(text[i:i+2],base=16)
        out.append(chr(((j)^key)-key))
    sout = "".join(out).replace("ᾱ","\n").replace("ù"," ")
    return sout
'''h = do()
encrypt = False
text = h'''
print(do())
