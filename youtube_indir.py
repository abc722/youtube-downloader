from pytube import YouTube

class Video():
    link = ''
    
    def __init__(self, link):
        self.link  = link                               #class nedir nasıl olulturulur , contruction nedir nasıl çalıştırılı , calssa fonk. nasıl ayzılır, başka bi sayfadan class nasıl çağrılır, nesne nasıl üretilir.
        self.yt = YouTube(link)
    
    def description(self):
        #video başlığı
        print("başlık:" , self.yt.title)

        #video görüntülenme sayısı
        print("görüntülenme sayısı:" ,self.yt.views)

        #video uzunluğu
        print("uzunluk:" ,self.yt.length)

        #videonun açıklması
        print("açıklama:",self.yt.description)

        #beğeni
        print("beğeni:" ,self.yt.rating)

    def download(self):
        ys = self.yt.streams.get_highest_resolution()

        #indirme başlatılıyor
        print("indiriliyor...")

        ys.download()

        print("indirme tamamlandı!!")        
        
