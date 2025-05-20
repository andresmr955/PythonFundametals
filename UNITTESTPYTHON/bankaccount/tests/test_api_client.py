import unittest, requests
from unittest.mock import patch
from UNITTESTPYTHON.bankaccount.src.exchange_api import get_location

class ApiClientTests(unittest.TestCase):
    
    @patch('src.exchange_api.requests.get')
    def test_get_location_returns_expected_area(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName" : "United States of America",
            "regionName" : "FLORIDA",
            "cityName" : "MIAMI",
        
        }
        
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States of America")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.exchange_api.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [requests.exceptions.RequestException("Service Unavailable"), unittest.mock.Mock(
            status_code = 200,
            json=lambda: {
                "countryName" : "United States of America",
                "regionName" : "FLORIDA",
                "cityName" : "MIAMI",
        
            }
        )]

  
        
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")
         
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States of America")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
     
        # result = get_location("8.8.8.8")
    
    @patch('src.exchange_api.requests.get')
    def test_get_location_service_requess_invalid_ip(self, mock_get):
        mock_response = unittest.mock.Mock()

        mock_response.status_code = 400

        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_location("invalid-ip")