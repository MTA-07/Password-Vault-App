DEBUG =True

def encrypt_password(password, shift):
    if DEBUG:
        print(f"[DEBUG] Encrypting password with shift {shift}...")

    encrypted = "".join(chr(ord(c) + shift) for c in password)
    return encrypted

def decrypt_password(encrypted_password, shift):
    if DEBUG:
        print(f"[DEBUG] Decrypting password with shift {shift}...")

    decoded = "".join(chr(ord(c) - shift)for c in encrypted_password)
    return decoded

if __name__ == "__main__":
    gizli_sifrem = "gokce123"
    anahtar = 4

    sifrelenmis_hali = encrypt_password(gizli_sifrem, anahtar)
    print("Sifreli Metin:", sifrelenmis_hali)

    cozulmus_hali = decrypt_password(sifrelenmis_hali, anahtar)
    print("Geri Cozulmus Metin:", cozulmus_hali)

