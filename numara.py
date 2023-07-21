import phonenumbers
from phonenumbers import geocoder,carrier,timezone
numara = input("Numarayı gir : ")
telefon = phonenumbers.parse(numara)
print(f"Konum : {geocoder.description_for_number(telefon,'en')}")
print(f"Telefon : {carrier.name_for_number(telefon,'en')}")
print(f"Zaman dilimi : {timezone.time_zones_for_number(telefon)}")
print(f"Geçerlilik durumu : {phonenumbers.is_valid_number(telefon)}")
print(f"Format : {phonenumbers.format_number(telefon,phonenumbers.PhoneNumberFormat.NATIONAL)}")