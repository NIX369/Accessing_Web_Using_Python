import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print("Retrieving: ", url)

    urlhandler = urllib.request.urlopen(url)
    data = urlhandler.read().decode()

    print("Retrieved", len(data), "Characters")

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print("=== Failed to retrieve ===")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]['geometry']['location']['lat']
    lng = js["results"][0]['geometry']['location']['lng']

    print("Lat: ",lat, "Long: ",lng)

    location = js['results'][0]['formatted_address']
    print(location)