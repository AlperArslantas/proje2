
import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

# Personel nesneleri
personel1 = Personel(1, "Ahmet", "Yılmaz", "İK", 5000)
personel2 = Personel(2, "Ayşe", "Kaya", "Muhasebe", 6000)

print(personel1)
print(personel2)

# Doktor nesneleri
doktor1 = Doktor(3, "Ali", "Demir", "Kardiyoloji", 8000, "Kardiyolog", 6, "Hastane A")
doktor2 = Doktor(4, "Elif", "Arslan", "Nöroloji", 9000, "Nörolog", 4, "Hastane B")
doktor3 = Doktor(5, "Murat", "Yıldız", "Ortopedi", 8500, "Ortopedist", 10, "Hastane C")

print(doktor1)
print(doktor2)
print(doktor3)

# Hemşire nesneleri
hemsire1 = Hemsire(6, "Zeynep", "Güneş", "Cerrahi", 4000, 40, "Sertifika A", "Hastane A")
hemsire2 = Hemsire(7, "Mehmet", "Çelik", "Pediatri", 4500, 38, "Sertifika B", "Hastane B")
hemsire3 = Hemsire(8, "Hale", "Çetin", "Dahiliye", 4200, 36, "Sertifika C", "Hastane C")

print(hemsire1)
print(hemsire2)
print(hemsire3)

# Hasta nesneleri
hasta1 = Hasta(9, "Fatma", "Kurt", "1992-05-10", "Grip", "İlaç Tedavisi")
hasta2 = Hasta(10, "Kemal", "Bulut", "1988-11-25", "Diyabet", "İnsülin Tedavisi")
hasta3 = Hasta(11, "Seda", "Yılmaz", "1995-03-15", "Hipertansiyon", "Diyet Tedavisi")

print(hasta1)
print(hasta2)
print(hasta3)

# Pandas DataFrame oluşturma
data = {
    "personel_no": [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(), hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
    "ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
    "soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
    "departman": [personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(), None, None, None],
    "maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None],
    "uzmanlik": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None, None, None, None],
    "deneyim_yili": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None, None, None, None],
    "hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None],
    "calisma_saati": [None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), None, None, None],
    "sertifika": [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), None, None, None],
    "hasta_no": [None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
    "dogum_tarihi": [None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
    "hastalik": [None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
    "tedavi": [None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()],
}

df = pd.DataFrame(data)

# Boş olan değişken değerleri için 0 atama
df.fillna(0, inplace=True)

# Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
uzmanlik_gruplari = df[df['uzmanlik'] != 0].groupby('uzmanlik').size()
print("Uzmanlık gruplarına göre doktor sayıları:\n", uzmanlik_gruplari)

# 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
deneyimli_doktorlar = df[(df['deneyim_yili'] > 5) & (df['deneyim_yili'] != 0)].shape[0]
print("5 yıldan fazla deneyime sahip doktor sayısı:", deneyimli_doktorlar)

# Hasta adına göre DataFrame’i alfabetik olarak sıralama
sorted_df = df.sort_values(by='ad')
print("Alfabetik sıraya göre hastalar:\n", sorted_df)

# Maaşı 7000 TL üzerinde olan personelleri bulma
maas_ustundekiler = df[df['maas'] > 7000]
print("Maaşı 7000 TL üzerinde olan personeller:\n", maas_ustundekiler)

# Doğum tarihi 1990 ve sonrası olan hastaları gösterme
df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'], errors='coerce')
sonrasi_hastalar = df[df['dogum_tarihi'] >= '1990-01-01']
print("Doğum tarihi 1990 ve sonrası olan hastalar:\n", sonrasi_hastalar)

# Yeni DataFrame elde etme
yeni_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
print("Yeni DataFrame:\n", yeni_df)
