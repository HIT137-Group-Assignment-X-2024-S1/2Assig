total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total += i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

def encrypt(text, key): 
    encrypted_text = "" 
    for char in text: 
        if char.isalpha(): 
            shifted = ord(char) + key 
            if char.islower(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('a'): 
                    shifted += 26 
            elif char.isupper(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('A'): 
                    shifted += 26 
            encrypted_text += chr(shifted) 
        else: 
            encrypted_text += char 
    return encrypted_text 
                
key = total
# encrypted_code = encrypt(original_code, key) 
# print(encrypted_code) 

def decrypt(text, key): 
    decrypted_text = "" 
    print(text)
    for char in text: 
        if char.isalpha(): 
            shifted = ord(char) + key 
            if char.islower(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('a'): 
                    shifted += 26 
            elif char.isupper(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('A'): 
                    shifted += 26 
            decrypted_text += chr(shifted) 
        else: 
            decrypted_text += char 
    return decrypted_text 

encrypted_text = '''
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0: 
            ahzoref.erzbir (ybpny_inevnoyr)
        ybpny_inevnoyr

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref (ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5): 
    cevag(v)
    V += 1

vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg) '''

decrypted_text = decrypt(encrypted_text, total)     #Decrypt text
print(decrypted_text)                               #Print decrypted text