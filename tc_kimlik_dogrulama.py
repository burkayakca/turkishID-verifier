import requests
import xml.etree.ElementTree as ET
from unicode_tr import unicode_tr #i'nin I olarak büyük harfe çevrilmesini önler

url = "https://tckimlik.nvi.gov.tr/service/kpspublic.asmx"

tckNo = int(input("TC Kimlik: "))
ad = unicode_tr(input(u"Ad: "))
soyad = unicode_tr(input(u"Soyad: "))

dogumYili = int(input("Doğum yılı: "))

payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo>{tckNo}</TCKimlikNo>
      <Ad>{ad.upper()}</Ad>
      <Soyad>{soyad.upper()}</Soyad>
      <DogumYili>{dogumYili}</DogumYili>
    </TCKimlikNoDogrula>
  </soap:Body>
</soap:Envelope>"""

headers = {
     "Content-Type": "text/xml; charset=utf-8",
     "SOAPAction": "http://tckimlik.nvi.gov.tr/WS/TCKimlikNoDogrula"
 }

response = requests.post(url, headers=headers, data=payload.encode("utf-8"))
root = ET.fromstring(response.text)
result = root.find('.//{*}TCKimlikNoDogrulaResult')

print("HTTP Status Code:", response.status_code)

if result is not None:
    if result.text == "true":
        print("Doğrulama başarılı.")
    else:
        print("Doğrulama başarısız. Bilgileri tekrar kontrol ediniz") 

print(input("Çıkmak için herhangi bir tuşa basınız"))