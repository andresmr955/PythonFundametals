import unittest
from unittest.mock import patch
import requests
from weather import get_weather

class TestWeatherAPI(unittest.TestCase):

    @patch('weather.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"weather" : "sunny"}

        result = get_weather("london")
        self.assertEqual(result, "The weather in london is sunny")

    @patch('weather.requests.get')
    def test_get_weather_api_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("API Down")

        with self.assertRaises(requests.exceptions.RequestException):
            get_weather("tokyo")

if __name__ == "__main__":
    unittest.main()