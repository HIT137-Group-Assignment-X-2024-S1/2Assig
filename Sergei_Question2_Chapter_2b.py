def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_text = ""
    for char in cryptogram:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift_key) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift_key) % 26) + ord('a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def decrypt_with_all_shifts(cryptogram):
    for shift_key in range(26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift_key)
        print(f"Shift Key {shift_key}: {decrypted_text}")

cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNIAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypt_with_all_shifts(cryptogram)