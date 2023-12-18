#Sınıf Geçme/Kalma Değişkeni
gectin = ('✨Dersten Geçtin✨') #Made By xLiteChesy
kaldin = ('😑Dersten Kaldın😑') #Made By xLiteChesy

#Belge Aldın/Almadın Değişkeni
belgeyok = ('😑Belge Almadın😑') #Made By xLiteChesy
belge1 = ('🎈Teşekkür Belgesi Aldın✨') #Made By xLiteChesy
belge2 = ('🎈Taktir Belgesi Aldın✨') #Made By xLiteChesy
belge3 = ('🎈Onur Belgesi Aldın✨') #Made By xLiteChesy

#Kullanıcıya Değer Verdirme
print('-----NOT DEĞERLERİ-----') #Made By xLiteChesy
not1 = int(input('1. Not Gir => ')) #Made By xLiteChesy
not2 = int(input('2. Not Gir => ')) #Made By xLiteChesy
szl = int(input('Sözlü Gir => ')) #Made By xLiteChesy
proje = int(input('Proje Gir => ')) #Made By xLiteChesy
print('-----NOT DEĞERLERİ-----') #Made By xLiteChesy

#Hesaplama Sistemi Ders Sayısına Göre
ort=int(not1)+int(not2)+int(szl)+int(proje) #Made By xLiteChesy
sonuc = ort/4 #Made By xLiteChesy

#Hesaplama Sisteminin Sonucu
print('-----SONUÇ-----') #Made By xLiteChesy
print('Ortalama => {0}'.format(sonuc)) #Made By xLiteChesy
print('-----SONUÇ-----')

print('-----TAKTİR / SINIF GEÇME-----') #Made By xLiteChesy
#Sınıfda Geçme/Kalma Sistemi Hesaplama ve Ekrana Çıkartma
if sonuc<50 :print(kaldin) #Made By xLiteChesy
if sonuc==50 :print(gectin) #Made By xLiteChesy
if sonuc>50 :print(gectin) #Made By xLiteChesy

#Belge sistemi Hesaplama ve Ekrana Çıkartma 
if sonuc<50 :print(belgeyok) #Made By xLiteChesy
if sonuc==50 :print(belgeyok) #Made By xLiteChesy
if sonuc>=70 :print(belge1) #Made By xLiteChesy
if sonuc>=85 :print(belge2) #Made By xLiteChesy
if sonuc>=100 :print(belge3) #Made By xLiteChesy
print('-----TAKTİR / SINIF GEÇME-----') #Made By xLiteChesy

#Yapımcı ve sosyal medya hesaplarının isimleri
print('-----/YAPIMCI\-----') #Made By xLiteChesy
print('✨\Made BY xLiteChesy/✨') #Made By xLiteChesy
print('✨\github.com/xLiteChesy/✨') #Made By xLiteChesy
print('✨\Yapım Tarihi: 30.11.2023/✨')
print('-----/YAPIMCI\-----') #Made By xLiteChesy