import subprocess

kullanici = input("Kullanıcı adı: ")

sonuc = subprocess.run(["last", "-n", "10"], capture_output=True, text=True)

if sonuc.returncode == 0:
    print("Son Girişler")
    print(sonuc.stdout)

sonuc2 = subprocess.run(["id", kullanici], capture_output=True, text=True)

if sonuc2.returncode == 0:
    print("Kullanıcı Bulundu")
    print(sonuc2.stdout)
else:
    print("Kullanıcı Bulunamadı!")
