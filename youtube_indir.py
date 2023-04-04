from pytube import YouTube

link = input("Enter the link:")
yt = YouTube(link)

#video başlığı
print("başlık:" , yt.title)

#video görüntülenme sayısı
print("görüntülenme sayısı:" ,yt.views)

#video uzunluğu
print("uzunluk:" ,yt.length)

#videonun açıklması
print("açıklama:",yt.description)

#beğeni
print("beğeni:" ,yt.rating)

ys = yt.streams.get_highest_resolution()

#indirme başlatılıyor
print("indiriliyor...")

ys.download()

print("indirme tamamlandı!!")
        
