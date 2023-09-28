import requests
import hashlib

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    resp = requests.get(url)
    if resp.status_code == 200:
        hashes = resp.text.splitlines()
        for h in hashes:
            if suffix in h:
                return True
    return False

def main():
    filename = input("Укажите имя файла: ")
  
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                username, password = line.split(',')
                password = password.strip()
                if check_password(password):
                    print(f"У пользователя {username} утеря пароля {password}")
                else:
                    print(f"У пользоваетля {username} пароль безопасен")
    except FileNotFoundError:
        print("Имя файла не найдено")

if name == "main":
    main()
