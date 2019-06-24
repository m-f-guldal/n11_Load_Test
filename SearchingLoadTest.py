#Bu yazılan kodda locust framework'ü kullanılarak 100 farklı keyword'ün
#csv dosyasından seçilip yük testi yapılması sağlanmıştır
import sys
import csv
import random
from locust import HttpLocust, TaskSet, task

#csv dosyasının içindeki değerleri bir dizi olarak döndüren fonksiyon
def readcsv(filename):	
    
    try:
        ifile = open(filename, "rU")
        reader = csv.reader(ifile, delimiter=";")
        pass
    except:
        print("yanlış dosya yada yanlış dosya yolu")
        sys.exit()
    

    rownum = 0	
    array = []

    for row in reader:
        array.append (row)
        rownum += 1
    
    ifile.close()
    return array
file=r"n11CekilenDatalar.csv"
Array1=[]
Array1=readcsv(file)


Array2=[]
#csv dosya yoluwhile True:


#csv dosyasının içinde 100'den daha az keyword olması halinde
#csv dosyasının içinde bulunan keyword kadar eleman dizinin içine atanır
if(len(Array1)<100):
    Array2=Array1
#csv dosyasının içinde istenildiği gibi 100'den daha fazla keyword varsa
#seçilen rastgele 100 keyword üzerinden yük testi yapılır
else:
    for i in range(0,100):
        x=random.randint(1,len(Array1)-1)
        Array2.append(Array1[x])
        Array1.remove(Array1[x])
#bir dizi içerisine bir csv dosyasından eklenmiş 100 farklı rastgele keyword
#indis sırasına göre istenilen kullanıcı sayısıyla arama islemi gerceklestirilir.
class WebsiteTasks(TaskSet):
    @task
    def query(self):
        for i in range(0,len(Array2)):
            self.client.get("/arama?q="+(str)(Array2[i]))
     
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000

