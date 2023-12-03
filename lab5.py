from enum import Enum

class City(Enum):
    LVIV = 1
    KYIV = 2 
    BURSHTYN = 3
    DNIPRO = 4

class WeatherType(Enum):
    SUNNY = 0
    CLOUDY = 1
    RAINY = 2
    FOGGY = 3

class Weather:

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
        return (f"The temperature on {self.day} in {self.city.name}, "
                f"{self.country} was {self.temp} Celsius degrees. The humidity was "
                f"{self.humidity} %, the wind speed was {self.wind_speed} and "
                f"the weather outside is {self.weather_type.name}")

class WeatherCalendar(Weather):
    def __init__(self):
        self.weather_objects = []

    def add_weather_objects(self, obj):
        self.weather_objects.append(obj)

    def find_max_temperature(self):
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
        
    
    def is_lviv_weather(self, humidity, weather_type):
        for obj in self.weather_objects:
            if humidity > 80 and weather_type == WeatherType.RAINY and obj.city is City.LVIV:
                return "The typical day in Lviv"
            else:
                return "You're lucky, man"

        
    def sort_weather(self):
        self.weather_objects.sort(key=lambda x: x.day)

        
def main():
    dnipro_foggy = Weather(1, City.DNIPRO, "Ukraine", 2, 80, 10, WeatherType.FOGGY)
    kyiv_cloudy = Weather(9, City.KYIV, "Ukraine", 4, 67, 7, WeatherType.CLOUDY)
    burshtyn_sunny = Weather(3, City.BURSHTYN, "Ukraine", 3, 72, 8, WeatherType.SUNNY)
    lviv_rainy = Weather(6, City.LVIV, "Ukraine", 7, 89, 9, WeatherType.RAINY)
    lviv_foggy = Weather(5, City.LVIV, "Ukraine", 1, 76, 6, WeatherType.FOGGY)
    
    calendar = WeatherCalendar()
    calendar.add_weather_objects(dnipro_foggy)
    calendar.add_weather_objects(kyiv_cloudy)
    calendar.add_weather_objects(burshtyn_sunny)
    calendar.add_weather_objects(lviv_rainy)
    calendar.add_weather_objects(lviv_foggy)

    print("dnipro_foggy displaying all parameters: ", dnipro_foggy.get_all_parameters())
    print("kyiv_cloudy displaying all parameters: ", kyiv_cloudy.get_all_parameters())
    print("burshtyn_sunny displaying all parameters: ", burshtyn_sunny.get_all_parameters())
    print("lviv_rainy displaying all parameters: ", lviv_rainy.get_all_parameters())
    print("lviv_foggy displaying all parameters: ", lviv_foggy.get_all_parameters())


    print("Max temperature was on", calendar.find_max_temperature())

    for obj in calendar.weather_objects:
        result = calendar.is_lviv_weather(obj.humidity, obj.weather_type)
        print(f"On day {obj.day}, {result}")


    calendar.sort_weather()
    for obj in calendar.weather_objects:
        print(obj.day, obj.city.name, obj.temp, obj.weather_type.name)
    
    print("The End")

if __name__ == "__main__":
    main()
