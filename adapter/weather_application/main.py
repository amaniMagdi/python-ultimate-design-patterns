from weather_service_adaptee import WeatherServiceAdaptee
from third_party_weather_service import ThirdPartyWeatherService
from legacy_weather_service import LegacyWeatherService


def main():
    # Instantiate the third-party weather service
    third_party_service = ThirdPartyWeatherService()
    
    # Wrap it with the legacy weather service
    legacy_service = LegacyWeatherService(third_party_service)
    
    # Use the adaptee to adapt the legacy service to the new interface
    weather_service_adaptee = WeatherServiceAdaptee(legacy_service)
    
    # Get temperature data using coordinates
    longitude = -0.1278   # Example: Longitude for London
    latitude = 51.5074    # Example: Latitude for London
    temperature_data = weather_service_adaptee.get_temperature(longitude, latitude)
    
    # Print the converted temperature data
    print("Temperature data:", temperature_data)

if __name__ == "__main__":
    main()
