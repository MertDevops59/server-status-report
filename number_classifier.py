
sayi = int(input("Bir Sayı yazın:"))


if sayi > 0:
   print ( "Pozitif sayı")

   if  sayi % 2 == 0:
        print ("Sayı çift")
   else:
       print ("Tek")

elif sayi < 0:
     print ( "Negatif sayı")

     if sayi % 2  != 0: 
         print ( "Sayı Tek")
     else:
         print ("Çift")
else:
    print("Sıfır")

