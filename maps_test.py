import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCJ2GhgOOCaoypV0JCC4NnxS-M0enWpN64')

reverse_geocode_result = gmaps.reverse_geocode((34.852733, -82.3915677))

print(reverse_geocode_result[0]['formatted_address'])

#####################################################################################

geocode_result = gmaps.geocode("650 N Academy St, Greenville, SC 29601, USA")

print(geocode_result[0]['geometry']['location'])
