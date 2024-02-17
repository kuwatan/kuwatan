#requestsモージュールを使用しています
import requests

#JSONデータ取得
tenki_url = 'https://weather.tsukumijima.net/api/forecast/city/200010'
tenki_json = requests.get(tenki_url).json()

d_title = tenki_json["title"]
d_time = tenki_json["description"]["publicTimeFormatted"]
f_dlab1 = tenki_json["forecasts"][1]["dateLabel"]
f_dwea = tenki_json["forecasts"][1]["detail"]["weather"]
f_dwi = tenki_json["forecasts"][1]["detail"]["wind"]
f_tmin = tenki_json["forecasts"][1]["temperature"]["min"]["celsius"]
f_tmax = tenki_json["forecasts"][1]["temperature"]["max"]["celsius"]
copy = tenki_json["copyright"]["title"]

print(d_title,"\n","発表時刻",d_time,"\n",f_dlab1,"の天気は",f_dwea,"\n",f_dwi,"\n""最低気温",f_tmin,"\n""最高気温",f_tmax,"\n",copy)
