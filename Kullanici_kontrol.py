import subprocess

kullanici = input ("kullanıci adi: ")

sonuc = subprocess.run(["id", kullanici], capture_output=True, text=True)

if sonuc.returncode == 0:
   print ("kullanıcı Bulundu:")
   print (sonuc.stdout)
else:
    print ("kullanıcı Bulunamadı!")
