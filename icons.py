import getData 
import credentials

city = credentials.city
api_key = credentials.api_key

res = getData.fetchJson(city, api_key)

icon_list = {
	"01d" : '',    # Clear sky - day
        "01n" : '',	# Clear sky - night
        "02d" : '',	# Few clouds (11-25%) - day
        "02n" : '',	# Few clouds (11-25%) - night
        "03d" : '', 	# Scattered clouds (25-50%) - day/night
        "03n" : '',
        "04d" : '',
        "04n" : '',	# Broken / Overcast clouds (51-84% / 85-100%) - day/night
        "09d" : '',	# Shower rain - day
        "09n" : '',	# Shower rain - night
        "10d" : '',	# Moderate / heavy rain - day
        "10n" : '',	# Moderate / heavy rain - night
        "11d" : '',	# Thunderstorm - day
        "11n" : '',	# Thunderstorm - night
        "13d" : '',		# Snow - day
        "13n" : '',	# Snow - night
        "50d" : '',	# Fog - day
        "50n" : '',	# Fog - night
}

icon = res['weather'][0]['icon']
#print(icon_id)
print(icon_list[icon])
