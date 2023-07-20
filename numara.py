import phonenumbers
from phonenumbers import geocoder,carrier,timezone
numara = input("Enter number : ")
telefon = phonenumbers.parse(numara)
print(f"Location : {geocoder.description_for_number(telefon,'en')}")
print(f"Carrier : {carrier.name_for_number(telefon,'en')}")
print(f"Time zone : {timezone.time_zones_for_number(telefon)}")
print(f"Geçerlilik durumu : {phonenumbers.is_valid_number(telefon)}")
print(f"Format : {phonenumbers.format_number(telefon,phonenumbers.PhoneNumberFormat.NATIONAL)}")
print(f"")