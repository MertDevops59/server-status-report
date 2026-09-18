sunucular = ["web", "db", "cache", "mail"]
acik = []
kapali = []
supheli =  []


for sunucu in sunucular:
    if sunucu == "db":
       supheli.append(sunucu)
    elif sunucu == "mail":
          kapali.append(sunucu)
    else:
        acik.append(sunucu)

print("Toplam", len(sunucular))
print("AÇık", len(acik))
print("Kapalı",len(kapali))
print("Kapali olanlar", kapali)
print("şupheli", len(supheli))
print("Şüpheli olanlar",supheli)
