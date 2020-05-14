def cipher(text):
    # アルファベット小文字 → (97, 123)
    text = [chr(219 - ord(t)) if 97 <= ord(t) <= 123 else t for t in text]
    return ''.join(text)


text = 'this is a message.'
encryption_text = cipher(text)
decryption_text = cipher(encryption_text)

print('{}\n{}'.format(encryption_text, decryption_text))
