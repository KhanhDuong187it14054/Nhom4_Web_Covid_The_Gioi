from covid import Covid
import json
covid = Covid(source="worldometers")

world = covid.get_status_by_country_name('world')

aDict = [
    {
        "country": world['country'],
        "confirmed": world['confirmed'],
        "deaths": world['deaths'],
        "recovered": world['recovered']
    }
]

list_country = ['USA','India','Brazil','UK','Italy','Germany','Malaysia','Thailand','VietNam','Singapore','China']

for country in list_country:
    x = covid.get_status_by_country_name(country)
    x = {
        "country": x['country'],
        "confirmed": x['confirmed'],
        "deaths": x['deaths'],
        "recovered": x['recovered']
    }
    aDict.append(x)

jsonString = json.dumps(aDict)
jsonFile = open("Nhom4_Web_Covid_The_Gioi/model/data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()