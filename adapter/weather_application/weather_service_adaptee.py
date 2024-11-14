from weather_service_adapter import WeatherServiceAdapter

class WeatherServiceAdaptee(WeatherServiceAdapter):
    def __init__(self, legacy_weather_service):
        self._legacy_weather_service = legacy_weather_service

    def get_temperature(self, longitude: float, latitude: float): 
        temp_in_xml = self._legacy_weather_service.get_temperature(self.get_city_of(longitude, latitude), 
                                                                   self.get_country_of(longitude, latitude))
        return self.convert_xml_data_to_json(temp_in_xml)

    def convert_xml_data_to_json(self, xml_data: str):
        print(f"Converting ....")
        return "Converted Data from XML into JSON"


    def get_city_of(self, longitude: float, latitude: float) -> str:
        print(f"Extracting city of longitude: {longitude} and latitude: {latitude}")
        return "City"

    def get_country_of(self, longitude: float, latitude: float) -> str:
        print(f"Extracting country of longitude: {longitude} and latitude: {latitude}")
        return "Country"
