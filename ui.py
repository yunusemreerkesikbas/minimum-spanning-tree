from app import MinimumSpanningTree
import time
mst = MinimumSpanningTree()
# NOT : DÖNGÜ İÇİNDE BİR PROGRAMI BAŞLATTIKTAN SONRA DİĞER PROGRAMA GEÇİNCE(prim algoritması çalıştıktan sonra kruskalı çalıştırmak isteyince) HATA VERİYOR. DÖNGÜ SONLANDIKTAN SONRA PROGRAMI TEKRAR BAŞLATIRSAK(prim çalıştı => döngüyü sonlandır , döngüyü başlat , kruskal çalıştır) HERHANGİ BİR SIKINTI YOK 
print("********** 2021-2022 ÇİZGE KURAMI **********")
print("""
        Minimum Spanning Tree Algoritması
        Minimum Spanning Tree Algoritması Nedir?
            MST algoritması kenar ağırlıklarına (weights) sahip olan bir çizit (graph) yapısı içinde minimal ve kapsayan ağacı (MST) bulan algoritmaya verilen isimdir
        Uygulamamızda güncel olarak 2 adet algoritma vardır:
        Prim's Algoritması - Kruskal Algoritması

        Lütfen yapmak istediğiniz işlemi seçiniz( 1 or 2 ):
        1- Prim's algoritmasını çalıştır
        2- Kruskal algoritmasını çalıştır
        Çıkmak için 'q' tuşuna basınız
      """)
def ui():
    while True:

        choose = input("Seciminiz: ")
        if choose == "1":
            print("Prim's algoritmasını daha iyi anlamak için önce kısa animasyonumuzu izleyin")
            print("Animasyondan çıkmak için 'q' tuşuna basınız")
            time.sleep(2)
            mst.openVideo('./video/prim.mp4', 'Prims Algorithm')
            print("Oluşturulan grafımız temsil ediliyor")
            time.sleep(1.5)
            mst.openImg('Prims Represent','./img/prim.png')
            print('İşleminiz yerine getiriliyor. Lütfen bekleyiniz')
            time.sleep(1)
            mst.prims()
            time.sleep(1)
            mst.openImg('Prims Result','./img/primResult.png')
            print('\n')
        elif choose == '2':
            print("Kruskal algoritmasını daha iyi anlamak için önce kısa animasyonumuzu izleyin")
            print("Animasyondan çıkmak için 'q' tuşuna basınız")
            time.sleep(2)
            mst.openVideo("./video/kruskal.mp4", 'Kruskal Algorithm')
            print("Oluşturulan grafımız temsil ediliyor")
            time.sleep(1.4)
            mst.openImg('Kruskal Represent','./img/kruskal.png')
            print('İşleminiz yerine getiriliyor. Lütfen bekleyiniz')
            time.sleep(1)
            mst.addEdgeToKruskal(0, 1, 10)
            mst.addEdgeToKruskal(1, 2, 7)
            mst.addEdgeToKruskal(2, 3, 11)
            mst.addEdgeToKruskal(3, 4, 3)
            mst.addEdgeToKruskal(5, 6, 1)
            mst.addEdgeToKruskal(6, 7, 11)
            mst.addEdgeToKruskal(7, 8, 14)
            mst.addEdgeToKruskal(1, 6, 8)
            mst.addEdgeToKruskal(2, 7, 2)
            mst.addEdgeToKruskal(3, 8, 20)
            mst.kruskal()
            time.sleep(1.5)
            mst.openImg('Kruskal Result','./img/kruskalResult.png')
        elif choose == 'q':
            print("Çıkış yapılıyor... Yine bekleriz...")
            time.sleep(1)
            break
        else:
            print("OOPPS ! Bir şeyler yanlış gitti tekrar deneyiniz...")
            time.sleep(1)


ui()

         