from enum import Enum

class City(Enum):
    LVIV = 1
    KYIV = 2 
    BURSHTYN = 3

class WeatherType(Enum):
    SUNNY = 0
    CLOUDY = 1
    RAINY = 2
    FOGGY = 3

class Weather(object):

    def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type):
        self.day = day
        self.city = city
        self.country = country
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.weather_type = weather_type
        
    def __del__(self):
        print("Cleanup has been completed")
        
    def get_all_parameters(self):

        """
        Explanatiom huy na blude
        :return: pizdec
        """
        return f"The temperature on {self.day} in {self.city.name}, {self.country} was {self.temp} Celsius degrees. The humidity was {self.humidity} %, the wind speed was {self.wind_speed} and the weather outside is {self.weather_type.name}" 



class WeatherCalendar(Weather):
    def __init__(self):
        self.weather_objects = []

    def add_weather_objects(self, obj):
        self.weather_objects.append(obj)

    def findMaxTemperature(self):
        max_temp = None
        max_temp_day = None
        for obj in self.weather_objects:
             if max_temp is None or obj.temp > max_temp:
                  max_temp = obj.temp
                  max_temp_day = obj.day
        if max_temp_day is not None:
            return max_temp_day
        else:
            return "Not enough data"
        
    
    def isLvivWeather(self, humidity, weather_type):
        for obj in self.weather_objects:
            if humidity > 80 and weather_type == WeatherType.RAINY and obj.city is City.LVIV:
                return "The typical day in Lviv"
            else:
                return "You're lucky, man"

        
    def sort_weather(self):
        self.weather_objects.sort(key=lambda x: x.day)

        
def main():
    weather1 = Weather(1, City.LVIV, "Ukraine", 2, 80, 10, WeatherType.FOGGY)
    weather2 = Weather(9, City.KYIV, "Ukraine", 4, 67, 7, WeatherType.CLOUDY)
    weather3 = Weather(3, City.BURSHTYN, "Ukraine", 3, 72, 8, WeatherType.SUNNY)
    weather4 = Weather(6, City.LVIV, "Ukraine", 7, 89, 9, WeatherType.RAINY)
    weather5 = Weather(5, City.LVIV, "Ukraine", 1, 76, 6, WeatherType.FOGGY)
    
    calendar = WeatherCalendar()
    calendar.add_weather_objects(weather1)
    calendar.add_weather_objects(weather2)
    calendar.add_weather_objects(weather3)
    calendar.add_weather_objects(weather4)
    calendar.add_weather_objects(weather5)

    print("weather1 getAll: ", weather1.get_all_parameters())
    print("weather2 getAll: ", weather2.get_all_parameters())
    print("weather3 getAll: ", weather3.get_all_parameters())
    print("weather4 getAll: ", weather4.get_all_parameters())
    print("weather5 getAll: ", weather5.get_all_parameters())


    print("Max temperature was on", calendar.findMaxTemperature())

    for obj in calendar.weather_objects:
        result = calendar.isLvivWeather(obj.humidity, obj.weather_type)
        print(f"On day {obj.day}, {result}")


    calendar.sort_weather()
    for obj in calendar.weather_objects:
        print(obj.day, obj.city.name, obj.temp, obj.weather_type.name)
    
    print("The End")

if __name__ == "__main__":
    main()
