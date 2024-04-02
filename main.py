from twilio.rest import Client

import requests

resource = {
    "200": "Thunderstorm with light rain",
    "201": "Thunderstorm with rain",
    "202": "Thunderstorm with heavy rain",
    "210": "Light thunderstorm",
    "211": "Thunderstorm",
    "212": "Heavy thunderstorm",
    "221": "Ragged thunderstorm",
    "230": "Thunderstorm with light drizzle",
    "231": "Thunderstorm with drizzle",
    "232": "Thunderstorm with heavy drizzle",
    "300": "Light intensity drizzle",
    "301": "Drizzle",
    "302": "Heavy intensity drizzle",
    "310": "Light intensity drizzle rain",
    "311": "Drizzle rain",
    "312": "Heavy intensity drizzle rain",
    "313": "Shower rain and drizzle",
    "314": "Heavy shower rain and drizzle",
    "321": "Shower drizzle",
    "500": "Light rain",
    "501": "Moderate rain",
    "502": "Heavy intensity rain",
    "503": "Very heavy rain",
    "504": "Extreme rain",
    "511": "Freezing rain",
    "520": "Light intensity shower rain",
    "521": "Shower rain",
    "522": "Heavy intensity shower rain",
    "531": "Ragged shower rain",
    "600": "Light snow",
    "601": "Snow",
    "602": "Heavy snow",
    "611": "Sleet",
    "612": "Light shower sleet",
    "613": "Shower sleet",
    "615": "Light rain and snow",
    "616": "Rain and snow",
    "620": "Light shower snow",
    "621": "Shower snow",
    "622": "Heavy shower snow",
    "701": "Mist",
    "711": "Smoke",
    "721": "Haze",
    "731": "Sand/dust whirls",
    "741": "Fog",
    "751": "Sand",
    "761": "Dust",
    "762": "Volcanic ash",
    "771": "Squalls",
    "781": "Tornado",
    "800": "Clear sky",
    "801": "Few clouds: 11-25%",
    "802": "Scattered clouds: 25-50%",
    "803": "Broken clouds: 51-84%",
    "804": "Overcast clouds: 85-100%"
}
account_sid = "input your account SID"
auth_token = "input your auth token"
api_key = "input API key"
latitude = 8.564281
longitude = 39.289491
data = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")
data.raise_for_status()
response = data.json()

weather = [response["list"][i]["weather"][0] for i in range(4)]
will_rain = False
condition = ''
for i in weather:
    codes = i['id']
    if codes < 700:
        will_rain = True
        condition = resource[f"{codes}"]

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"There is going to be {condition}. remember to bring an umbrella.",
        from_='+12563914059',
        to='+251931523743'
    )
    print(message.status)
