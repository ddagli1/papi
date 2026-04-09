import requests  # HTTP istekleri göndermek için kütüphane (internet üzerinden API'lerle iletişim kurmak)
from urllib.parse import quote  # Metni güvenli bir şekilde URL biçimine dönüştürme işlevi


class ImgAPI:
    # ImgAPI sınıfı, resim oluşturma hizmetiyle yapılan işlemleri yönetir

    def download_image(self, prompt):
        # Görüntünün metin biçimli açıklamasını (promt) alan download_image yöntemini tanımlama.

        encoded_prompt = quote(prompt)
        # Metni URL'ler için güvenli bir biçime dönüştürme.
        # Örneğin: "sevimli robot" → "cute%20robot".
        # Böylece sunucunun isteği doğru şekilde yorumlaması sağlanır.

        url = f"https://image.pollinations.ai/image/{encoded_prompt}"
        # API için istek URL'sini oluşturma.
        # Görsel açıklamasını URL içinde aktarma.

        response = requests.get(url)
        # Sunucuya bir GET isteği gönderiliyor.
        # Sunucu görüntüyü oluşturur ve yanıtta geri gönderir.

        with open("generated_image.jpg", "wb") as file:
            # Bir dosyayı ikili modda (wb) yazma amacıyla açma.
            # Görüntülerle çalışırken ikili modun kullanılması şarttır.

            file.write(response.content)
            # Sunucu yanıtının içeriğini dosyaya yazıyor.
            # response.content, resmin baytlarını içerir.

        print("Resim kaydedildi!")
        # Görüntünün başarıyla kaydedildiğini bildiriyoruz.

        return "generated_image.jpg"
        # Dosya adını döndürme.
        # Bunu yapmak, botun daha sonra resmi kullanıcıya gönderebilmesi açısından faydalı olacaktır.

api = ImgAPI()

if __name__ == "__main__":
    api = ImgAPI()
    api.download_image("cute robot")
