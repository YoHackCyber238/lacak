"""
   http://ip-api.com/json/IP_ADDRES
   https://www.google.com/maps/@LAT,LON,9z?h1=id
"""

import requests
import json

print("==================================")
print("||      Tools Lacak Lokasi      ||")
print("==================================")
print("||        By YoHackCyber        ||")
print("==================================")

ipaddress = input("Masukkan IP Address : ")
iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")
if iprequest.status_code == 200:
    ipdata = json.loads(iprequest.text)
    if ipdata["status"] == "success":
        print("Country :", ipdata["country"], ipdata["countryCode"])
        print("Region :", ipdata["region"], ipdata["regionName"])
        print("City :", ipdata["city"])
        print("Zip :", ipdata["zip"])
        lat = ipdata["lat"]
        lon = ipdata["lon"]
        print("Location :", lat, ",", lon)

        maps = f"https://www.google.com/maps/@{lat},{lon},9z?h1=id"
        print("Maps :", maps)

        print("Timezone :", ipdata["timezone"])
        print("ISP :", ipdata["isp"])
        print("IP Address :", ipdata["query"])