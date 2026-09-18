hatalar = []

with open("log.txt", "r") as dosya:
    for satir in dosya:
        if "ERROR" in satir:
            hatalar.append(satir)

print("Toplam hata:", len(hatalar))
for hata in hatalar:
    print(hata)
