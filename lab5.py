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

class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country
    
class WindAndType:
    def __init__(self, wind_speed, weather_type):
        self.wind_speed = wind_speed
        self.weather_type = weather_type

class TempAndHumidity:
    def __init__(self, temp, humidity):
        self.validate_humidity(humidity)
        self.temp = temp
        self.humidity = humidity

    def validate_humidity(self, humidity):
        if not 0 <= humidity <= 100:
            raise ValueError("Humidity must be a number from 0 to 100")

class Weather:

    def __init__(self, day, location, temp_hum, wind_and_weather_type):
        self.validate_day(day)
        self.day = day
        self.location = location
        self.temp_hum = temp_hum
        self.wind_and_weather_type = wind_and_weather_type

    def validate_day(self, day):
        if day < 0:
            raise ValueError("Day must be a positive number")
    
    def __del__(self):
        print("Cleanup has been completed")
        
    def get_all_parameters(self):
        return (f"The temperature on {self.day} in {self.location.city.name}, "
                f"{self.location.country} was {self.temp_hum.temp} Celsius degrees. The humidity was "
                f"{self.temp_hum.humidity} %, the wind speed was {self.wind_and_weather_type.wind_speed} and "
                f"the weather outside is {self.wind_and_weather_type.weather_type.name}")

class WeatherCalendar(Weather):
    def __init__(self):
        super().__init__(day=0, location=None, temp_hum=0, wind_and_weather_type=None)
        self.weather_objects = []

    def add_weather_objects(self, obj):
        self.weather_objects.append(obj)

    def find_max_temperature(self):
        max_temp = None
        max_temp_day = None
        for obj in self.weather_objects:
             if max_temp is None or obj.temp_hum.temp > max_temp:
                  max_temp = obj.temp_hum.temp
                  max_temp_day = obj.day
        if max_temp_day is not None:
            return max_temp_day
        else:
            return "Not enough data"
        
    
    def is_lviv_weather(self, temp_hum,  wind_and_weather_type, location):
        for obj in self.weather_objects:
            if temp_hum.humidity > 80 and wind_and_weather_type.weather_type == WeatherType.RAINY 
                and location.city == City.LVIV:
                return "The typical day in Lviv"
            else:
                return "You're lucky, man"

        
    def sort_weather(self):
        self.weather_objects.sort(key=lambda x: x.day)

        
def main():
    dnipro_foggy = Weather(1, location=Location(City.DNIPRO, "Ukraine"),
                           temp_hum=TempAndHumidity(2, 80), wind_and_weather_type=WindAndType(10, WeatherType.FOGGY))
    kyiv_cloudy = Weather(9, location=Location(City.KYIV, "Ukraine"),
                          temp_hum=TempAndHumidity(4, 67), wind_and_weather_type=WindAndType(7, WeatherType.CLOUDY))
    burshtyn_sunny = Weather(3, location=Location(City.BURSHTYN, "Ukraine"),
                             temp_hum=TempAndHumidity(3, 72), wind_and_weather_type=WindAndType(8, WeatherType.SUNNY))
    lviv_rainy = Weather(6, location=Location(City.LVIV, "Ukraine"),
                         temp_hum=TempAndHumidity(7, 89), wind_and_weather_type=WindAndType(9, WeatherType.RAINY))
    lviv_foggy = Weather(5, location=Location(City.LVIV, "Ukraine"),
                         temp_hum=TempAndHumidity(1, 76), wind_and_weather_type=WindAndType(6, WeatherType.FOGGY))
    
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
        result = calendar.is_lviv_weather(obj.temp_hum, obj.wind_and_weather_type, obj.location)
        print(f"On day {obj.day}, {result}")


    calendar.sort_weather()
    for obj in calendar.weather_objects:
        print(obj.day, obj.location.city.name, obj.temp_hum.temp, obj.wind_and_weather_type.weather_type.name)
    
    print("The End")

if __name__ == "__main__":
    main()
