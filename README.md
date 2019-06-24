# n11_Load_Test
n11KeywordDatası'nda n11 sitesinin arama kısmında tanımlı olan keyword'ler çekilerek
kodu ile csv dosyası halinde istenilen konuma r'n11CekilenDatlar.csv' olarak export edilir.
Export edilmiş olan datalar SearchingLoadTest ile yüklenmiş olan dosya yolu ile
import edilerek random 100 keyword ile n11.com sitesinde Locust framework kullanarak
yük testi yapılır.
Oluşturulan excel dosyası'na aratılmak istenen keyword'ler satır satır yazılıp
SearchingLoadTest içindeki dosya yoluna konumu eklenir
cmd'de SearchingLoadTest'in yüklendiği dosya yolu kullanılıp
rastgele keyword'lerin gönderilmek istendiği websitesi yazılır

Örnek olarak:
locust -f C:\Users\......\SearchingLoadTest.py --host=https://n11.com
dosyaların indirildiği konumda locust komutu çalıştırılırsa hatasız locust engine ayağa kalkacaktır
locust arayüzünden kullanıcı ve yoğunluk parametreleri girilerek test başlatılır
not:dosya yolu yanlış hatası alıyorsanız SearchingLoadTest'in 29. satırındaki dosya yolu güncellenerek
hata giderilir
