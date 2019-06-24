#Bu yazılan kodda n11 sitesinde arama çubuğuna tanımlı keyword'ler
#bulunarak her keyword'ün csv dosyasındaki bir satıra denk gelecek şekilde
#eklenmesi sağlanır
import requests
from bs4 import BeautifulSoup
import csv
t="https://www.n11.com/"
r=requests.get(t)

soup = BeautifulSoup(r.content,"html.parser")

veri = soup.find_all("li",{"class":"subCatMenuItem"})
array=[]
for x in veri:
    x=str(x)
#a değişkenine title'ın bulunduğu indis atanır
    a=x.find('title')
#String içide title'dan sonraki kısım y değişkenine atanır    
    y=x[(a+7):]
#yeni oluşturulan String içinde ">içeren kısım bulunur ve indis b değişkenine atanır
    b=y.find('">')
#asıl keyword'lerin bulunduğu String z değişkenine atanır    
    z=y[:b]
#eğer string içinde &amp bulunamazsa ayrılacak 2 keyword olmadığından direkt olarak
#array'e eklenir
    if(z.find('&amp;')<1):
        array.append(z)
#burada ise &amp yazan yerlerden keyword'le bölünür ve array'e atanır
    else:
        t=(z.split(" &amp; "))
        for j in t:
            array.append(j)
#son olarakta array'in içindeki farklı indisli her değer csv dosyasına farklı bir satır
#olarak eklenir
with open(r'n11CekilenDatalar.csv', 'w',newline='') as csvFile:
    writer = csv.writer(csvFile)
    for i in range(0,len(array)):
        writer.writerow([array[i]])
        
