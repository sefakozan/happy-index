# YZ Uygulamaları ile Doğru Maske Takma Oranı ve Mutluluk İndeksi Hesaplama (HAPPY INDEX)

Türkiye İstatistik Kurumu (TÜİK), her yıl “Yaşam Memnuniyet Araştırması” gerçekleştirmektedir. TÜİK’in 2019 raporuna göre, mutlu olduğunu beyan eden erkeklerin oranı %47,6 iken, kadınlarda bu oran %57,0 olarak hesaplanmıştır. Ayrıca, Sinop %77,6 oranla en mutlu il olarak raporda yer almıştır. TÜİK, memnuniyeti kamu hizmetlerinden, belediye hizmetlerinden gibi kategorilere ayırarak değerlendirmektedir. Birleşmiş Milletler ve Avrupa İstatistik Ofisi ise her yıl ülkeler düzeyinde anket yaparak Dünya Mutluluk İndeksi Raporu yayınlamaktadır.

Yapay zeka (YZ) uygulamaları ile mutluluk indeksi hesaplama, dünyada henüz deneysel düzeyde olsa da, öznel verilerin YZ algoritmalarıyla analiz edilmesi, daha önce elde edilmesi zor olan veri analizlerinin yapılmasını sağlamaktadır. Örneğin, IBM kendi çalışanlarının mutluluk oranlarını ölçmek için, Dubai’de kamu binalarında vatandaşların kamu hizmetinden memnuniyet oranını hesaplamak için, mağazalar ise tüketicilerin memnuniyet oranını ölçmek için YZ kullanmaktadır.

## Proje Açıklaması
Bu projede, 9.000 adet CC0 lisanslı, doğru şekilde medikal yüz maskesi takmış, yanlış maske takmış ve maske takmamış insan yüzlerinden oluşan bir veri kümesi kullanılarak Python programlama dili ile bir **Evrişimli Sinir Ağı (CNN)** modeli geliştirilmiştir. Eğitilen model, **%96 test başarım oranı** elde etmiştir.

Geliştirilen bu model ile birlikte toplam **4 adet CNN modeli** entegre edilerek bir masaüstü uygulaması ile beraber bir web uygulaması oluşturulmuştur. Bu uygulama, bir görüntü akışındaki insan yüzlerini tespit ederek aşağıdaki analizleri gerçekleştirir:
- Yüzde maske bulunuyorsa, **doğru maske takma oranını** hesaplar.
- Yüzde maske bulunmuyorsa, kişinin **cinsiyetini**, **yaşını** ve **mutluluk oranını** tahmin eder.

Uygulama, insanların anlık yüz ifadeleri üzerinden kamera ile veri toplayarak **doğru maske takma oranı** ile **mutluluk indeksinin yaşa, cinsiyete ve zamana göre dağılımını** hesaplamaktadır.

## Kullanım Alanları
- Kamu hizmetlerinden memnuniyet analizi
- Çalışan mutluluğu ölçümü
- Tüketici memnuniyet analizi
- Pandemi döneminde maske kullanım alışkanlıklarının izlenmesi

## Teknik Detaylar
- **Veri Kümesi**: 9.000 CC0 lisanslı görüntü (doğru maske, yanlış maske, maskesiz yüzler)
- **Model**: 4 adet Evrişimli Sinir Ağı (CNN)
- **Programlama Dili**: Python
- **Test Başarım Oranı**: %96
- **Uygulama Türü**: Masaüstü uygulaması, Web uygulaması
- **Fonksiyonlar**:
  - Yüz tespiti
  - Maske takma oranı analizi
  - Cinsiyet ve yaş tahmini
  - Mutluluk indeksi tahmini

## Kurulum ve Kullanım
1. Depoyu klonlayarak projeye erişebilirsiniz:
   ```bash
   git clone https://github.com/sefakozan/happy-index.git
   ```
2. Web sitesini ziyaret edebilirsiniz. 
    > [https://sefakozan.github.io/happy-index](https://sefakozan.github.io/happy-index/)
3. Masaüstü uygulamasını indirebilirsiniz. 
    > [happy-index.exe](https://sefakozan.github.io/happy-index/happy-index.exe)
4. Proje dökümanlarını inceleyebilirsiniz. 
    > [Happy Index - Proje Dökümanı](https://sefakozan.github.io/happy-index/docs/Happy%20Index%20-%20Proje%20D%C3%B6k%C3%BCman%C4%B1.pdf)  
    >  [TÜBİTAK Proje Sunum](https://sefakozan.github.io/happy-index/docs/T%C3%9CB%C4%B0TAK%20Proje%20Sunum.pdf)