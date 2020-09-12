import urllib.request
from pyowm import OWM

"""
input: 위치
output: [온도, 습도, 풍속, 하늘]
ex) weather(창원) --> [13.0, 82, 2.6, 'light rain']
"""

# KEY 불법 사용을 금지합니다.
def changing(location: str) -> str:
    client_id = "yMvFjhkkzdTliU0Ik8mW"
    client_secret = "gjgnzPrNqr"

    encText = urllib.parse.quote(location)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))

    response_body = response.read().decode('utf-8')
    return(response_body[152:-4])



# KEY 불법 사용을 금지합니다.
def weather(location:str)->list:
    owm = OWM("c20815c166952daa39b576c27f888454")
    obs = owm.weather_at_place(changing(location))
    observation = obs.get_weather()
    temperature = observation.get_temperature(unit='celsius')
    cloud = str(observation)
    humidity = observation.get_humidity()
    wind = observation.get_wind()

    return [temperature['temp'], humidity, wind['speed'], cloud[102:-1]]




if __name__ == "__main__":
    #test
    print(weather("쿠미"))
